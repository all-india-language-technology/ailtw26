#!/usr/bin/env python3
"""
build_handbook_tex.py — Convert handbook Markdown sources to LaTeX.

Requires: pandoc  https://pandoc.org/installing.html
          A standard LaTeX distribution (MiKTeX or TeX Live) for compilation.

Output:   pdf/tex/        — one .tex fragment per chapter / appendix
          pdf/handbook.tex — master document (compile with xelatex)

Usage:
    cd pdf
    python build_handbook_tex.py
    xelatex handbook.tex
    xelatex handbook.tex   # second pass builds ToC and cross-references
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────
ROOT         = Path(__file__).resolve().parents[1]
HANDBOOK_DIR = ROOT / "handbook"
OUT_DIR      = ROOT / "output"
TEX_DIR      = OUT_DIR / "tex"

# Canonical reading order — must match pdf/build_handbook_html.py
CHAPTERS = [
    "ch00-frontmatter.md",
    "ch01-how-llms-work.md",
    "ch02-anatomy-of-a-prompt.md",
    "ch03-master-formula.md",
    "ch04-advanced-techniques.md",
    "ch05-prompting-by-lane.md",
]
APPENDICES = [
    "app-A-glossary.md",
    "app-B-risk-reference.md",
    "app-C-lane-reference.md",
    "app-D-prompt-templates.md",
    "app-E-meta-prompting.md",
    "app-F-attention-paper.md",
    "app-G-beyond-basics.md",
    "app-H-minority-languages.md",
    "app-I-how-this-was-made.md",
]
ALL_FILES = CHAPTERS + APPENDICES


# ── Pandoc check ──────────────────────────────────────────────────────────
def check_pandoc() -> None:
    if not shutil.which("pandoc"):
        print(
            "ERROR: pandoc not found.\n"
            "Install it from https://pandoc.org/installing.html\n"
            "Then re-run this script."
        )
        sys.exit(1)


# ── Inline markdown → LaTeX helper ───────────────────────────────────────
# Used inside raw-LaTeX blocks that Pandoc won't process.
def inline_md_to_tex(text: str) -> str:
    """Convert inline Markdown (bold, italic, code) to LaTeX equivalents."""
    # Inline code — do first so backticks don't confuse bold/italic
    text = re.sub(r"`([^`]+)`", lambda m: r"\texttt{" + tex_escape(m.group(1)) + r"}", text)
    # Bold **...**
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text, flags=re.DOTALL)
    # Italic *...* — single-line only; don't span newlines to prevent runaway matches
    text = re.sub(r"(?<!\*)\*(?!\*)([^\n*]+?)(?<!\*)\*(?!\*)", r"\\textit{\1}", text)
    return text


# ── LaTeX special-character escape ───────────────────────────────────────
_TEX_TRANS = str.maketrans({
    "&":  r"\&",
    "%":  r"\%",
    "$":  r"\$",
    "#":  r"\#",
    "_":  r"\_",
    "{":  r"\{",
    "}":  r"\}",
    "~":  r"\textasciitilde{}",
    "^":  r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
})

def tex_escape(s: str) -> str:
    return s.translate(_TEX_TRANS)


def _convert_placeholders(text: str) -> str:
    """Wrap [fill-in placeholder] text in \\placeholder{} raw LaTeX command."""
    def _repl(m: re.Match) -> str:
        return r"\placeholder{" + tex_escape(m.group(1)) + r"}"
    # Match [text] not followed by ( to avoid Markdown link syntax
    return re.sub(r"\[([^\]\n]+)\](?!\()", _repl, text)


# ── Emoji stripper ────────────────────────────────────────────────────────
_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002702-\U000027B0"
    "\U0001F600-\U0001F64F"
    "\u2600-\u26FF"
    "\u2700-\u27BF"
    "]+",
    flags=re.UNICODE,
)

def strip_emoji(md: str) -> str:
    return _EMOJI_RE.sub("", md)


# ── Pre-processing ────────────────────────────────────────────────────────
# Transforms handbook-specific Markdown patterns into raw LaTeX that Pandoc
# passes through unchanged (requires +raw_tex in --from flags).

def preprocess(md: str) -> str:
    md = strip_emoji(md)
    md = _convert_chapter_headers(md)
    md = _convert_callout_blockquotes(md)
    md = _convert_example_labels(md)
    return md


def _convert_chapter_headers(md: str) -> str:
    """
    > **Session tag:** Foundations
    > **Key question:** Why does the exact wording…
    → \\chapterheader{Foundations}{Why does the exact wording…}
    """
    def _repl(m: re.Match) -> str:
        block = m.group(0)
        tag_m = re.search(r"\*\*Session tag:\*\*\s*(.+?)(?:\s{2,})?$", block, re.MULTILINE)
        q_m   = re.search(r"\*\*Key question:\*\*\s*(.+?)$",            block, re.MULTILINE)
        tag = tex_escape((tag_m.group(1).strip() if tag_m else ""))
        q   = tex_escape((q_m.group(1).strip()   if q_m   else ""))
        return f"\\chapterheader{{{tag}}}{{{q}}}\n\n"

    # Match a contiguous block of > lines that contains "Session tag:"
    return re.sub(
        r"(?m)^(?:> [^\n]*\n)*> \*\*Session tag:\*\*[^\n]*\n(?:> [^\n]*\n)*",
        _repl,
        md,
    )


def _convert_callout_blockquotes(md: str) -> str:
    """
    Converts labelled callout blockquotes:
        > **Note:** Some important note.
        > **Data sensitivity note:** Extended note that may span the line.
    → \\begin{callout}{Note} ... \\end{callout}

    Deliberately skips:
    - Turn N: patterns (multi-turn conversation examples in app-E)
    - Bare quoted questions (> **"Is this published?"**)
    """
    _SKIP = re.compile(r"^Turn \d+$|^\"")

    def _repl(m: re.Match) -> str:
        block = m.group(0)
        stripped = re.sub(r"(?m)^> ?", "", block).strip()
        label_m = re.match(r"\*\*([^*]+):\*\*\s*(.*)", stripped, re.DOTALL)
        if not label_m:
            return block
        label = label_m.group(1).strip()
        if _SKIP.match(label):
            return block
        body = inline_md_to_tex(label_m.group(2).strip())
        return f"\\begin{{callout}}{{{tex_escape(label)}}}\n{body}\n\\end{{callout}}\n\n"

    return re.sub(
        r"(?m)^(> \*\*[^*\"]+:\*\*[^\n]*(?:\n> [^\n]*)*)\n",
        _repl,
        md,
    )


def _convert_example_labels(md: str) -> str:
    """
    **Weak prompt:**
    > quoted prompt text…
    → \\begin{examplebad}{Weak prompt} quoted prompt text… \\end{examplebad}
    """
    LABELS = [
        (r"\*\*Weak prompt:\*\*",                    "examplebad",  "Weak prompt"),
        (r"\*\*Strong prompt:\*\*",                  "examplegood", "Strong prompt"),
        (r"\*\*Stronger prompt:\*\*",                "examplegood", "Stronger prompt"),
        (r"\*\*Strong prompt \(using CoT\):\*\*",    "examplegood", "Strong prompt (using CoT)"),
        (r"\*\*Meta-generated prompt[^*]*:\*\*",     "examplegood", "Meta-generated prompt"),
    ]
    for pattern, env, label in LABELS:
        def _repl(m: re.Match, env: str = env, label: str = label) -> str:
            quote = re.sub(r"(?m)^> ?", "", m.group("quote")).strip()
            quote = _convert_placeholders(quote)
            quote = inline_md_to_tex(quote)
            return (
                f"\\begin{{{env}}}{{{label}}}\n"
                f"{quote}\n"
                f"\\end{{{env}}}\n\n"
            )
        md = re.sub(
            rf"(?m)^{pattern}\s*\n(?P<quote>(?:>[^\n]*\n)+)",
            _repl,
            md,
        )
    return md


# ── Pandoc invocation ─────────────────────────────────────────────────────
_PANDOC_CMD = [
    "pandoc",
    "--from=markdown+raw_tex+smart",
    "--to=latex",
    "--wrap=none",
]

def md_to_tex(md_text: str, source_name: str) -> str:
    prepped = preprocess(md_text)
    result = subprocess.run(
        _PANDOC_CMD,
        input=prepped,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"  [pandoc error in {source_name}]\n  {result.stderr.strip()}", file=sys.stderr)
    return result.stdout


# ── Post-processing ───────────────────────────────────────────────────────

def _promote_headings(tex: str) -> str:
    """
    Pandoc fragment: h1→\\section, h2→\\subsection, h3→\\subsubsection, h4→\\paragraph
    We need:         h1→\\chapter,  h2→\\section,    h3→\\subsection,    h4→\\subsubsection
    Use temp tokens to avoid double-replacement.
    """
    tex = tex.replace(r"\paragraph{",     r"\XPARA{")
    tex = tex.replace(r"\subsubsection{", r"\XSUBSUB{")
    tex = tex.replace(r"\subsection{",    r"\XSUB{")
    tex = tex.replace(r"\section{",       r"\chapter{")
    tex = tex.replace(r"\XSUB{",          r"\section{")
    tex = tex.replace(r"\XSUBSUB{",       r"\subsection{")
    tex = tex.replace(r"\XPARA{",         r"\subsubsection{")
    return tex


def postprocess(tex: str, stem: str) -> str:
    tex = _promote_headings(tex)

    # ch00 is the preface — we don't want a numbered chapter, and the
    # opening "# Prompt with Precision" is already on the title page.
    if stem == "ch00-frontmatter":
        # Remove the redundant book-title chapter heading
        tex = re.sub(r"\\chapter\{[^}]*\}\n?", "", tex, count=1)

    # Appendix files: strip "Appendix X: " / "Appendix X — " prefix so
    # LaTeX's own \appendix labelling doesn't produce "Appendix A: Appendix A: …"
    if stem.startswith("app-"):
        tex = re.sub(r"(\\chapter\{)Appendix\s+[A-F][:\s\u2013\u2014\-]+\s*", r"\1", tex)

    return tex


# ── LaTeX preamble ────────────────────────────────────────────────────────
PREAMBLE = r"""
\documentclass[11pt,a4paper,twoside,openright]{book}

