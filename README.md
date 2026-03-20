# Prompt Engineering for Bible Translators

Course material for the **AILT 2026 AI Tools Track** — *Prompt Engineering for Bible Translators*.  
Designed for translation consultants, mother-tongue translators, language technology staff, and  
project leadership attending the Africa Inland Leadership Training 2026 workshop.

---

## What is this?

A static website (GitHub Pages) containing:

- **AI Tools Handbook** — five chapters + nine appendices on LLMs and prompt engineering
- **Prompt Engineering course** — five interactive session pages with lane-differentiated content
- **Using Prompts to Understand Scripture** — a standalone practical session

---

## Quick start (rebuild the site)

**Requirements:**

```bash
pip install -r requirements.txt
```

Download the [Tailwind CSS standalone binary](https://github.com/tailwindlabs/tailwindcss/releases/latest)
(`tailwindcss-windows-x64.exe`) and rename it to `tailwindcss.exe`. Place it in this folder or anywhere on your `PATH`.

**Build:**

```bash
python scripts/build.py
```

Or with `make`:

```bash
make build        # normal build (skips unchanged files)
make force        # rebuild everything
make clean        # delete docs/ only
make serve        # serve docs/ locally at http://localhost:8000
```

**First-time GitHub Pages setup:**

```bash
git init
git add .
git commit -m "initial commit"
# create a public repo on GitHub, then:
git remote add origin https://github.com/<username>/prompt-engineering-bt-course.git
git push -u origin main
# GitHub repo → Settings → Pages → Source: main branch, /docs folder
```

---

## Repository layout

```
handbook/          ← source: Markdown chapters & appendices
modules/
  004-prompt-engineering/   ← handcrafted HTML module
  006-use-prompts-scripture/ ← handcrafted HTML module
scripts/
  build.py         ← single build entry point
  lib/             ← build library modules
  templates/       ← HTML shell & landing page templates
  assets-src/      ← CSS + JS source files
  design/          ← component reference (DESIGN.md)
docs/              ← BUILD OUTPUT → served by GitHub Pages
```

**What gets committed:** everything — source files, build scripts, and the `docs/` output.  
GitHub Pages serves only `docs/`; the full source is visible on GitHub (intentional).

---

## Dependencies

| Tool | Purpose | Install |
|---|---|---|
| Python ≥ 3.9 | Build orchestration | Pre-installed on most systems |
| `markdown` library | Markdown → HTML | `pip install markdown` |
| Tailwind CSS standalone binary | CSS compilation | Download binary (no npm needed) |

No Node.js. No npm. No bundlers.
