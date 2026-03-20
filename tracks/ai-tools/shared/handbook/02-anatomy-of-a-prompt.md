# Chapter 2: Anatomy of a Great Prompt

> **Session tag:** Core Techniques  
> **Key question:** What are the building blocks of a prompt that consistently produces translation-grade output?

---

## 2.0 From Understanding to Crafting

Chapter 1 (section 1.3) maps all nine factors that shape what an LLM produces — from training data and fine-tuning purpose through to the four levers you control directly: model choice, system prompt, augmentation data, and your prompt. This chapter focuses on the last of those levers: **how to construct the prompt itself**.

For augmentation data — supplying documents, glossaries, and project context to extend the model's knowledge for a specific task — see Chapter 3.

---

## 2.1 The Specificity Advantage

Of the four factors you control, how you construct your prompt has the highest immediate impact on output quality. The single most important principle in prompting is: **specificity**.

Vague prompts produce generic outputs. Specific prompts produce usable outputs. The difference is not the quality of the AI — it is the quality of the instruction.

| Prompt | What you get |
|---|---|
| *"Explain Mark 5"* | A Sunday-school summary aimed at a general reader |
| *"Act as an exegetical consultant. Summarize the cultural and economic significance of the pigs in Mark 5:1–20 for a translation team working in a region where pigs are highly prized wealth. Use plain English. Do not speculate beyond the text."* | A targeted, culturally-anchored, exegetically grounded summary ready to use in a translation session |

Every element of the strong prompt does specific work. The building blocks below explain exactly what each element contributes — and how to apply them across your own translation tasks.

---

## 2.2 Building Block 1: Persona (Role Assignment)

**What it does:** Tells the model *who to be* for this task. This sets the vocabulary, the expertise level, the default framing, and the depth of the response.

Without a role, the model defaults to a generic helpful assistant aiming at a general audience. With a role, it draws from a specific domain of its training and calibrates the output accordingly.

**How to use it:** Start the prompt with *"Act as a…"* or *"You are a…"* followed by a specific, relevant expert description.

### Examples by Lane

**Lane 1 — Translator**
> *"Act as a rural mother-tongue translator encountering this passage for the first time. Read the following back-translation and identify three phrases that feel unnatural in spoken language."*

**Lane 2 — Consultant**
> *"Act as a senior translation consultant specialised in Biblical Greek exegesis. Analyse the following draft rendering of Mark 5:9 for theological accuracy."*

**Lane 3 — Leadership / Support**
> *"Act as a technical project manager writing a status update for a non-technical stakeholder. Summarise the following meeting notes."*

### Common mistake

Assigning a role that is too vague defeats the purpose. *"Act as an expert"* tells the model almost nothing. *"Act as a biblical scholar specialised in Second Temple Judaism writing for a translation team in a shame-honour culture"* gives the model substantial, useful framing.

---

## 2.3 Building Block 2: Output Format

**What it does:** Tells the model *how to structure the response* — table, checklist, numbered list, prose paragraphs, JSON, markdown. Left unspecified, the model defaults to flowing prose, which is often harder to use directly.

**Why it matters in BT work:** You frequently need output that can be pasted directly into Paratext notes, an Excel sheet, a checking report, or a team communication. Specifying the format saves manual reformatting and makes the output immediately actionable.

**How to use it:** Add a format instruction toward the end of the prompt, after the task description.

### Format examples

| Format instruction | When to use it |
|---|---|
| *"Return as a 3-column markdown table: Verse \| Issue \| Suggestion"* | Checking notes, issue logs |
| *"Provide a bulleted checklist with a checkbox for each action item"* | Meeting follow-up, task lists |
| *"Number each point. No prose introduction or conclusion."* | Quick analysis, structured review |
| *"Format as: Term — Definition — Translation Risk"* | Key-term analysis |
| *"Return one paragraph, 100 words maximum"* | Executive summary, quick brief |
| *"Format the following genealogy as valid USFM, using \\lh, \\li, \\b markers. Output only the USFM — no explanation, no prose wrapper."* | Scripture data entry, Paratext import |

### Lane 3 note

Lane 3 practitioners working with administrative data — meeting notes, project reports, rollout checklists — gain the most from format specification. A prompt that produces a markdown checklist table can be pasted into Notion, Word, or a project management tool with zero reformatting. Define the columns explicitly: *"Action | Owner | Deadline | Status."*

---

## 2.4 Building Block 3: Guardrails (Negative Constraints)

**What it does:** Tells the model what *not* to do. Guardrails are the safety fence that prevents the model from drifting into speculation, hallucination, theological overreach, or inappropriate register.

In Bible Translation, guardrails are not optional. The model's default is to be helpful and complete — which means it will fill gaps with plausible-sounding content, speculate when uncertain, and elaborate beyond the evidence. Guardrails override these defaults explicitly.

**How to use it:** Add negative constraints ("Do not…") and uncertainty-flagging instructions ("If uncertain, flag it as NEEDS VERIFICATION rather than guessing").

### Core guardrails for BT work

**Execution constraint:**
> *"Do not paraphrase the source text. Quote it exactly as given."*