%% ── Encoding & fonts ────────────────────────────────────────────────────
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}

%% ── Page geometry ───────────────────────────────────────────────────────
\usepackage[
  a4paper,
  top=25mm, bottom=28mm,
  inner=28mm, outer=22mm,
  headheight=14pt,
]{geometry}

%% ── Running headers ─────────────────────────────────────────────────────
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\nouppercase{\leftmark}}
\fancyhead[RO]{\small\nouppercase{\rightmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}

%% ── Typography ──────────────────────────────────────────────────────────
\usepackage{microtype}
\usepackage{parskip}
\setlength{\parindent}{0pt}

%% ── Colours ─────────────────────────────────────────────────────────────
\usepackage[dvipsnames,svgnames,table]{xcolor}
\definecolor{brandblue}{HTML}{0F5D79}
\definecolor{goodgreen}{HTML}{1E7F54}
\definecolor{badred}{HTML}{A74B28}
\definecolor{calloutbg}{HTML}{EEF5F8}
\definecolor{calloutborder}{HTML}{7AA6BF}
\definecolor{goodbg}{HTML}{E9F7EF}
\definecolor{badbg}{HTML}{FDF0EA}
\definecolor{codebg}{HTML}{F5F8FB}
\definecolor{muted}{HTML}{5F6F82}

%% ── Tables ──────────────────────────────────────────────────────────────
\usepackage{calc}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{tabularx}
\renewcommand{\arraystretch}{1.3}

%% ── Lists ───────────────────────────────────────────────────────────────
\usepackage{enumitem}
\setlist{noitemsep, topsep=4pt, leftmargin=*}

%% ── Pandoc syntax highlighting ─────────────────────────────────────────
\usepackage{fancyvrb}
\usepackage{framed}
\newcounter{none}% satisfies \def\LTcaptype{none} in pandoc longtable output
\definecolor{shadecolor}{RGB}{248,248,248}
\newenvironment{Shaded}{\begin{snugshade}}{\end{snugshade}}
\newcommand{\VerbBar}{|}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}}
\newcommand{\AlertTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{#1}}}
\newcommand{\AnnotationTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textbf{\textit{#1}}}}
\newcommand{\AttributeTok}[1]{\textcolor[rgb]{0.77,0.63,0.00}{#1}}
\newcommand{\BaseNTok}[1]{\textcolor[rgb]{0.00,0.00,0.81}{#1}}
\newcommand{\BuiltInTok}[1]{#1}
\newcommand{\CharTok}[1]{\textcolor[rgb]{0.31,0.60,0.02}{#1}}
\newcommand{\CommentTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textit{#1}}}
\newcommand{\CommentVarTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textbf{\textit{#1}}}}
\newcommand{\ConstantTok}[1]{\textcolor[rgb]{0.00,0.00,0.00}{#1}}
\newcommand{\ControlFlowTok}[1]{\textcolor[rgb]{0.13,0.29,0.53}{\textbf{#1}}}
\newcommand{\DataTypeTok}[1]{\textcolor[rgb]{0.13,0.29,0.53}{#1}}
\newcommand{\DecValTok}[1]{\textcolor[rgb]{0.00,0.00,0.81}{#1}}
\newcommand{\DocumentationTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textbf{\textit{#1}}}}
\newcommand{\ErrorTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{#1}}}
\newcommand{\ExtensionTok}[1]{#1}
\newcommand{\FloatTok}[1]{\textcolor[rgb]{0.00,0.00,0.81}{#1}}
\newcommand{\FunctionTok}[1]{\textcolor[rgb]{0.02,0.16,0.49}{#1}}
\newcommand{\ImportTok}[1]{#1}
\newcommand{\InformationTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textbf{\textit{#1}}}}
\newcommand{\KeywordTok}[1]{\textcolor[rgb]{0.13,0.29,0.53}{\textbf{#1}}}
\newcommand{\NormalTok}[1]{#1}
\newcommand{\OperatorTok}[1]{\textcolor[rgb]{0.81,0.36,0.00}{\textbf{#1}}}
\newcommand{\OtherTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{#1}}
\newcommand{\PreprocessorTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textit{#1}}}
\newcommand{\RegionMarkerTok}[1]{#1}
\newcommand{\SpecialCharTok}[1]{\textcolor[rgb]{0.00,0.00,0.00}{#1}}
\newcommand{\SpecialStringTok}[1]{\textcolor[rgb]{0.31,0.60,0.02}{#1}}
\newcommand{\StringTok}[1]{\textcolor[rgb]{0.31,0.60,0.02}{#1}}
\newcommand{\VariableTok}[1]{\textcolor[rgb]{0.00,0.00,0.00}{#1}}
\newcommand{\VerbatimStringTok}[1]{\textcolor[rgb]{0.31,0.60,0.02}{#1}}
\newcommand{\WarningTok}[1]{\textcolor[rgb]{0.56,0.35,0.01}{\textbf{\textit{#1}}}}

%% ── Code listings ───────────────────────────────────────────────────────
\usepackage{listings}
\lstset{
  basicstyle=\small\ttfamily,
  breaklines=true,
  breakatwhitespace=true,
  frame=single,
  rulecolor=\color{calloutborder},
  backgroundcolor=\color{codebg},
  xleftmargin=6pt, xrightmargin=6pt,
  aboveskip=8pt, belowskip=8pt,
  columns=flexible,
}

%% ── Custom boxes ────────────────────────────────────────────────────────
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable}

%% Chapter-top metadata bar
\newcommand{\chapterheader}[2]{%
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=calloutbg, colframe=calloutborder,
    leftrule=4pt, toprule=0.4pt, bottomrule=0.4pt, rightrule=0.4pt,
    arc=4pt, left=8pt, right=8pt, top=6pt, bottom=6pt,
  ]
    \textbf{Session:}\enspace #1\quad\textbar\quad
    \textbf{Key question:}\enspace\textit{#2}
  \end{tcolorbox}%
  \medskip
}

%% Generic callout  \begin{callout}{Label} ... \end{callout}
\newenvironment{callout}[1]{%
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=calloutbg, colframe=calloutborder,
    leftrule=4pt, toprule=0.4pt, bottomrule=0.4pt, rightrule=0.4pt,
    arc=4pt, left=8pt, right=8pt, top=6pt, bottom=6pt,
    title={\small\bfseries\color{brandblue}#1},
    attach boxed title to top left={yshift=-2mm, xshift=8mm},
    boxed title style={colback=calloutbg, colframe=calloutborder,
                       arc=3pt, left=3pt, right=3pt},
  ]
}{%
  \end{tcolorbox}%
  \medskip
}

%% Weak / bad example  \begin{examplebad}{label} ... \end{examplebad}
\newenvironment{examplebad}[1]{%
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=badbg, colframe=badred,
    leftrule=4pt, toprule=0.4pt, bottomrule=0.4pt, rightrule=0.4pt,
    arc=4pt, left=8pt, right=8pt, top=6pt, bottom=6pt,
    title={\small\bfseries\color{badred}\MakeUppercase{#1}},
    attach boxed title to top left={yshift=-2mm, xshift=8mm},
    boxed title style={colback=badbg, colframe=badred,
                       arc=3pt, left=3pt, right=3pt},
  ]
  \ttfamily\small
  \setlength{\parskip}{0.45\baselineskip}%
}{%
  \end{tcolorbox}%
  \medskip
}

%% Strong / good example  \begin{examplegood}{label} ... \end{examplegood}
\newenvironment{examplegood}[1]{%
  \begin{tcolorbox}[
    enhanced, breakable,
    colback=goodbg, colframe=goodgreen,
    leftrule=4pt, toprule=0.4pt, bottomrule=0.4pt, rightrule=0.4pt,
    arc=4pt, left=8pt, right=8pt, top=6pt, bottom=6pt,
    title={\small\bfseries\color{goodgreen}\MakeUppercase{#1}},
    attach boxed title to top left={yshift=-2mm, xshift=8mm},
    boxed title style={colback=goodbg, colframe=goodgreen,
                       arc=3pt, left=3pt, right=3pt},
  ]
  \ttfamily\small
  \setlength{\parskip}{0.45\baselineskip}%
}{%
  \end{tcolorbox}%
  \medskip
}

%% Placeholder text inside example boxes
\newcommand{\placeholder}[1]{%
  {\normalfont\small\color{brandblue}[#1]}%
}

%% ── Chapter & section formatting ────────────────────────────────────────
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\LARGE\bfseries\color{brandblue}}
  {\chaptertitlename\ \thechapter}{10pt}{\Huge}[\vspace{4pt}\color{calloutborder}\hrule]
\titlespacing*{\chapter}{0pt}{-10pt}{24pt}

\titleformat{\section}
  {\normalfont\large\bfseries\color{brandblue}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\normalsize\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\itshape}{\thesubsubsection}{1em}{}

%% ── Appendix ────────────────────────────────────────────────────────────
\usepackage[toc,page]{appendix}

%% ── Draft watermark ─────────────────────────────────────────────────────
\usepackage[firstpage=false]{draftwatermark}
\SetWatermarkText{DRAFT}
\SetWatermarkScale{1.2}
\SetWatermarkColor[gray]{0.88}

%% ── Hyperlinks ──────────────────────────────────────────────────────────
\usepackage[
  hidelinks,
  pdftitle={Prompt with Precision},
  pdfauthor={Benjamin C. Varghese},
  pdfsubject={CC BY-SA 4.0},
  bookmarksnumbered,
]{hyperref}

%% ── Pandoc compatibility shims ──────────────────────────────────────────
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
"""


# ── Master document template ──────────────────────────────────────────────
_MASTER_TEMPLATE = r"""{preamble}
\begin{{document}}

%% ── Title page ──────────────────────────────────────────────────────────
\begin{{titlepage}}
  \centering
  \vspace*{{4cm}}
  {{\Huge\bfseries\color{{brandblue}} Prompt with Precision}}\\[0.7em]
  {{\Large A Practitioner's Guide to AI Prompting\\[0.3em] for Bible Translation}}\\[2.5em]
  {{\normalsize AI Tools Track --- Prompt Engineering Module}}\\[0.3em]
  {{\normalsize AILT Workshop \textperiodcentered\ March 2026}}\\[1.5em]
  {{\normalsize\textbf{{Author:}} Benjamin C. Varghese}}\\[0.4em]
  {{\normalsize\textit{{Release v0.1-beta}}}}
  \vfill
  \noindent\rule{{\textwidth}}{{0.4pt}}
  \vspace{{6pt}}\\
  {{\small \textcopyright\ 2026 Benjamin C. Varghese \textbar\ Licensed under CC~BY-SA~4.0}}\\[2pt]
  {{\small All examples use Mark~5:1--20 as the shared through-line passage.}}
\end{{titlepage}}

\frontmatter
\tableofcontents
\clearpage

%% ── Preface / Front matter ───────────────────────────────────────────────
\input{{tex/ch00-frontmatter.tex}}

\mainmatter

%% ── Chapters ────────────────────────────────────────────────────────────
{chapter_inputs}

%% ── Appendices ──────────────────────────────────────────────────────────
\appendix
\appendixpage

{appendix_inputs}

\end{{document}}
"""


# ── Main ──────────────────────────────────────────────────────────────────
def build() -> None:
    check_pandoc()
    TEX_DIR.mkdir(parents=True, exist_ok=True)

    for name in ALL_FILES:
        md_path  = HANDBOOK_DIR / name
        stem     = md_path.stem
        tex_path = TEX_DIR / f"{stem}.tex"
        print(f"  {name}  →  tex/{stem}.tex")
        md_text  = md_path.read_text(encoding="utf-8")
        raw_tex  = md_to_tex(md_text, name)
        final    = postprocess(raw_tex, stem)
        tex_path.write_text(final, encoding="utf-8")

    # Assemble master document
    chapter_inputs  = "\n".join(
        f"\\input{{tex/{Path(f).stem}.tex}}"
        for f in CHAPTERS[1:]           # ch00 is already in frontmatter section
    )
    appendix_inputs = "\n".join(
        f"\\input{{tex/{Path(f).stem}.tex}}"
        for f in APPENDICES
    )
    master = _MASTER_TEMPLATE.format(
        preamble=PREAMBLE,
        chapter_inputs=chapter_inputs,
        appendix_inputs=appendix_inputs,
    )
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    master_path = OUT_DIR / "handbook.tex"
    master_path.write_text(master, encoding="utf-8")

    print(f"\nDone.")
    print(f"  Fragments  →  output/tex/   ({len(ALL_FILES)} files)")
    print(f"  Master doc →  output/handbook.tex")
    print(f"\nTo compile (run twice for ToC):")
    print(f"  cd output")
    print(f"  xelatex handbook.tex")
    print(f"  xelatex handbook.tex")


if __name__ == "__main__":
    build()
