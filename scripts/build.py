#!/usr/bin/env python3
"""
build.py — AILT 2026 Prompt Engineering for Bible Translators
Single build entry point for the GitHub Pages release site.

Usage:
    python scripts/build.py          # incremental build (skip unchanged files)
    python scripts/build.py --force  # rebuild everything
    python scripts/build.py --clean-only  # delete docs/ only

Output: docs/  (configured as GitHub Pages source)
"""

import sys
import os
import re
import shutil
import subprocess
from pathlib import Path

# ─── PATH SETUP ──────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
ROOT       = SCRIPT_DIR.parent

sys.path.insert(0, str(SCRIPT_DIR))
from lib import md_to_html, inject

# ─── DIRECTORIES ─────────────────────────────────────────────────────────────

DOCS          = ROOT / 'docs'
TRACKS_DIR    = ROOT / 'tracks' / 'ai-tools'
HANDBOOK_SRC  = TRACKS_DIR / 'shared' / 'handbook'
MODULES_SRC   = TRACKS_DIR / 'modules'
ASSETS_SRC    = SCRIPT_DIR / 'assets-src'
TEMPLATES_DIR = SCRIPT_DIR / 'templates'

DOCS_ASSETS = DOCS / 'assets'
DOCS_HB     = DOCS / 'handbook'
DOCS_PE     = DOCS / 'prompt-engineering'
DOCS_006    = DOCS / 'use-prompts-scripture'

# ─── HANDBOOK FILE MAP ────────────────────────────────────────────────────────
# (source_filename, output_filename, section_label_for_index)

HANDBOOK_CHAPTERS = [
    ('01-how-llms-work.md',          'ch01.html',              'Chapter 1', 'How LLMs Work — and Why It Matters for Prompting'),
    ('02-anatomy-of-a-prompt.md',    'ch02.html',              'Chapter 2', 'Anatomy of a Great Prompt'),
    ('03-master-formula.md',         'ch03.html',              'Chapter 3', 'The Master Formula'),
    ('04-advanced-techniques.md',    'ch04.html',              'Chapter 4', 'Advanced Techniques'),
    ('05-prompting-by-lane.md',      'ch05.html',              'Chapter 5', 'Prompting by Lane'),
]
HANDBOOK_FRONTMATTER = ('ch00-frontmatter.md', 'ch00-frontmatter.html')
HANDBOOK_APPENDICES = [
    ('app-a-glossary.md',           'app-a.html',  'Appendix A', 'Glossary'),
    ('app-b-risk-reference.md',     'app-b.html',  'Appendix B', 'Risk Reference'),
    ('app-c-lane-reference.md',     'app-c.html',  'Appendix C', 'Lane Reference'),
    ('app-d-prompt-templates.md',   'app-d.html',  'Appendix D', 'Prompt Templates'),
    ('app-e-meta-prompting.md',     'app-e.html',  'Appendix E', 'Meta-Prompting'),
    ('app-f-attention-paper.md',    'app-f.html',  'Appendix F', 'The Attention Paper'),
    ('app-g-beyond-basics.md',      'app-g.html',  'Appendix G', 'Beyond the Basics'),
    ('app-h-minority-languages.md', 'app-h.html',  'Appendix H', 'Minority Languages'),
    ('app-i-how-this-was-made.md',  'app-i.html',  'Appendix I', 'How This Was Made'),
]

# Prompt Engineering module source -> published filename
MODULE_004_FILES = [
    ('source/legacy/index.html', 'index.html'),
    ('sessions/01-how-llms-work.html', 'ch01.html'),
    ('sessions/02-anatomy-of-a-prompt.html', 'ch02.html'),
    ('sessions/03-master-formula.html', 'ch03.html'),
    ('sessions/04-advanced-techniques.html', 'ch04.html'),
    ('sessions/05-prompting-by-lane.html', 'ch05.html'),
]

# ─── HELPERS ─────────────────────────────────────────────────────────────────

FORCE = '--force' in sys.argv

def _log(msg: str):
    print(msg)

