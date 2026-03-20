/**
 * tailwind.config.js — Design token reference (Tailwind v3 format)
 *
 * NOTE: The installed binary is Tailwind v4, which uses CSS-native
 * configuration (@theme blocks in input.css) instead of this file.
 * This file is kept as documentation of the design token values.
 * The actual compiled CSS is generated from scripts/assets-src/input.css.
 *
 * Design tokens are applied as CSS custom properties (:root) in input.css.
 */
module.exports = {
  content: [
    'scripts/templates/**/*.html',
    'docs/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        navy:  { DEFAULT: '#1B2B5E', dim: '#14203F', light: '#243870' },
        brand: '#F4A020',
        c1: '#ea580c',
        c2: '#2563eb',
        c3: '#7c3aed',
        c4: '#059669',
        c5: '#d97706',
        lane1: '#0284c7',
        lane2: '#7c3aed',
        lane3: '#059669',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
    },
  },
  plugins: [],
};