**Theological constraint (most important):**
> *"Do not speculate beyond the text. If you are uncertain about any interpretation, flag it as NEEDS VERIFICATION rather than presenting it as established."*

**Tone constraint:**
> *"Do not use theological jargon (e.g. 'eschatological', 'expiation', 'penal substitution'). Use plain English accessible to a primary-school reader."*

**Reference constraint (anti-hallucination):**
> *"Do not cite specific Louw-Nida codes, Greek dictionary entries, or scholar names. I will verify those independently. Describe the semantic range in plain terms only."*

**Hallucination-reduction instruction:**
> *"If you do not know something, say so. Do not fabricate an answer to fill the gap."*

### Temperature in plain language

Most AI chat interfaces do not show a temperature slider, but you can achieve the same effect through word choice. The language you use in guardrails implicitly steers the model toward precision or creativity:

- **Cold (precise, literal):** *"Be precise and literal. Do not speculate or be creative. Give one definitive answer."*  
  Use for: exegesis, back-translation review, checking questions, key-term analysis
- **Medium (fluent but accurate):** No special instruction needed. Default behaviour.  
  Use for: cultural background synthesis, structured summaries
- **Warm (creative, varied):** *"Generate 3 creative variations. Be expressive and culturally vivid."*  
  Use for: community-engagement scripts, story illustrations, training materials

**Critical point:** Never run checking or exegesis work in a "warm" session. Warm language produces fluent output that drifts from the source. For accuracy-sensitive work, always include a cold guardrail: *"Be precise and literal. Do not speculate."*

---

## 2.5 Building Block 4: Few-Shot Prompting (Teaching by Example)

**What it does:** Instead of describing the style or format you want in abstract terms, you show the model *one perfect example* and ask it to follow that exact pattern. The model learns your team's style, vocabulary, and format from the example instantly.

**Why it matters:** Writing a paragraph of instructions explaining your team's checking-question style, your project's tone, or your preferred report format is hard and often produces inconsistent results. One well-chosen example communicates all of that effortlessly.

**How to use it:** Provide the example first, labelled clearly, then give the new task.

### Example — Lane 2, checking questions

**Zero-shot (no example):**
> *"Write a checking question for Mark 5:3."*

Result: inconsistent with your team's established style — may be too long, too short, too literal, or at the wrong reading level.

**One-shot (with example):**
> *"Here is a good checking question for Mark 5:2: 'Where did the possessed man come from when he met Jesus?' Now write a checking question for Mark 5:3 following this exact pattern — one sentence, plain language, observable fact, no interpretation."*

Result: style-consistent, vocabulary-consistent, team-ready.

### Example — Lane 3, meeting summary

**Zero-shot:**
> *"Summarise this meeting."*

**One-shot:**
> *"Here is an example summary entry from last week: '— Ben to send revised project timeline to all leads by Friday. Owner: Ben. Deadline: Friday 13 Mar.' Using exactly this format (dash + action + Owner + Deadline), summarise the action items from the following meeting notes: [paste notes]"*

### When to use few-shot

Use it whenever:
- Your team has an established style or format that differs from a generic template
- You have been dissatisfied with zero-shot outputs and cannot easily describe what is wrong
- You want consistency across multiple outputs (e.g. checking questions for an entire chapter)

One excellent example is usually enough. Two examples further clarify edge cases.

---

## 2.6 Building Block 5: Chain of Thought (CoT)

**What it does:** Instructs the model to map out its reasoning *step-by-step before arriving at a final answer*. This prevents premature conclusions, exposes the model's assumptions at each stage, and gives you traceable reasoning you can audit and correct.

**Why it matters in BT:** Translation decisions — especially key-term choices, rendering of culturally loaded words, and identification of implicit information — involve multiple layers of reasoning. If the model skips straight to a recommendation, you cannot tell whether it understood all the relevant layers. If it reasons out loud, step by step, you can catch an error at Step 1 before it corrupts the final recommendation.

### Case study: Rendering "Legion" in Mark 5:9

The word "Legion" is a classic example of a term that requires layered reasoning before a translation recommendation can be trusted.

**Without Chain of Thought:**
> *"What are some plausible ways of expressing 'Legion' in Mark 5:9 in my translation?"*

The model produces a list of options with apparent confidence. You cannot tell whether it understood the Roman military connotation, the theological significance of scale, or the likely available equivalents in your target culture. The suggestions may be linguistically plausible but theologically shallow — and you have no way to evaluate them without seeing the reasoning behind them.

**With Chain of Thought:**
> *"Work through this step by step before making a recommendation:*
> 
> *Step 1 — What did 'Legion' mean to a first-century Roman audience? (military scale, organized power, dread)*
> 
> *Step 2 — What does the use of this specific word communicate about the nature and scale of this man's possession?*
> 
> *Step 3 — What concept in [target language/culture] communicates 'an overwhelming, innumerable, terrifying spiritual force'?*
> 
> *Only after completing all three steps, suggest 2–3 translation options with your reasoning for each."*

Now you can check the model's reasoning at each stage. If Step 1 is wrong — if the model treats "Legion" as simply meaning "many" rather than as a specific military term — you catch that before it corrupts the recommendation.