def _is_stale(src: Path, out: Path, *extra_deps: Path) -> bool:
    """Return True if out does not exist or src (or any dep) is newer than out."""
    if FORCE or not out.exists():
        return True
    out_mtime = out.stat().st_mtime
    for dep in (src, *extra_deps):
        if dep.exists() and dep.stat().st_mtime > out_mtime:
            return True
    return False

def _read(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def _write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    _log(f'  wrote  {path.relative_to(ROOT)}')

def _skip(path: Path):
    _log(f'  skip   {path.relative_to(ROOT)} (up to date)')

# ─── SHELL TEMPLATE ───────────────────────────────────────────────────────────

SHELL_TMPL = _read(TEMPLATES_DIR / 'shell.html')

# ─── PROCESSING PIPELINE ─────────────────────────────────────────────────────

def process_handbook_page(src: Path, out: Path, title: str, assets: str, site_root: str):
    """Convert a handbook Markdown file → full HTML page."""
    if not _is_stale(src, out, TEMPLATES_DIR / 'shell.html'):
        _skip(out); return

    md_text  = _read(src)
    raw_html = md_to_html.convert(md_text)

    if not title:
        title = md_to_html.extract_title(md_text) or src.stem

    # Add heading IDs (keeps anchor links working)
    raw_html  = inject.ensure_heading_ids(raw_html)

    # Wrap in prose container
    content = inject.wrap_prose(raw_html)

    page = inject.apply_shell(content, '', title, assets, site_root, SHELL_TMPL)
    _write(out, page)


def process_004_page(src: Path, out: Path, title: str, assets: str, site_root: str):
    """Process a 004 module HTML page → full site page."""
    if not _is_stale(src, out, TEMPLATES_DIR / 'shell.html'):
        _skip(out); return

    html = _read(src)
    body = inject.extract_body(html)

    # Remove inline <script> tags (shell provides the shared script)
    body = re.sub(r'<script\b[^>]*>.*?</script>', '', body, flags=re.DOTALL | re.IGNORECASE)

    # Add heading IDs
    body = inject.ensure_heading_ids(body)

    page = inject.apply_shell(body, '', title, assets, site_root, SHELL_TMPL)
    _write(out, page)


def process_006_page(src: Path, out: Path, title: str, assets: str, site_root: str):
    """Process the 006 module HTML page → full site page (light theme)."""
    if not _is_stale(src, out, TEMPLATES_DIR / 'shell.html'):
        _skip(out); return

    html = _read(src)
    body = inject.extract_body(html)

    # Strip dark inline <style> — the shared CSS provides light-theme equivalents
    body = inject.strip_style_tags(body)

    # Remove inline <script> tags
    body = re.sub(r'<script\b[^>]*>.*?</script>', '', body, flags=re.DOTALL | re.IGNORECASE)

    # Remove stray <link> tags (font imports etc.)
    body = re.sub(r'<link\b[^>]*/>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'<link\b[^>]*>', '', body, flags=re.IGNORECASE)

    # Add heading IDs
    body = inject.ensure_heading_ids(body)

    page = inject.apply_shell(body, '', title, assets, site_root, SHELL_TMPL)
    _write(out, page)


def build_handbook_index(out: Path, assets: str, site_root: str):
    """Generate the handbook overview / table-of-contents page."""
    if not FORCE and out.exists():
        _skip(out); return

    lines = ['<div class="prose-content">']
    lines.append('<div class="handbook-hero"><div class="hh-inner">'
                 '<div class="hh-eyebrow">Course Handbook</div>'
                 '<h1>Course Contents</h1>'
                 '</div></div>')

    lines.append('<p>The appendices are part of the course package, not a separate shelf of extras. Use the chapters for the core flow and the appendices as companion tools during and after training.</p>')

    lines.append('<h2>Core Chapters</h2><ul>')
    for fname, hname, label, display_title in HANDBOOK_CHAPTERS:
        lines.append(f'<li><a href="{hname}">{label} — {display_title}</a></li>')
    lines.append('</ul>')

    lines.append('<h2>Course Appendices</h2><ul>')
    for fname, hname, label, display_title in HANDBOOK_APPENDICES:
        lines.append(f'<li><a href="{hname}">{label} — {display_title}</a></li>')
    lines.append('</ul>')

    # Also link frontmatter
    lines.append('<hr><p><a href="ch00-frontmatter.html">Frontmatter &amp; Introduction</a></p>')
    lines.append('</div>')

    content = '\n'.join(lines)
    toc     = ''  # index page is simple, no sidebar
    page    = inject.apply_shell(
        content, toc,
        'Handbook — Prompt Engineering for Bible Translators',
        assets, site_root, SHELL_TMPL
    )
    _write(out, page)


# ─── PHASE 0 — VALIDATE ──────────────────────────────────────────────────────

def phase_validate():
    _log('\nPhase 0: Validate')
    ok = True

    # Check key source directories
    for d in [TRACKS_DIR, HANDBOOK_SRC, MODULES_SRC, ASSETS_SRC, TEMPLATES_DIR]:
        if not d.is_dir():
            _log(f'  ERROR: missing directory {d.relative_to(ROOT)}')
            ok = False

    # Check key source files
    key_files = [
        TEMPLATES_DIR / 'shell.html',
        ASSETS_SRC / 'input.css',
        ASSETS_SRC / 'script.js',
        ASSETS_SRC / 'favicon.svg',
        TEMPLATES_DIR / 'landing.html',
        TEMPLATES_DIR / 'about.html',
    ]
    for f in key_files:
        if not f.is_file():
            _log(f'  ERROR: missing file {f.relative_to(ROOT)}')
            ok = False

    # Check handbook source files
    all_hb = (
        [HANDBOOK_FRONTMATTER] +
        [(f, h) for f, h, *_ in HANDBOOK_CHAPTERS] +
        [(f, h) for f, h, *_ in HANDBOOK_APPENDICES]
    )
    for fname, _ in all_hb:
        p = HANDBOOK_SRC / fname
        if not p.is_file():
            _log(f'  WARN: missing handbook source: {p.relative_to(ROOT)}')

    # Check 004 source files
    for rel_src, _ in MODULE_004_FILES:
        p = MODULES_SRC / 'prompt-engineering' / rel_src
        if not p.is_file():
            _log(f'  WARN: missing 004 source: {p.relative_to(ROOT)}')

    # Check 006
    p006 = MODULES_SRC / 'use-prompts-scripture' / 'sessions' / '01-using-prompts-to-understand-scripture.html'
    if not p006.is_file():
        _log(f'  WARN: missing 006 source: {p006.relative_to(ROOT)}')

    # Check tailwindcss binary
    tw = _find_tailwind()
    if tw is None:
        _log('  WARN: tailwindcss binary not found on PATH or project root.')
        _log('        CSS will NOT be compiled. Download tailwindcss-windows-x64.exe,')
        _log('        rename to tailwindcss.exe, and place in this folder or PATH.')
    else:
        _log(f'  OK: tailwindcss at {tw}')

    if not ok:
        _log('\nBuild aborted due to errors above.')
        sys.exit(1)
    _log('  Validation passed.')


def _find_tailwind() -> str | None:
    """Return path to tailwindcss binary, or None if not found."""
    # Check project root first
    for name in ('tailwindcss.exe', 'tailwindcss'):
        p = ROOT / name
        if p.is_file():
            return str(p)
    # Check PATH
    tw = shutil.which('tailwindcss') or shutil.which('tailwindcss.exe')
    return tw


# ─── PHASE 1 — CLEAN ─────────────────────────────────────────────────────────

def phase_clean():
    _log('\nPhase 1: Clean')

    if FORCE:
        # Full wipe on --force
        if DOCS.exists():
            git_dir = DOCS / '.git'
            if git_dir.exists():
                _log('  WARNING: .git found inside docs/ — skipping delete to avoid data loss.')
            else:
                shutil.rmtree(DOCS)
                _log(f'  deleted docs/')

    # Always ensure output directories exist
    for d in [DOCS, DOCS_ASSETS, DOCS_HB, DOCS_PE, DOCS_006]:
        d.mkdir(parents=True, exist_ok=True)

    nojekyll = DOCS / '.nojekyll'
    if not nojekyll.exists():
        nojekyll.write_text('')
        _log('  created docs/.nojekyll')

    if not FORCE:
        _log('  (incremental mode — existing docs/ files kept)')


# ─── PHASE 2 — HANDBOOK ──────────────────────────────────────────────────────

def phase_handbook():
    _log('\nPhase 2: Handbook')
    assets    = '../assets/'
    site_root = '../'

    # Frontmatter page
    src, out_name = HANDBOOK_FRONTMATTER
    src_path = HANDBOOK_SRC / src
    out_path = DOCS_HB / out_name
    if src_path.is_file():
        process_handbook_page(src_path, out_path, 'Frontmatter', assets, site_root)

    # Chapter pages
    for fname, hname, label, display_title in HANDBOOK_CHAPTERS:
        src_path = HANDBOOK_SRC / fname
        out_path = DOCS_HB / hname
        if src_path.is_file():
            process_handbook_page(src_path, out_path, f'{label} — {display_title}', assets, site_root)

    # Appendix pages
    for fname, hname, label, display_title in HANDBOOK_APPENDICES:
        src_path = HANDBOOK_SRC / fname
        out_path = DOCS_HB / hname
        if src_path.is_file():
            process_handbook_page(src_path, out_path, f'{label} — {display_title}', assets, site_root)

    # Handbook index
    build_handbook_index(DOCS_HB / 'index.html', assets, site_root)


# ─── PHASE 3 — MODULES ───────────────────────────────────────────────────────

def phase_modules():
    _log('\nPhase 3: Modules')
    assets    = '../assets/'
    site_root = '../'

    # 004 Prompt Engineering
    src_dir = MODULES_SRC / 'prompt-engineering'
    _log('  004 prompt-engineering:')
    for rel_src, out_name in MODULE_004_FILES:
        src = src_dir / rel_src
        out = DOCS_PE / out_name
        if not src.is_file():
            _log(f'    WARN: {rel_src} not found, skipping')
            continue
        # Derive a title from the filename as fallback
        title = _title_from_004_file(out_name)
        process_004_page(src, out, title, assets, site_root)

    # 006 Using Prompts to Understand Scripture
    _log('  006 use-prompts-scripture:')
    src_006 = MODULES_SRC / 'use-prompts-scripture' / 'sessions' / '01-using-prompts-to-understand-scripture.html'
    out_006 = DOCS_006 / 'index.html'
    if src_006.is_file():
        process_006_page(
            src_006, out_006,
            'Using Prompts to Understand Scripture',
            assets, site_root
        )
    else:
        _log('    WARN: 006/index.html not found, skipping')


def _title_from_004_file(fname: str) -> str:
    titles = {
        'index.html': 'Prompt Engineering · AILT 2026',
        'ch01.html':  'Ch 1 — How LLMs Work · Prompt Engineering',
        'ch02.html':  'Ch 2 — Anatomy of a Prompt · Prompt Engineering',
        'ch03.html':  'Ch 3 — The Master Formula · Prompt Engineering',
        'ch04.html':  'Ch 4 — Advanced Techniques · Prompt Engineering',
        'ch05.html':  'Ch 5 — Prompting by Lane · Prompt Engineering',
    }
    return titles.get(fname, 'Prompt Engineering · AILT 2026')


# ─── PHASE 4 — LANDING & STATIC PAGES ────────────────────────────────────────

def phase_landing():
    _log('\nPhase 4: Landing & static pages')

    landing_src = TEMPLATES_DIR / 'landing.html'
    landing_out = DOCS / 'index.html'
    if _is_stale(landing_src, landing_out):
        shutil.copy2(landing_src, landing_out)
        _log(f'  wrote  docs/index.html')
    else:
        _skip(landing_out)

    about_src = TEMPLATES_DIR / 'about.html'
    about_out = DOCS / 'about.html'
    if _is_stale(about_src, about_out):
        shutil.copy2(about_src, about_out)
        _log(f'  wrote  docs/about.html')
    else:
        _skip(about_out)


# ─── PHASE 5 — ASSETS ────────────────────────────────────────────────────────

def phase_assets():
    _log('\nPhase 5: Assets')

    # Copy favicon
    favicon_src = ASSETS_SRC / 'favicon.svg'
    favicon_out = DOCS_ASSETS / 'favicon.svg'
    if _is_stale(favicon_src, favicon_out):
        shutil.copy2(favicon_src, favicon_out)
        _log('  wrote  docs/assets/favicon.svg')
    else:
        _skip(favicon_out)

    # Copy shared script.js (our assets-src version which includes presentation mode)
    script_src = ASSETS_SRC / 'script.js'
    script_out = DOCS_ASSETS / 'script.js'
    if _is_stale(script_src, script_out):
        shutil.copy2(script_src, script_out)
        _log('  wrote  docs/assets/script.js')
    else:
        _skip(script_out)

    # Compile Tailwind CSS
    css_src = ASSETS_SRC / 'input.css'
    css_out = DOCS_ASSETS / 'style.css'
    tw = _find_tailwind()

    if tw is None:
        _log('  WARN: tailwindcss not found — CSS not compiled.')
        _log('        Install tailwindcss.exe and re-run, or run manually:')
        _log('        tailwindcss -i scripts/assets-src/input.css -o docs/assets/style.css --minify')
        # Copy input.css as-is as fallback (without Tailwind base)
        if _is_stale(css_src, css_out):
            _log('  Copying input.css as-is (Tailwind directives will not be compiled)')
            _strip_tailwind_directives(css_src, css_out)
    else:
        # Check if CSS is stale (compare against all doc HTML for accuracy)
        if FORCE or not css_out.exists() or css_src.stat().st_mtime > css_out.stat().st_mtime:
            _log(f'  Compiling CSS with Tailwind...')
            cmd = [tw, '-i', str(css_src), '-o', str(css_out), '--minify']
            result = subprocess.run(
                cmd, cwd=str(ROOT), capture_output=True, text=True
            )
            if result.returncode != 0:
                _log(f'  ERROR running tailwindcss:\n{result.stderr}')
                _log('  Falling back to direct CSS copy (no Tailwind compilation)')
                _strip_tailwind_directives(css_src, css_out)
            else:
                _log('  wrote  docs/assets/style.css (Tailwind compiled)')
        else:
            _skip(css_out)


def _strip_tailwind_directives(src: Path, out: Path):
    """Copy CSS, removing Tailwind directives (fallback when Tailwind binary not available)."""
    css = src.read_text(encoding='utf-8')
    # v3 directives
    css = re.sub(r'@tailwind\s+\w+\s*;?\s*\n?', '', css)
    # v4 import
    css = re.sub(r'@import\s+"tailwindcss"\s*;?\s*\n?', '', css)
    out.write_text(css, encoding='utf-8')
    _log(f'  wrote  docs/assets/style.css (no Tailwind base — install tailwindcss.exe for full build)')


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    if '--clean-only' in sys.argv:
        phase_clean()
        _log('\nClean complete.')
        return

    _log('=' * 60)
    _log('AILT 2026 · Prompt Engineering — Build')
    _log(f'Root: {ROOT}')
    _log(f'Mode: {"FORCE" if FORCE else "incremental"}')
    _log('=' * 60)

    phase_validate()
    phase_clean()
    phase_handbook()
    phase_modules()
    phase_landing()
    phase_assets()

    _log('\n' + '=' * 60)
    _log('Build complete.')
    _log(f'Output: {DOCS}')
    _log('Serve locally: python -m http.server 8000 --directory docs')
    _log('=' * 60)


if __name__ == '__main__':
    main()
