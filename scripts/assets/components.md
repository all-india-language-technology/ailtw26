# CSS Component Reference
> Quick reference for slides.html authoring. One read = zero re-discovery needed.

## Layout containers

```html
<div class="s vcenter">     <!-- slide wrapper, vertically centred -->
<div class="s center">      <!-- slide wrapper, centred both axes (title slides) -->
<div class="two-col">       <!-- 2-column grid, 1fr 1fr, gap 20px -->
<div class="role-grid">     <!-- 2×2 grid -->
<div class="step-flow">     <!-- vertical step connector list -->
```

## Feature cards `.fcard`

```html
<div class="fcard sky|violet|emerald|amber|pink|red">
  <span class="fc-icon">🔢</span>
  <div class="fc-body">
    <div class="fc-title">Title</div>
    <div class="fc-desc">Description</div>
  </div>
</div>
```

## Bucket / classify cards `.bucket-card`

```html
<div class="bucket-grid">   <!-- default 3-col; override with style="grid-template-columns:..." -->
  <div class="bucket-card sky|violet|emerald|amber|pink|red">
    <div class="bc-title">Title</div>
    <div class="bc-desc">Description</div>
  </div>
</div>
```

## Callouts `.callout`

```html
<div class="callout info|warn|success|danger|violet">
  <span class="co-icon">💡</span>
  <span>Content with <strong>bold</strong> supported.</span>
</div>
```

## Tables `.slide-table`

```html
<table class="slide-table">
  <thead><tr><th>Col A</th><th>Col B</th></tr></thead>
  <tbody>
    <tr class="row-danger|row-success|row-warn">
      <td class="label-danger|label-success">Label</td>
      <td>Content</td>
    </tr>
  </tbody>
</table>

<!-- Split table — left header red, right header emerald -->
<table class="slide-table split-table">
  <thead><tr><th>Fixed</th><th>In Your Hands</th></tr></thead>
  ...
</table>
```

## Slide-level chrome

```html
<span class="slide-tag tag-nlp|tag-hook|tag-transfer|tag-close|tag-activity|tag-deepdive|tag-reflection|tag-aspiration|tag-challenge|tag-options|tag-roadmap">Label</span>
<h2 class="slide-h sky|violet|emerald|amber|pink">Heading</h2>
<p class="eyebrow">SMALL CAPS KICKER</p>
<div class="big-quote">Quote with <em>gradient highlight</em></div>
<div class="slide-num">7</div>
<div class="slide-timer">⏱ __TIMER_key-name__</div>
<div class="nav-hint">↓ next sub-slide</div>
```

## Images

```html
<img src="../assets/filename.png" class="slide-img" alt="description">
<p class="img-caption">Caption text</p>
```
Note: path is relative from `output/presentation.html` → `assets/` at module root.

## Timer tokens

Format: `__TIMER_<key>__` where `<key>` matches a `slide-<key>:` entry in `timings.txt`.
Use semantic names (e.g. `__TIMER_key-terms__`), not numbers.
Unspecified slides fall back to `default-slide:` in `meta.txt`.
Sub-slides in vertical stacks do NOT get timer tokens — time is tracked by the parent only.

## Vertical stacks (Reveal.js)

```html
<section>               <!-- position container — no content here -->
  <section>             <!-- top slide — gets the __TIMER__ token -->
    <div class="nav-hint">↓ description</div>
  </section>
  <section>             <!-- sub-slide — no timer token -->
    ...
  </section>
</section>
```

## Colour palette (CSS variables)

| Variable | Hex | Use |
|---|---|---|
| `--sky` | #38bdf8 | Primary / information |
| `--violet` | #a78bfa | Secondary / depth |
| `--emerald` | #34d399 | Success / positive |
| `--amber` | #fbbf24 | Warning / caution |
| `--red` | #f87171 | Danger / failure modes |
| `--pink` | #f472b6 | Transfer / capabilities |

Each colour has `--sky-dim`, `--sky-border` variants for backgrounds and borders.