**Lane 2 note:** Chain of Thought is the most important technique for consultants and exegetes. It transforms the AI from an oracle delivering verdicts into a traceable research assistant whose reasoning can be audited, challenged, and corrected — which is exactly what a checking process requires.

### How to use it

Add a step-by-step instruction before the final question:

> *"Think step by step. First, [reasoning step 1]. Then, [reasoning step 2]. Finally, [conclusion or recommendation]."*

Or more simply:
> *"Think step by step before answering. Show your reasoning at each stage."*

---

## 2.7 Building Block 6: Context (Situational Background)

**What it does:** Tells the model *the situation you are in* — who you are, what project this is for, what constraints apply, who will use the output, and what success looks like. This is distinct from pasting source text into the conversation (that is external context, covered fully in Chapter 3). Situational context calibrates *how* the model reasons before it begins, not merely *what* it reasons about.

**Why it matters:** Without situational background, the model fills gaps with assumptions — it assumes a generic audience, a generic purpose, and generic constraints. Those assumptions are almost never correct for Bible Translation work. Situational context overrides the defaults explicitly before any reasoning begins.

**A simple test:** If you handed your prompt to a stranger with no other information, would they have enough to do the task well? If not, the missing information is your context.

**How to use it:** Add a background statement early in the prompt — after the Persona instruction, before the task itself.

### What to include

| Information type | Example |
|---|---|
| **Who you are** | *"I am a mother-tongue translator working in Tamil with a team of three."* |
| **The project** | *"We are in checking stage 2 of the Gospel of Mark."* |
| **The audience** | *"Our primary audience is first-generation literate adults in rural Tamil Nadu."* |
| **Purpose of output** | *"This response will be used in a team discussion, not published directly."* |
| **Key constraints** | *"We follow the UBS translation brief. Avoid theological register."* |

### Example — with and without context

**Without context:**
> *"Act as a translation consultant. Review this back-translation of Mark 5:1–5 and identify naturalness issues."*

The model reviews the text and returns feedback calibrated for a generic document. It does not know your language family, your community's oral register, or that you are preparing for a consultant check next week.

**With context:**
> *"Act as a translation consultant. I am working in Tamil with a mother-tongue team in rural Tamil Nadu. We are at checking stage 2, preparing for a consultant check next week. Our community has a strong oral storytelling tradition — the translation should sound like a story told aloud, not a formal written document.*
>
> *Review this back-translation of Mark 5:1–5 and identify any phrases that would sound stilted when read aloud."*

The same instruction, radically different output — the model now knows who it is serving, what matters, and what the standard of success is.

### Lane note

**Lane 1 (Translators):** Include your language name, target community, and current project stage. Even one sentence of context sharpens the output significantly.

**Lane 2 (Consultants):** Include the type of check (naturalness, accuracy, key-term), the translation team's background language, and any issues carried forward from prior checking sessions.

**Lane 3 (Leadership / Support):** Include your organisation, your audience (church leaders, donors, partner organisations), and the purpose of the document you are producing.

---

## 2.8 Combining the Building Blocks

You do not need all six building blocks in every prompt. The right combination depends on the task:

| Task type | Recommended building blocks |
|---|---|
| Exegesis / key-term analysis | Persona + Context + Guardrails (cold) + Chain of Thought |
| Checking question generation | Persona + Context + Format + Few-Shot |
| Cultural background research | Persona + Context + Guardrails (cultural anchoring) + Format |
| Back-translation review | Persona + Context + Guardrails (theological) + Format + CoT |
| Administrative summary | Context + Format + Few-Shot |
| Creative illustration | Persona + Guardrails (warm) + Format |

> **Note:** Building Block 6 (Context) can be added to almost any prompt. The table above omits it only where the task is fully self-contained — e.g. a creative writing task where there is no project-specific constraint. When in doubt, add a sentence of situational background.

### A fully assembled example prompt

**Task:** Lane 2 consultant needs a structured analysis of how "Legion" is rendered in a back-translation draft.

> *"Act as a senior translation consultant. [Persona]*
> 
> *I am working with a mother-tongue translation team in South India. We are at checking stage 2 of Mark and preparing for a consultant review next month. This response will be used in a team discussion session. [Context]*
> 
> *Below is a back-translation of Mark 5:9 from our draft. [External context — paste back-translation here]*
> 
> *Work through the following steps before making a recommendation: [Chain of Thought]*
> *Step 1 — What does the source text word 'Legion' communicate about scale, nature, and the emotional impact on a first-century reader?*
> *Step 2 — Does the back-translation rendering capture those elements? Identify any gaps.*
> *Step 3 — For each gap identified, suggest a specific correction or alternative.*
> 
> *Do not speculate beyond the text. If you are uncertain about any claim, flag it as NEEDS VERIFICATION. [Guardrails]*
> 
> *Return your response as: Finding | Evidence | Recommendation. [Format]"*

This prompt combines five building blocks into a single, coherent instruction that a consultant could use directly in a checking session.

---

*Continue to Chapter 3: The Master Formula →*