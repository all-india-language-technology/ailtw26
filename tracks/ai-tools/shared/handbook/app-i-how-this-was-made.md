# Appendix I: How This Handbook Was Made
## A Worked Example of AI-Assisted Knowledge Work in an IDE

*This appendix is a transparency note and a case study in one. It documents how this handbook — the document you are holding — was produced. It is written so that anyone who has read this far can see exactly what was done, by whom, and what role AI played at each step. It is also intended as a concrete illustration of the IDE-based agentic workflow described in §G.6.*

---

## I.1 The Starting Point

This handbook did not begin as a document. It began as a preparation problem.

The task was to run a four-day AI tools track for a mixed audience of Bible Translation practitioners — translators, consultants, linguists, language technology specialists, literacy workers, and project leaders. That audience needed something they could continue using after the workshop: a reference they could return to when the session notes had faded and the exercises were a distant memory.

What already existed at the start of the handbook project:

- A presentation (used in pre-workshop peer review) covering prompt engineering foundations
- A set of planning notes capturing audience analysis, learning outcomes, lane structure, and rough topic lists
- An interview transcript with subject matter experts
- Module outlines for the workshop sessions
- Domain expertise about Bible Translation workflows, accumulated across years of practice

What did not yet exist: a structured, typeset, distributable handbook with consistent formatting, internal cross-references, multiple output formats (PDF, HTML), and the depth of coverage a reference document requires.

The question was how to close that gap in the time available — days, not weeks — without losing quality.

---

## I.2 The Workspace

The work was done in **VS Code** with **GitHub Copilot** — an AI-equipped Integrated Development Environment of exactly the kind described in §G.6.

The handbook's source files are plain Markdown — a lightweight text format with no proprietary lock-in, readable without any tool, and processable by scripts. A Python build pipeline converts those Markdown files into a typeset PDF (via pandoc and XeLaTeX) and a styled HTML file. All of this lives in a git repository.

The workspace structure looked like this:

```
handbook/        ← Markdown source (ch00–ch05, app-A through app-I)
scripts/         ← Python build scripts
output/          ← generated PDF and HTML (not in git)
notes/           ← planning notes and rough captures
modules/         ← workshop session outlines
```

Every file in this structure was visible to the AI at all times. There was no need to paste content into a chat window. Opening the workspace meant the AI could already read the planning notes, the existing chapters, the build scripts, and the previous session's output at once.

---

## I.3 What the Workflow Actually Looked Like

The workflow was not: *write a prompt → get a chapter → paste it in*.

It was a **conversation across multiple sessions**, each picking up where the last left off. The rough shape of each cycle:

1. **Provide context and direction.** Describe what is needed — sometimes from a bullet list of topics, sometimes from rough notes, sometimes by pointing at an existing section that needs revising.
2. **The AI drafts or executes.** Depending on the task: writes a chapter section, builds a Python script, fixes a compilation error, refactors a regex.
3. **Review and catch what is wrong.** Read the output. Apply domain expertise. Identify errors, gaps, and misframings.
4. **Redirect.** Describe the problem. Ask for a revision. The AI revises.
5. **Commit what is good.** When a piece is solid, commit it to git. Move to the next task.

The git history is a record of this process. Each commit represents a checkpoint where the human author reviewed the work, judged it sound, and locked it in.

**An illustrative example:** Early in the project, the handbook contained a factual error. Chapter 1 described attention mechanisms as producing a structural limit on what an LLM can "remember" — implying that fade toward the end of a long context is baked into the architecture. Appendix F, written separately, described the Transformer architecture more carefully and made clear that attention is *not* inherently recency-biased. The two sections contradicted each other.

This error was caught during review, not by the AI independently. The AI had written both sections coherently in isolation; it was the human reading across the full document who noticed the contradiction. Once flagged, the AI revised both sections — adding a careful distinction between structural capability (uniform attention is possible in principle) and learned behavioural tendency (models trained on typical data develop recency bias empirically). The fix was precise and technically correct. But it happened because a human was reading for consistency, not because the AI was monitoring itself.

---

## I.4 What the AI Did

Across the handbook's production, the AI performed the following:

**Writing from outlines and notes.** Each chapter and appendix began from something: bullet points in a planning document, rough notes from a conversation, a section heading and a sentence of intent. The AI turned these into structured prose — with section hierarchy, examples, summary rules, and cross-references — that would have taken days to write manually.

**Appendix G** was written almost entirely from the bullet list in the planning notes. The author described ten topic areas; the AI wrote ten full sections, each with background, practical guidance, trade-offs, and a summary rule. The author reviewed each section for accuracy, added domain-specific corrections, and directed expansions.

