#!/usr/bin/env python3
"""
build_modules.py — Build presentation and handout artifacts for each module.

For each module folder under modules/ that contains a slides.html fragment,
this script:
  1. Wraps slides.html in the full Reveal.js scaffold -> presentation.html
  2. Compiles handout-facilitator.tex -> handout-facilitator.pdf (via XeLaTeX)
  3. Compiles handout-participant.tex -> handout-participant.pdf (via XeLaTeX)

Usage:
    python scripts/build_modules.py              # build all modules
    python scripts/build_modules.py hb-ch01      # build modules starting with prefix
    python scripts/build_modules.py --status     # show build status table

Asset files (scripts/assets/):
    presentation.css      -- shared CSS for all presentations
    template.html         -- Reveal.js scaffold; placeholders: __TITLE__ __TAGLINE__
                             __CSS__ __SLIDES__ __REVEAL_CDN__
    handout-preamble.tex  -- LaTeX preamble prepended to every handout body

Timings (timings.txt per module):
    slide-<key>: <minutes>   # <key> matches __TIMER_<key>__ token in slides.html
    Slides without an explicit entry use `default-slide: N` from meta.txt.
    Sub-slides in vertical stacks should NOT have __TIMER__ tokens.

Requires:
    - xelatex on PATH (MiKTeX or TeX Live)
    - No Python dependencies beyond the stdlib
"""
from __future__ import annotations

import datetime
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# -- Paths ------------------------------------------------------------------
ROOT        = Path(__file__).resolve().parents[1]
MODULES_DIR = ROOT / "modules"

# -- Reveal.js CDN (4.3.1 via cdnjs) ---------------------------------------
REVEAL_CDN = "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1"

# -- Asset files (all in scripts/assets/) -----------------------------------
CSS_FILE      = ROOT / "scripts" / "assets" / "presentation.css"
TEMPLATE_FILE = ROOT / "scripts" / "assets" / "template.html"
PREAMBLE_FILE = ROOT / "scripts" / "assets" / "handout-preamble.tex"


# -- XeLaTeX compilation helper ---------------------------------------------

def check_xelatex() -> bool:
    return shutil.which("xelatex") is not None


