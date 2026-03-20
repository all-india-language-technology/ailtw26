# Design System Reference — Prompt Engineering for Bible Translators

**Tailwind version:** v4 (standalone binary)  
**CSS source:** `scripts/assets-src/input.css` → compiled to `docs/assets/style.css`  
**Script source:** `scripts/assets-src/script.js` → copied to `docs/assets/script.js`

---

## Colour Tokens

| Token | Value | Usage |
|---|---|---|
| `--navy` | `#1B2B5E` | Primary brand, nav background |
| `--navy-dim` | `#14203F` | Darker nav, hero gradients |
| `--navy-light` | `#243870` | Hover states |
| `--amber` | `#F4A020` | Brand accent, nav brand name, CTAs |
| `--amber-dim` | `#D98B0B` | Amber hover |
| `--c1` | `#ea580c` | Connection phase — orange |
| `--c2` | `#2563eb` | Content phase — blue |
| `--c3` | `#7c3aed` | Challenge phase — violet |
| `--c4` | `#059669` | Change phase — emerald |
| `--c5` | `#d97706` | Closure phase — amber |
| `--lane1` | `#0284c7` | Translator lane — sky |
| `--lane2` | `#7c3aed` | Consultant lane — violet |
| `--lane3` | `#059669` | Tech/Leadership lane — emerald |

---

## Shell Components

### Site Nav
```html
<nav class="shell-nav">
  <div class="shell-nav-inner">
    <a href="../" class="shell-brand">…</a>
    <div class="shell-nav-links">
      <a href="#" class="shell-nav-link">Link</a>
      <a href="#" class="shell-nav-link active">Active Link</a>
    </div>
  </div>
</nav>
```

### Page Layout (with TOC sidebar)
```html
<div class="shell-page with-toc">
  <main class="shell-main" id="main-content">…</main>
  <aside class="page-toc">
    <p class="toc-heading">On this page</p>
    <ul class="toc-list">
      <li><a href="#section-id">H2 section</a></li>
      <li><a href="#sub-id" class="toc-h3">H3 subsection</a></li>
    </ul>
  </aside>
</div>
```

### Page Layout (no sidebar)
```html
<div class="shell-page">
  <main class="shell-main" id="main-content">…</main>
</div>
```

---

## 004 Module Components

### Chapter Hero
```html
<header class="chapter-hero">
  <div class="container">
    <div class="ch-eyebrow">
      <span class="ch-num">Chapter 1</span>
      <span class="ch-tag-label">Foundations</span>
    </div>
    <h1>How LLMs Work</h1>
    <p class="hero-key-q">Why does the exact wording change the output?</p>
  </div>
</header>
```

### Phase Bar (5 C's navigation)
```html
<div class="phase-bar">
  <div class="phase-inner">
    <a class="phase-pip" data-c="1" data-section="connection" href="#connection">
      <div class="phase-dot">C</div>
      <span class="phase-name">Connection</span>
    </a>
    <!-- … -->
  </div>
</div>
```

### Section Badges
```html
<span class="section-badge badge-c1">C1 · Connection</span>
<span class="section-badge badge-c2">C2 · Content</span>
<span class="section-badge badge-c3">C3 · Challenge</span>
<span class="section-badge badge-c4">C4 · Change</span>
<span class="section-badge badge-c5">C5 · Closure</span>
```

### Card Grid
```html
<div class="card-grid cols-2">
  <div class="card c1">…</div>
  <div class="card c2">…</div>
</div>
```

Card border variants: `c1`–`c5`, `lane1`–`lane3`, `amber`, `sky`, `violet`, `pink`, `emr`, `danger`, `neutral`

### Callout Boxes
```html
<div class="callout info">
  <span class="callout-icon">ℹ️</span>
  <div><p>Info message</p></div>
</div>
```
Variants: `info`, `warn`, `danger`, `success`

### Prompt Display (dark code block)
```html
<div class="prompt-block">
  <span class="prompt-label strong">Strong prompt</span>
  <div class="prompt-display strong">
    <span class="P">You are a translation consultant…</span>
  </div>
  <div class="bb-legend">
    <span class="bb-pill P">Persona</span>
    <span class="bb-pill CX">Context</span>
  </div>
</div>
```

Annotation spans: `.P` (Persona), `.CX` (Context), `.F` (Format), `.G` (Guardrails), `.FS` (Few-shot), `.CT` (Chain-of-thought)

### Reveal Button
```html
<button class="reveal-btn" data-target="reveal-1"
        data-open-text="Show strong prompt"
        data-close-text="Hide prompt">
  <span class="btn-text">Show strong prompt</span>
  <span class="reveal-arrow">▼</span>
</button>
<div class="hidden-reveal" id="reveal-1">
  <!-- hidden content shown on click -->
</div>
```