**Appendix H** was written from a rougher set of notes — fragments about LLM data scarcity, audio data in BT communities, NLLB, Masakhane, and ScriptureForge — plus the author's own analysis of the strategic gap. The AI organised these fragments into a coherent seven-section structure and wrote them up. The author reviewed and requested emphasis changes — for example, explicitly strengthening the framing of audio data as an underrecognised asset.

**Building and debugging the technical pipeline.** The PDF build pipeline is non-trivial: Markdown goes through a custom Python preprocessor (converting quotation boxes, placeholder text, and example labels into LaTeX commands), then through pandoc for structure, then through XeLaTeX for typesetting. The HTML pipeline runs through a different Python script with custom CSS.

None of this existed at the start. The AI wrote the build scripts, debugged multiple XeLaTeX compilation failures (missing packages like `calc`, undefined macros from pandoc's syntax highlighting output, a counter error from table rendering), fixed regex bugs that were causing multi-paragraph prompt boxes to truncate, and added CSS for styled placeholder text. This would have been hours of manual debugging; it was instead a series of directed conversations.

**Maintaining consistency across sessions.** Because the AI could see all files in the workspace, it maintained cross-references between sections — when a new appendix was added, it updated references in other appendices and the build scripts simultaneously.

---

## I.5 What the Human Did

The AI's contribution was real and substantial. So was the human author's. These are not in competition; they were complementary.

**Domain expertise.** The AI does not know what matters to a Bible Translation consultant in a field setting. It does not know the difference between a key-term decision and a naturalness question. It does not know what "Informed Pilot" means as a posture in this community, or why that framing lands differently than "use AI carefully." The author knew all of this and shaped the content accordingly.

**Audience calibration.** Every section in this handbook is pitched at a specific audience with a specific mix of roles, a specific level of technical familiarity, and specific constraints (low-resource languages, field conditions, restricted contexts). The AI could execute on tone and register when told what was needed; it could not infer the right calibration on its own.

**Factual review.** The AI produces confident text. Confident is not the same as correct. Every section was reviewed against what the author knew to be true. Technical claims about how models work, claims about specific tools or initiatives (NLLB, FLORES, Scripture Forge), and theological framings were all checked. Some needed correction; most were accurate; a few were over-simplified and required nuance.

**Structural judgment.** What goes in this handbook and what doesn't, how the appendices relate to the chapters, where to put a cross-reference and where to leave space — these are not questions the AI can resolve. They require a human who knows what this workshop is trying to do and what readers will need when they come back to this document six months later.

**All commits.** Every commit to the git repository represents a human decision that something was ready. The AI never pushed anything. Each checkpoint was locked in by the author, after review.

---

## I.6 The Timeline

The workshop presentation materials were built on **12 March 2026**.

The full handbook — six chapters, nine appendices, a typeset PDF and HTML output, and a working build pipeline — was produced on **16 March 2026**. Four days later.

The handbook represents several months of accumulated expertise about Bible Translation workflows, AI tools, and adult learning design. That expertise existed before the AI was involved. What the AI shortened was the time from *expertise exists* to *expertise is documented, structured, and distributed*.

This is the honest account of what AI-assisted knowledge work looks like at its best: a human with deep domain knowledge, working in a capable tool environment, producing a document that captures and organises what they already knew in a fraction of the time it would have taken alone.

---

## I.7 What This Means for the Reader

If you are a Bible Translation practitioner reading this, the relevance is direct.

You already have domain expertise. You know your target language, your community, your translation workflow, your key-term decisions, your project history. That expertise is the irreplaceable input. What an IDE with AI can do is help you turn that expertise into structured documents, formatted outputs, consistent reports, and repeatable tools — at a speed that was not previously available to people who were not programmers.

The workflow described in §G.6 is not theoretical. The handbook you are reading is its output.

The threshold for using it is lower than it may appear. This handbook was produced by someone who is not a full-time software developer — who needed to debug XeLaTeX preamble errors, manage a Python build pipeline, and write technical sections on model architecture. The AI provided the technical execution; the author provided the judgment about what was correct and what needed saying.

The skills the handbook teaches — precise task description, critical output evaluation, iterative refinement, structured verification — are the same skills that made this workflow function. Prompting is not just for extracting text from a chatbot. It is the interface through which a practitioner with expertise can direct capable tools to produce work at scale.

---

*For the workflow principles behind this approach, see §G.6: Agentic Workflows and Prompting in IDEs.*  
*For the data privacy considerations that govern what can be done in local vs. cloud AI environments, see §G.3: Data Privacy.*  
*For the full case for AI engagement in minority language development, see Appendix H.*
