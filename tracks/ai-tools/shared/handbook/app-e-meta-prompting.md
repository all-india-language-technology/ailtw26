# Appendix E: Meta Prompting
## Let the AI Write Your Prompts

*Meta prompting is using the AI to generate or improve a prompt you will then use for your actual task. Instead of building a complex, multi-block prompt from scratch, you describe what you need in plain language and ask the model to do the structural work.*

---

## What Meta Prompting Is — and Is Not

**It is:** Using the AI as a prompt engineer — giving it a plain-language description of your task and asking it to produce a structured, detailed prompt built on best practices.

**It is not:** A shortcut past learning the building blocks. You still need to understand what good looks like in order to evaluate and correct the prompt the model generates. The building blocks in Chapter 2 are not less relevant when you use meta prompting — they are the criteria by which you judge the output.

**Critical principle:** A meta-generated prompt inherits the AI's assumptions about your audience, culture, and theological constraints. **Always review it before you use it.** The checklist at the end of this appendix tells you exactly what to check.

---

## Three Ways to Use It

### 1 — Generate a new prompt from scratch

You describe the task; the AI writes the prompt.

> *"I need a prompt that will help me check whether our Tamil translation of Mark 5:1–20 sounds natural when read aloud to a rural audience. Our team are mother-tongue translators, not scholars. The output should be practical — something I can use in a team session this week. Write me a detailed prompt I can use with Claude or ChatGPT, using Persona, Guardrails, and Output Format."*

The model returns a fully structured prompt. You read it, adjust anything that doesn't fit your project, and then use it.

---

### 2 — Improve a prompt you already have

You paste your existing prompt and ask for a structured upgrade.

> *"Here is a prompt I have been using:*
>
> *'Review our back-translation of Mark 5 and flag accuracy issues.'*
>
> *Improve this prompt by adding a clear Persona, relevant Guardrails for Bible Translation accuracy work, a Chain of Thought instruction, and a structured Output Format. Keep it practical — this will be used by a translation consultant, not a software developer."*

The model returns a strengthened version. This is one of the fastest ways to see what ch02's building blocks look like in practice applied to your own real task.

---

### 3 — Generate a reusable template for a recurring task

You describe a workflow that repeats across your project and ask for a template with placeholders.

> *"I need a reusable prompt template for key-term analysis sessions. We use these regularly throughout our translation project — one session per key term. The template should include Persona, a Chain of Thought reasoning structure, Guardrails against speculation, and an Output Format we can paste into our key-term register. Use bracketed placeholders for the parts that change each session (e.g. the term, the passage, the target language)."*

The result becomes your own project-specific entry for App-D — a template built for your team rather than a generic one.

---

## Worked Examples by Lane

### Lane 1 — Translator

**Plain-language request:**
> *"Write me a prompt to help me think through how to render the word 'Legion' in Mark 5:9 into Tamil. I need the AI to reason step by step — not just give me options. I want suggestions I can bring to my consultant."*

**Meta-generated prompt (typical output):**
> *"Act as a biblical exegете and translation advisor working with a Tamil mother-tongue translation team.*
>
> *Work through the following steps before making any recommendations:*
>
> *Step 1 — What does 'Legion' mean in its first-century Roman military context? What does this term communicate about scale, power, and the nature of the possession?*
>
> *Step 2 — What range of Tamil words or phrases could communicate 'an overwhelming, terrifying, innumerable spiritual force'? Consider both formal and colloquial registers.*
>
> *Step 3 — For each option, assess: (a) Does it carry unintended connotations in Tamil cultural context? (b) Is it likely to be understood by a first-generation literate rural reader?*
>
> *After completing all three steps, suggest 2–3 translation options with your reasoning. Do not speculate beyond what the text and linguistic evidence support. Flag any uncertainty as NEEDS VERIFICATION.*
>
> *Return as: Option | Reasoning | Potential Risk | Suggested for consultant review (Yes/No)."*

**Review before use:** Check Step 2 — the model may have assumed a specific register or cultural frame. Adjust to match your team's actual community.

---

### Lane 2 — Consultant

**Plain-language request:**
> *"Write me a prompt for checking a team's key-term decisions against their translation project brief. I want to use this at the start of a checking round. It should compare their actual decisions against the translation project brief guidelines and flag any inconsistencies."*

