from __future__ import annotations

import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK_DIR = ROOT / "handbook"
OUT_HTML = ROOT / "output" / "handbook.html"

# Canonical reading order.
FILES = [
    "ch00-frontmatter.md",
    "ch01-how-llms-work.md",
    "ch02-anatomy-of-a-prompt.md",
    "ch03-master-formula.md",
    "ch04-advanced-techniques.md",
    "ch05-prompting-by-lane.md",
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


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text or "section"


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def mark_example_labels(md_text: str) -> str:
    # Convert label paragraphs into explicit marker tags before Markdown conversion.
    # This allows consistent styling of Weak/Strong examples across chapters.
    label_map = {
        "**Weak prompt:**": '<p class="example-label example-bad-label">Weak prompt</p>',
        "**Strong prompt:**": '<p class="example-label example-good-label">Strong prompt</p>',
        "**Stronger prompt:**": '<p class="example-label example-good-label">Stronger prompt</p>',
        "**Strong prompt (using CoT):**": '<p class="example-label example-good-label">Strong prompt (using CoT)</p>',
        "**Meta-generated prompt (typical output):**": '<p class="example-label example-good-label">Meta-generated prompt</p>',
    }

    out_lines: list[str] = []
    for line in md_text.splitlines():
        stripped = line.strip()
        if stripped in label_map:
            out_lines.append(label_map[stripped])
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


def style_examples(html: str) -> str:
    # Wrap label + following blockquote into example cards.
    pattern = re.compile(
        r'<p class="example-label (?P<labelclass>example-(?:bad|good)-label)">(?P<label>.*?)</p>\s*<blockquote>(?P<quote>.*?)</blockquote>',
        re.DOTALL,
    )

    def repl(match: re.Match[str]) -> str:
        labelclass = match.group("labelclass")
        kind = "example-bad" if "bad" in labelclass else "example-good"
        label = match.group("label")
        quote = match.group("quote")
        # Style [placeholder text] inside prompts
        quote = re.sub(r'\[([^\]<\n]+)\](?!\()', r'<span class="placeholder">[\1]</span>', quote)
        return (
            f'<section class="example {kind}">'
            f'<div class="example-head">{label}</div>'
            f'<blockquote>{quote}</blockquote>'
            "</section>"
        )

    return pattern.sub(repl, html)


def build() -> None:
    md_engine = markdown.Markdown(
        extensions=[
            "extra",          # tables, fenced code, etc.
            "admonition",
            "sane_lists",
            "toc",
        ],
        extension_configs={
            "toc": {"permalink": False},
        },
        output_format="html5",
    )

    sections: list[str] = []
    toc_entries: list[str] = []

    for idx, name in enumerate(FILES, start=1):
        md_path = HANDBOOK_DIR / name
        md_text = md_path.read_text(encoding="utf-8")
        title = extract_title(md_text, name)
        anchor = f"sec-{idx:02d}-{slugify(title)}"

        prepped_md = mark_example_labels(md_text)
        html_body = md_engine.convert(prepped_md)
        md_engine.reset()

        html_body = style_examples(html_body)

        toc_entries.append(f'<li><a href="#{anchor}">{title}</a></li>')
        sections.append(
            "\n".join(
                [
                    f'<section id="{anchor}" class="chapter">',
                    f'<div class="chapter-meta">{name}</div>',
                    html_body,
                    "</section>",
                ]
            )
        )

    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Prompt with Precision - Handbook</title>
  <style>
    :root {{
      --bg: #f4f6f8;
      --paper: #ffffff;
      --ink: #1f2a36;
      --muted: #5f6f82;
      --brand: #0f5d79;
      --brand-soft: #e6f2f7;
      --line: #d8e0e8;
      --good: #1e7f54;
      --good-bg: #e9f7ef;
      --bad: #a74b28;
      --bad-bg: #fdf0ea;
      --code-bg: #f5f8fb;
      --shadow: 0 12px 30px rgba(20, 40, 60, 0.08);
    }}

    html, body {{
      margin: 0;
      padding: 0;
      background: radial-gradient(circle at top left, #eef5f8 0, #f8f9fb 45%, #eef1f5 100%);
      color: var(--ink);
      font-family: "Segoe UI", "Arial", sans-serif;
      line-height: 1.58;
    }}

    .layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 22px;
      max-width: 1500px;
      margin: 0 auto;
      padding: 22px;
      box-sizing: border-box;
    }}

    nav.toc {{
      position: sticky;
      top: 16px;
      align-self: start;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 14px;
      box-shadow: var(--shadow);
      padding: 16px 14px;
      max-height: calc(100vh - 44px);
      overflow: auto;
    }}

    .toc h2 {{
      margin: 0 0 8px;
      font-size: 1rem;
      letter-spacing: .04em;
      text-transform: uppercase;
      color: var(--brand);
    }}

    .toc ol {{
      margin: 0;
      padding-left: 18px;
    }}

    .toc li {{
      margin: 6px 0;
    }}

    .toc a {{
      color: var(--ink);
      text-decoration: none;
      font-size: .92rem;
    }}

    .toc a:hover {{
      color: var(--brand);
      text-decoration: underline;
    }}

    main.book {{
      min-width: 0;
    }}

    .book-header {{
      background: linear-gradient(125deg, #0d5f7e 0%, #2f7d95 45%, #5e9daf 100%);
      color: #fff;
      border-radius: 16px;
      padding: 26px 28px;
      box-shadow: var(--shadow);
      margin-bottom: 18px;
    }}

    .book-header h1 {{
      margin: 0;
      font-size: clamp(1.7rem, 2.8vw, 2.4rem);
      line-height: 1.2;
      font-family: "Georgia", "Times New Roman", serif;
    }}

    .book-header p {{
      margin: 6px 0 0;
      opacity: .95;
    }}

    .book-meta {{
      font-size: .85rem;
      opacity: .80;
      margin-top: 10px !important;
    }}

    .chapter {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 14px;
      box-shadow: var(--shadow);
      margin-bottom: 18px;
      padding: 28px 30px;
      overflow-wrap: anywhere;
    }}

    .chapter-meta {{
      display: inline-block;
      margin-bottom: 8px;
      font-size: .76rem;
      text-transform: uppercase;
      letter-spacing: .07em;
      color: var(--muted);
      background: #f1f5f8;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 4px 10px;
    }}

    h1, h2, h3, h4 {{
      color: #12384b;
      margin-top: 1.15em;
      margin-bottom: .45em;
      line-height: 1.28;
      font-family: "Georgia", "Times New Roman", serif;
    }}

    h1 {{ font-size: 1.85rem; }}
    h2 {{ font-size: 1.35rem; border-bottom: 1px solid var(--line); padding-bottom: .28em; }}
    h3 {{ font-size: 1.1rem; }}

    p, li {{ font-size: 1rem; }}

    a {{ color: #0d607f; }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0 18px;
      font-size: .95rem;
    }}

    th, td {{
      border: 1px solid var(--line);
      padding: 9px 10px;
      text-align: left;
      vertical-align: top;
    }}

    th {{
      background: var(--brand-soft);
      color: #133b4d;
      font-weight: 700;
    }}

    blockquote {{
      margin: 14px 0;
      padding: 10px 14px;
      border-left: 4px solid #7aa6bf;
      background: #f7fbfe;
      color: #294357;
    }}

    code {{
      background: var(--code-bg);
      border: 1px solid #dce7ef;
      padding: 1px 5px;
      border-radius: 5px;
      font-size: .9em;
      font-family: "Consolas", "Courier New", monospace;
    }}

    pre {{
      background: #f3f7fa;
      border: 1px solid #d8e5ee;
      border-radius: 8px;
      padding: 13px;
      overflow: auto;
    }}

    pre code {{
      border: 0;
      background: transparent;
      padding: 0;
    }}

    .example {{
      border-radius: 10px;
      border: 1px solid;
      margin: 16px 0;
      overflow: hidden;
    }}

    .example-head {{
      font-weight: 700;
      font-size: .9rem;
      letter-spacing: .02em;
      padding: 8px 12px;
      text-transform: uppercase;
    }}

    .example blockquote {{
      margin: 0;
      border-left: 0;
      padding: 12px 14px;
    }}

    .example blockquote p {{
      margin: 0 0 0.6em;
    }}

    .example blockquote p:last-child {{
      margin-bottom: 0;
    }}

    .placeholder {{
      color: #0f5d79;
      background: #daeef5;
      border-radius: 3px;
      padding: 1px 5px;
      font-style: normal;
    }}

    .example-bad {{
      border-color: #ebc7b5;
      background: var(--bad-bg);
    }}
    .example-bad .example-head {{
      background: #f6ddd1;
      color: var(--bad);
    }}

    .example-good {{
      border-color: #b6dfca;
      background: var(--good-bg);
    }}
    .example-good .example-head {{
      background: #d8efe2;
      color: var(--good);
    }}

    @media (max-width: 1050px) {{
      .layout {{
        grid-template-columns: 1fr;
      }}
      nav.toc {{
        position: static;
        max-height: none;
      }}
    }}

    @media print {{
      body {{ background: #fff; }}
      .layout {{ display: block; padding: 0; max-width: none; }}
      nav.toc {{ display: none; }}
      .book-header, .chapter {{ box-shadow: none; border-radius: 0; border: 0; }}
      .chapter {{ page-break-inside: avoid; margin: 0 0 12mm; padding: 0; }}
      @page {{ size: A4; margin: 15mm 14mm 16mm; }}
    }}
  </style>
</head>
<body>
  <div class=\"layout\">
    <nav class=\"toc\">
      <h2>Contents</h2>
      <ol>
        {''.join(toc_entries)}
      </ol>
    </nav>
    <main class=\"book\">
      <header class=\"book-header\">
        <h1>Prompt with Precision</h1>
        <p>A Practitioner's Guide to AI Prompting for Bible Translation</p>        <p class="book-meta">Benjamin C. Varghese &nbsp;&middot;&nbsp; Release v0.1-beta &nbsp;&middot;&nbsp; <a href="https://creativecommons.org/licenses/by-sa/4.0/" style="color:#cce8f0">CC BY-SA 4.0</a></p>      </header>
      {''.join(sections)}
    </main>
  </div>
</body>
</html>
"""

    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML}")


if __name__ == "__main__":
    build()