### Lane Toggle
```html
<div class="lane-group">
  <div class="lane-toggle">
    <button class="lane-btn" data-lane="1">Translators</button>
    <button class="lane-btn" data-lane="2">Consultants</button>
    <button class="lane-btn" data-lane="3">Tech &amp; Leadership</button>
  </div>
  <div class="lane-content" data-lane="1">…</div>
  <div class="lane-content" data-lane="2">…</div>
  <div class="lane-content" data-lane="3">…</div>
</div>
```

### Activity Box (C3)
```html
<div class="activity-box">
  <div class="activity-header">
    <span class="activity-icon">✏️</span>
    <h3>Activity Title</h3>
  </div>
  <p>Instructions…</p>
</div>
```

### Commitment Box (C4)
```html
<div class="commitment-box">
  <div class="commitment-header">
    <h3>My Commitment</h3>
  </div>
  <p class="commitment-prompt-text">One thing I will try this week…</p>
  <textarea class="commitment-input" rows="4"></textarea>
  <div class="commitment-actions">
    <button class="btn-print">🖨 Print</button>
  </div>
</div>
```

### Big Quote (C5)
```html
<div class="big-quote">
  <blockquote>The model completes patterns…</blockquote>
  <cite>Source</cite>
</div>
```

### Step List
```html
<ol class="step-list">
  <li>
    <div class="step-num">1</div>
    <div class="step-body"><strong>Step title</strong> Description text.</div>
  </li>
</ol>
```

### Chapter Footer Nav
```html
<div class="chapter-footer-nav">
  <div class="nav-row">
    <a href="ch01.html" class="ch-nav-btn">← Previous</a>
    <span class="ch-nav-spacer"></span>
    <a href="ch03.html" class="ch-nav-btn primary">Next →</a>
  </div>
</div>
```

---

## 006 Module Components

### Hero (maintained dark for visual impact)
```html
<div class="hero">
  <p class="hero-meta">AILT 2026 · AI Tools Track</p>
  <h1>Session Title</h1>
  <p class="hero-sub">Subtitle text</p>
  <div class="hero-pills">
    <span class="pill sky">Day 3 · Morning</span>
    <span class="pill amber">45 minutes</span>
  </div>
</div>
```

### Session Map Bar
```html
<div class="map-bar">
  <div class="map-inner">
    <a class="map-step c1" href="#c1">Connection<span class="mtime">00:00</span></a>
    <div class="map-line"></div>
    <!-- … -->
  </div>
</div>
```

### C-Section Header (006 style)
```html
<section class="c-section" id="c1">
  <div class="c-header">
    <div class="c-badge badge-amber">1</div>
    <div class="c-title-area">
      <div class="c-label">C1 · Connection</div>
      <div class="c-title">Section Title</div>
      <div class="c-timing">⏱ 00:00 – 00:05 · 5 minutes</div>
    </div>
  </div>
  <div class="cards">…</div>
</section>
```

### Scenario Box (006)
```html
<div class="scenario">
  <strong>Scenario</strong>
  <p>Description…</p>
</div>
```

### Task Box
```html
<div class="task-box">
  <div class="task-label">✏️ Your task — 90 seconds</div>
  <div class="task-title">Task title</div>
  <div class="task-desc">Description</div>
</div>
```

### Tip Box
```html
<div class="tip info">
  <span class="tip-icon">💬</span>
  <span>Tip content</span>
</div>
```
Variants: `info`, `warn`, `success`

### Prompt Block (006, dark display)
```html
<div class="prompt-block">
  <div class="pb-header"><div class="dot"></div> Prompt</div>
  <div class="pb-rows">
    <div class="pb-line">
      <span class="pb-tag p">P</span>
      <span class="pb-text">You are a biblical scholar…</span>
    </div>
  </div>
</div>
```

---

## Handbook Prose

Handbook pages wrap their content in:
```html
<div class="prose-content">
  <!-- markdown-converted HTML -->
</div>
```

All standard HTML elements (`h1`–`h4`, `p`, `ul`, `ol`, `table`, `code`, `pre`, `blockquote`) receive styled prose treatment via `.prose-content *` selectors.

---

## Presentation Mode

Activated by `?present` URL parameter. `script.js` detects this, adds `body.present-mode`, and calls `initPresentation()`.

- For pages with `.c-section` elements: sections are shown/hidden one at a time
- For handbook pages: h2 blocks are wrapped and shown/hidden
- Controls: `◀ Prev`, `Next ▶`, `✕ Exit` (fixed bottom bar)
- Keyboard: `←`/`→` arrows advance sections; `Esc` exits

---

## Build Commands

```bash
python scripts/build.py          # incremental (skip unchanged)
python scripts/build.py --force  # rebuild everything
python scripts/build.py --clean-only  # delete docs/ only
```

Or via Make:
```bash
make build     # incremental
make force     # full rebuild
make clean     # delete docs/
make serve     # local preview at http://localhost:8000
```