**Meta-generated prompt (typical output):**
> *"Act as a senior translation consultant conducting a pre-check review.*
>
> *Below I will provide two documents: (1) our translation project brief, which contains our key-term guidelines; and (2) our current key-term decision list.*
>
> *[Paste translation project brief here]*
> *[Paste key-term list here]*
>
> *Work through the key-term list systematically:*
>
> *Step 1 — For each key term, identify the guideline or constraint in the translation project brief that applies.*
>
> *Step 2 — Compare the team's decision against that guideline.*
>
> *Step 3 — Flag any decision that conflicts with, deviates from, or is not addressed by the translation project brief.*
>
> *Do not suggest alternative renderings — only flag inconsistencies for discussion. If a term is not addressed in the translation project brief, flag it as BRIEF GAP rather than marking it as an error.*
>
> *Return as: Term | Team Decision | Relevant Brief Guideline | Status (Consistent / Inconsistent / Brief Gap) | Notes."*

**Review before use:** Confirm that the "BRIEF GAP" category fits your workflow — if you want the AI to suggest alternatives for gaps, remove that constraint.

---

### Lane 3 — Leadership / Support

**Plain-language request:**
> *"I need a prompt to summarise long meeting notes from translation project meetings into a clean action-item table I can send to team leads. The notes are always messy — mixed language, incomplete sentences, tangents. I want something I can reuse every week."*

**Meta-generated prompt (typical output, as a reusable template):**
> *"Act as a project coordinator summarising a translation team meeting.*
>
> *Below are the raw meeting notes from [date] — [meeting title]:*
> *[Paste meeting notes here]*
>
> *Identify every action item, decision, and follow-up mentioned in the notes.*
>
> *For each item:*
> *- Extract the action or decision even if it is stated informally or indirectly.*
> *- Identify the person responsible (if named; otherwise write 'Owner: TBC').*
> *- Identify the deadline (if mentioned; otherwise write 'Deadline: TBC').*
>
> *Ignore general discussion, background context, and tangents that did not produce an action or decision.*
>
> *Return as a markdown table: Action | Owner | Deadline | Status (Action / Decision / Follow-up).*
>
> *Do not invent, infer, or assume any details not stated in the notes. If something is ambiguous, include it and mark it as NEEDS CLARIFICATION."*

**Review before use:** The "NEEDS CLARIFICATION" flag is a guardrail the model added — keep it. It prevents fabricated owners and deadlines.

---

## Before You Use a Meta-Generated Prompt: Review Checklist

A meta-generated prompt is a first draft, not a final product. Check these five things before you use it:

| Check | Question to ask |
|---|---|
| **Persona** | Does the role match your actual task? Is it specific enough — or too generic? |
| **Audience assumptions** | Has the model assumed an audience (language, culture, literacy level) that doesn't match your community? |
| **Theological guardrails** | Are there guardrails against speculation and hallucination? If not, add them. |
| **Output format** | Is the output format something you can paste directly into your workflow? Adjust if not. |
| **Project-specific terms** | Does the prompt use your actual project's language — your key-term choices, your passage scope, your team's terminology? |

If a prompt passes all five checks, it is ready to use. If not, either steer the model to revise it or edit it yourself directly.

---

## The Upgrade Loop: Combining Meta Prompting with Steering

Meta prompting works well with the iteration loop from Chapter 3. Generate the prompt, then steer it into shape:

> **Turn 1:** *"Write me a prompt for [task description]."*
>
> **Turn 2:** *"Good start. Now add a Chain of Thought reasoning structure with three explicit steps."*
>
> **Turn 3:** *"The persona is too generic. Change it to a consultant working with a shame-honour oral culture in South India."*
>
> **Turn 4:** *"Add a NEEDS VERIFICATION flag instruction and remove the final prose conclusion — output only the table."*

Four turns. A prompt that would have taken 20 minutes to write manually, built in under five — and grounded in your specific project context.

---

*Return to Appendix D: Prompt Template Library → for production-ready templates you can use immediately.*  
*Return to Chapter 2: Anatomy of a Great Prompt → for the building blocks that underpin everything here.*