def compile_tex(tex_source: str, out_pdf: Path) -> bool:
    """Write tex_source to a temp dir, compile twice with xelatex, copy PDF out.
    Returns True on success."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        tex_file = tmp_path / "handout.tex"
        tex_file.write_text(tex_source, encoding="utf-8")

        cmd = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "handout.tex"]
        for _ in range(2):                      # two passes for headers/refs
            result = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True,
                                    encoding="utf-8", errors="replace")
            if result.returncode != 0:
                print("    [xelatex error] see log:")
                log_file = tmp_path / "handout.log"
                if log_file.exists():
                    lines = log_file.read_text(encoding="utf-8", errors="replace").splitlines()
                    print("\n".join(lines[-20:]))
                return False

        pdf_file = tmp_path / "handout.pdf"
        if pdf_file.exists():
            shutil.copy2(pdf_file, out_pdf)
            return True
        return False


# -- Per-module builder -----------------------------------------------------

def read_timings(module_dir: Path) -> dict:
    """Parse timings.txt -> {slide_key: minutes_string}.

    Key is the string after 'slide-', e.g.:
        slide-key-terms: 5   ->  {'key-terms': '5'}
        slide-2:         5   ->  {'2': '5'}   (old numeric style, still works)
    Blank lines and comment-only lines are ignored.
    """
    timings_file = module_dir / "timings.txt"
    if not timings_file.exists():
        return {}
    timings: dict = {}
    for line in timings_file.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key.startswith("slide-"):
            timings[key[6:]] = val          # string key — no int() conversion
    return timings


def build_presentation(module_dir: Path) -> None:
    slides_file = module_dir / "slides.html"
    if not slides_file.exists():
        return

    for asset, label in [(CSS_FILE, "CSS file"), (TEMPLATE_FILE, "HTML template")]:
        if not asset.exists():
            print(f"  ERROR: {label} not found: {asset}")
            return

    # -- Read meta.txt -------------------------------------------------------
    meta_file     = module_dir / "meta.txt"
    title         = "AI Tools Workshop AILT 2026"
    tag_line      = ""
    duration      = 0
    default_slide = 0
    if meta_file.exists():
        for line in meta_file.read_text(encoding="utf-8").splitlines():
            if   line.startswith("title:"):         title         = line[6:].strip()
            elif line.startswith("tagline:"):        tag_line      = line[8:].strip()
            elif line.startswith("duration:"):
                try:    duration      = int(line[9:].strip())
                except ValueError: pass
            elif line.startswith("default-slide:"):
                try:    default_slide = int(line[14:].strip())
                except ValueError: pass

    # -- Timer injection -----------------------------------------------------
    # Finds every __TIMER_<key>__ token in slides.html.
    # Substitutes from timings.txt; falls back to default-slide if set.
    timings        = read_timings(module_dir)
    slides_content = slides_file.read_text(encoding="utf-8")
    token_keys     = re.findall(r'__TIMER_([\w-]+)__', slides_content)
    substituted_total = 0
    for key in token_keys:
        minutes_str = timings.get(key) or (str(default_slide) if default_slide else None)
        if minutes_str:
            slides_content = slides_content.replace(
                f"__TIMER_{key}__", f"~ {minutes_str} min"
            )
            try:    substituted_total += int(minutes_str)
            except ValueError: pass

    if (timings or default_slide) and duration:
        ok     = (substituted_total == duration)
        status = "\u2713" if ok else "\u26a0 "
        extra  = "" if ok else f"  <- expected {duration} min -- adjust timings.txt then re-run"
        print(f"    {status} timing: {substituted_total} min / {duration} min session{extra}")

    # -- Validation checks ---------------------------------------------------
    # 1. Unresolved timer tokens
    leftover = re.findall(r'__TIMER_[\w-]+__', slides_content)
    if leftover:
        print(f"    \u26a0  unresolved timer tokens: {leftover}")

    # 2. Missing image assets
    for asset in re.findall(r'src="\.\./assets/([^"]+)"', slides_content):
        if not (module_dir / "assets" / asset).exists():
            print(f"    \u26a0  missing asset: assets/{asset}")

    # 3. Unclosed <section> tags
    opens  = slides_content.count("<section")
    closes = slides_content.count("</section")
    if opens != closes:
        print(f"    \u26a0  section tag mismatch: {opens} <section> vs {closes} </section>")

    # -- Render and write ----------------------------------------------------
    css      = CSS_FILE.read_text(encoding="utf-8")
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    html = (template
            .replace("__TITLE__",      title)
            .replace("__TAGLINE__",    tag_line)
            .replace("__CSS__",        css)
            .replace("__SLIDES__",     slides_content)
            .replace("__REVEAL_CDN__", REVEAL_CDN))

    out_dir = module_dir / "output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "presentation.html").write_text(html, encoding="utf-8")
    print(f"    \u2713  output/presentation.html")


def build_handout(module_dir: Path, kind: str) -> None:
    """kind is 'facilitator' or 'participant'"""
    tex_source_file = module_dir / f"handout-{kind}.tex"
    if not tex_source_file.exists():
        return

    if not PREAMBLE_FILE.exists():
        print(f"  ERROR: LaTeX preamble not found: {PREAMBLE_FILE}")
        return

    body     = tex_source_file.read_text(encoding="utf-8")
    preamble = PREAMBLE_FILE.read_text(encoding="utf-8")
    full_tex = preamble + "\n\\begin{document}\n\n" + body + "\n\\end{document}\n"

    out_dir = module_dir / "output"
    out_dir.mkdir(exist_ok=True)
    out_pdf = out_dir / f"handout-{kind}.pdf"
    print(f"    compiling output/handout-{kind}.pdf ...")
    ok = compile_tex(full_tex, out_pdf)
    if ok:
        print(f"    \u2713  output/handout-{kind}.pdf")
    else:
        print(f"    \u2717  output/handout-{kind}.pdf -- compilation failed (see log above)")


def build_module(module_dir: Path) -> None:
    print(f"\n  [{module_dir.name}]")
    build_presentation(module_dir)
    build_handout(module_dir, "facilitator")
    build_handout(module_dir, "participant")


# -- Status display ---------------------------------------------------------

def print_status(candidates: list) -> None:
    print(f"\n  {'Module':<36} {'Built':^6} {'Duration':^10} Last built")
    print("  " + "-" * 65)
    for module_dir in candidates:
        duration  = "--"
        meta_file = module_dir / "meta.txt"
        if meta_file.exists():
            for line in meta_file.read_text(encoding="utf-8").splitlines():
                if line.startswith("duration:"):
                    duration = line[9:].strip() + " min"
        out = module_dir / "output" / "presentation.html"
        if out.exists():
            mtime = datetime.datetime.fromtimestamp(
                out.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
            built = "\u2713"
        else:
            mtime, built = "never", "\u2717"
        print(f"  {module_dir.name:<36} {built:^6} {duration:^10} {mtime}")
    print()


# -- Entry point ------------------------------------------------------------

def main() -> None:
    if not MODULES_DIR.exists():
        print(f"ERROR: modules directory not found at {MODULES_DIR}")
        sys.exit(1)

    filter_prefix = sys.argv[1] if len(sys.argv) > 1 else None
    candidates    = sorted(p for p in MODULES_DIR.iterdir() if p.is_dir())

    if filter_prefix == "--status":
        print_status(candidates)
        sys.exit(0)

    if filter_prefix:
        candidates = [p for p in candidates if p.name.startswith(filter_prefix)]

    if not check_xelatex():
        print("WARNING: xelatex not found on PATH -- handout PDFs will be skipped.")

    if not candidates:
        print("No matching module folders found.")
        sys.exit(0)

    print(f"Building {len(candidates)} module(s) ...")
    for module_dir in candidates:
        build_module(module_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()
