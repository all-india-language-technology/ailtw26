# Prompt with Precision — Handbook Build Plan

**Full Title:** Prompt with Precision: A Practitioner's Guide to AI Prompting for Bible Translation  
**Subtitle:** AI Tools Track · Prompt Engineering Module · AILT 2026  
**Target Audience:** Bible Translation practitioners across three lanes — Translators & Language Workers (Lane 1), Consultants & Advisors (Lane 2), Leadership & Technical Enablers (Lane 3)  
**Purpose:** A focused, take-home reference handbook covering everything taught in the Prompt Engineering module — principles, techniques, lane-specific examples, and a ready-to-use template library.  
**Scope:** Prompt engineering only. Other AI Tools track topics (Scripture Forge, AQuA, LM Studio, etc.) are out of scope for this handbook.

---

## Build Workflow

```
Stage 1 → Markdown  (you are here)
Stage 2 → Review & finalize topics, examples, appendices
Stage 3 → Convert each chapter to .tex (XeLaTeX-ready)
Stage 4 → Compile master .tex via XeLaTeX → PDF
```

### Stage 3–4 Notes (for when ready)
- Compiler: XeLaTeX (required for Unicode / non-Latin script support)
- Font: Unicode-capable serif — Gentium Plus or Linux Libertine recommended
- Master file: `handbook-main.tex` (imports all chapter .tex files via `\input{}`)
- Package plan: `fontspec`, `geometry`, `hyperref`, `tcolorbox`, `booktabs`, `longtable`, `microtype`
- Each appendix will be a separate `\chapter*{}` in the backmatter

---

## File Structure

| File | Content |
|---|---|
| `ch00-frontmatter.md` | Title page, preface, how to use this handbook |
| `ch01-how-llms-work.md` | How LLMs work · The risk radar · Why prompting matters |
| `ch02-anatomy-of-a-prompt.md` | Six building blocks: Persona, Format, Guardrails, Few-Shot, Chain of Thought, Context |
| `ch03-master-formula.md` | Instruction + Materials + Tools + Additional Info · Iteration loop |
| `ch04-advanced-techniques.md` | Context window management · AI session brief · System prompts · One-task-per-chat |
| `ch05-prompting-by-lane.md` | Lane 1, Lane 2, and Lane 3 prompt patterns with worked examples |
| `app-A-glossary.md` | Glossary of key AI and prompting terms |
| `app-B-risk-reference.md` | Risk Quick Reference — all six failure modes with mitigations |
| `app-C-lane-reference.md` | Lane Reference Card — quick-access prompt pairs by role |
| `app-D-prompt-templates.md` | Prompt Template Library — production-ready, copy-paste templates |
| `app-E-meta-prompting.md` | Meta Prompting — using the AI to write and improve your prompts |
| `app-F-attention-paper.md` | "Attention Is All You Need" — plain-English story of the paper and the AI revolution it sparked |

---

## Chapter Summaries

### Chapter 1 — How LLMs Work & Why It Matters for Prompting
Demystifies the machine: pattern matching, word embeddings, the scribe analogy, what AI *cannot* do. Introduces the five risk failure modes (Hallucination, Knowledge Cutoff, Bias & Worldview, Math & Counting, Context Loss) with BT-specific examples and safer prompt alternatives.

### Chapter 2 — Anatomy of a Great Prompt
The six building blocks covered one at a time with weak vs strong examples drawn from Mark 5. Persona, Output Format, Guardrails, Few-Shot Prompting, Chain of Thought, and Context (Situational Background).

### Chapter 3 — The Master Formula
The four-component framework: Instruction, Materials, Tools, Additional Info. Covers the iteration loop (conversational steering) and how to assemble all four components into a production workflow.

### Chapter 4 — Advanced Techniques
How the context window works, why guardrails silently disappear in long sessions, and four practical defences: Task Chunking, Summarise & Restart, AI Session Brief, and System Prompts.

### Chapter 5 — Prompting by Lane
Lane-specific worked examples covering the full six-technique set. Translators, Consultants, and Support/Leadership roles each get a dedicated section with realistic BT scenarios.

---

## Status Tracker

| File | Status | Notes |
|---|---|---|
| `ch00-frontmatter.md` | � Complete | Title page, preface, lane defs, Mark 5 through-line, AI/Scripture note |
| `ch01-how-llms-work.md` | 🟢 Complete | All 5 risk modes with BT examples and safer alternatives |
| `ch02-anatomy-of-a-prompt.md` | 🟢 Complete | 6 building blocks, combining table, full assembled example |
| `ch03-master-formula.md` | 🟢 Complete | 4 components, iteration loop, full workflow example |
| `ch04-advanced-techniques.md` | 🟢 Complete | 4 context window defences, ecosystem/data sensitivity |
| `ch05-prompting-by-lane.md` | 🟢 Complete | 9 lane scenarios, cross-lane exercises |
| `app-A-glossary.md` | 🟢 Complete | 30 terms — AI fundamentals through advanced prompting |
| `app-B-risk-reference.md` | 🟢 Complete | All 6 failure modes, decision guide |
| `app-C-lane-reference.md` | 🟢 Complete | 9 prompt pairs (3 per lane), weak/strong with explanation |
| `app-D-prompt-templates.md` | 🟢 Complete | 10 production templates with lane/task/technique labels |
| `app-E-meta-prompting.md` | 🟢 Complete | 3 use patterns, 3 lane examples, review checklist, upgrade loop |
| `app-F-attention-paper.md` | 🟢 Complete | Plain-English story of the 2017 paper, GPT timeline, wonder-focused narrative |

**Stage 1 (Markdown) — COMPLETE. Ready for Stage 2 review.**

Legend: 🔴 Not started · 🟡 In progress · 🟢 Complete
