# Appendix D: Prompt Template Library
## Production-Ready Templates — Copy, Adapt, Use

*These templates are structured starting points. Replace bracketed placeholders with your specific content. Do not use them verbatim — adapt the persona, context, and guardrails to your actual task.*

---

## How to Use These Templates

Each template is labelled with:
- **Lane** — which role it is designed for
- **Task type** — what workflow stage it supports
- **Key techniques** — which building blocks it uses (P = Persona, F = Format, G = Guardrails, FS = Few-Shot, CoT = Chain of Thought)

---

## Template 1 — Cultural Background Research

**Lane:** 1 · **Task:** FIA preparation · **Techniques:** P + G + F

```
Act as a [biblical scholar / cultural anthropologist / historian of Second Temple Judaism] 
specialised in [relevant region / period / culture].

Explain the [specific cultural or historical element] in [exact passage reference] 
for a translation team working with [target audience description — 
e.g. "a shame-honour community in East Africa where pigs represent household wealth"].

Focus specifically on: 
1. [First aspect of cultural significance]
2. [Second aspect]
3. [How this affects how a target community will receive the passage]

Use plain English. Do not speculate beyond what the text and historical record support. 
Do not cite specific reference codes — I will verify those independently. 
Maximum [word count] words.

Return as [3 numbered paragraphs / a table: Aspect | Explanation | Translation Implication].
```

---

## Template 2 — Naturalness Check

**Lane:** 1 · **Task:** Draft review · **Techniques:** P + G + F

```
Act as a mother-tongue speaker of [language name] hearing this passage 
as spoken narrative for the first time — not as written text.

Below is a draft rendering of [passage reference]:
[paste draft here]

Identify up to [3–5] phrases that would sound unnatural, awkward, 
or overly formal to an oral listener.

For each phrase:
- Quote it exactly
- Explain what sounds wrong
- Suggest a more natural alternative

Do not change the meaning of any phrase — only adjust for naturalness. 
Flag any suggestion you are uncertain about.

Return as: Phrase | Problem | Suggested Alternative.
```

---

## Template 3 — Comparative Rendering Analysis

**Lane:** 2 · **Task:** Checking round · **Techniques:** P + CoT + G + F

```
Act as a translation consultant conducting a formal checking review.

Below are two renderings of [passage reference]:

DRAFT: [paste draft]
REFERENCE ([version name]): [paste reference text]

Work through the following steps before producing your output:

Step 1 — Identify all differences between the two renderings.
Step 2 — For each difference, categorise it as: 
  (a) theological content, (b) implicit information, or (c) discourse structure.
Step 3 — For each difference, assess: 
  significant issue / acceptable variation / style choice.

Do not speculate about translator intent. 
Flag uncertain assessments as NEEDS VERIFICATION.

Return as: Verse | Difference | Category | Assessment | Flag.
```

---

## Template 4 — Key-Term Analysis

**Lane:** 2 · **Task:** Key-term decisions · **Techniques:** P + CoT + G + F

```
Act as a translation consultant with expertise in New Testament Greek semantics.

From [passage reference] (source text below), 
identify theologically significant terms — defined as words whose precise rendering 
will significantly affect doctrinal understanding in translation.

Work through these steps for each term:

Step 1 — Describe the term's semantic range in plain language 
  (do not cite specific Louw-Nida codes — I will verify independently).
Step 2 — Identify the translation risk if the term is rendered too narrowly.
Step 3 — Identify the translation risk if the term is rendered too broadly.
Step 4 — Suggest one checking question the translation team could use 
  to verify the rendering with the community.

Do not fabricate reference codes or scholarly citations. 
Mark uncertain items as NEEDS VERIFICATION.

[paste source text]

Return as: Term | Semantic Range | Narrowing Risk | Broadening Risk | Checking Question.
```

---

## Template 5 — Back-Translation Review

**Lane:** 2 · **Task:** Checking round · **Techniques:** P + CoT + G + F

```
Act as a senior translation consultant.

I am providing three texts for [passage reference]:

SOURCE TEXT (ESV): [paste]
CURRENT DRAFT: [paste]
BACK-TRANSLATION OF DRAFT: [paste]

Work through the following steps:

Step 1 — Compare the back-translation to the ESV source. 
  Identify any place where content present in the ESV source 
  is absent from or weakened in the back-translation.

Step 2 — For each gap, assess: 
  (a) draft issue, (b) back-translation accuracy issue, or (c) both.

Step 3 — Suggest one specific checking question per gap 
  that the consultant could use with the translation team to surface the issue.

Do not flag minor stylistic variations — focus only on meaning gaps. 
Do not speculate about translator intent. 
Flag uncertain assessments as NEEDS VERIFICATION.

Return as: Verse | Gap Description | Type (a/b/both) | Checking Question.
```

---

## Template 6 — Chain of Thought Rendering Decision

**Lane:** 2 · **Task:** Difficult key-term · **Techniques:** P + CoT + G + F

```
Act as a senior translation consultant.

I need to decide how to render the term "[term]" in [passage reference] 
for a [target audience description] translation.

Work through these steps before making a recommendation:

Step 1 — What did "[term]" communicate to a first-century reader 
  (cultural weight, connotations, emotional impact)?

Step 2 — What does the use of this specific term communicate 
  theologically and narratively in this passage?

Step 3 — What concept in [target language / culture] 
  communicates [brief description of the required meaning]?

Only after completing all three steps, suggest 2–3 translation options 
with your reasoning for each.

Flag any step where you are uncertain. 
Do not speculate beyond what the text supports.

Return: Step-by-step reasoning, then a final Options section formatted as: 
Option | Meaning conveyed | Advantage | Risk.
```

---

## Template 7 — Administrative Action Extraction

**Lane:** C · **Task:** Meeting / email processing · **Techniques:** P + F + G

```
Act as a project coordinator extracting action items from communication records.

I am pasting [number] [emails / meeting notes] below, 
each labelled with sender/date or meeting name/date.

For each item in the source material, identify:
1. Any action required from me or my team
2. The deadline if mentioned (use "Unspecified" if not stated)
3. The owner (person responsible)
4. Any dependencies or waiting-on items

Ignore greetings, pleasantries, background context, and information-only content. 
Extract only actionable items.

[paste all source material, clearly labelled]

Return as a markdown checklist table: 
☐ Action | Owner | Deadline | Waiting On.
```

---

## Template 8 — Governance Report from Raw Notes

**Lane:** C · **Task:** Reporting · **Techniques:** P + FS + G + F

```
Act as a project manager writing a formal governance report 
for a non-technical executive audience.

Here is an example report entry from a previous session that matches 
the format and tone we use:
[paste one example report section / paragraph]

Now convert the following session notes into the same format and tone.

[paste raw notes]

Do not insert information not present in the notes. 
Do not use technical jargon — translate all technical terms into plain language. 
Match the section headings and structure of the example above.
```

---

## Template 9 — AI Session Brief (Reusable Session Starter)

**Lane:** All · **Task:** Session initialisation · **Purpose:** Paste at the start of every new AI chat session

```markdown
# AI Session Brief — [Project Name]

## Session instruction
You are assisting [role / name] with Bible translation work.
Follow all rules in this brief for the entire session.

## Project context
- Target language: [name and ISO code if known]
- Target audience: [description — literacy, cultural frame, oral/literate]
- Translation phase: [FIA / Drafting / Checking / Review]
- Source text version: [ESV / ULT / other]

## Theological guardrails (standing — apply to all outputs)
- Do not speculate beyond what the source text states
- Flag all uncertain interpretations as: NEEDS VERIFICATION
- Do not paraphrase or alter source text quotations
- Do not add theological commentary not present in the source
- Do not fabricate reference codes, citations, or Greek forms

## Key-term decisions
- [Term] → approved rendering: [rendering]
- [Term] → approved rendering: [rendering]
- [add as needed]

## Style defaults
- Reading level: [primary / secondary / expert]
- Register: [formal / plain / oral-conversational]
- Avoid: [specific vocabulary, framing, or cultural references to avoid]

## Output format defaults
- Tables use columns: [define your standard columns]
- Uncertain items flagged as: NEEDS VERIFICATION
- Maximum response length (unless specified): [word count or page limit]
```

---

## Template 10 — Rollout Readiness Checklist

**Lane:** C · **Task:** Tool deployment · **Techniques:** P + G + F

```
Act as a deployment project manager in a field technology context.

I am preparing to introduce [tool name] to a translation team.

Team profile:
- Team size: [number] people
- Hardware: [spec — e.g. i5 laptops, 16GB RAM, no dedicated GPU]
- Connectivity: [e.g. intermittent 3G, satellite, broadband]
- Tool familiarity: [experienced with / new to specific tools]
- AI experience: [none / basic / intermediate]

Generate a rollout readiness checklist covering:
1. Pre-deployment infrastructure and access checks
2. Team training requirements (content and duration)
3. First-session facilitation plan
4. Risk flags specific to this deployment context
5. Success criteria for a 30-day pilot

All recommendations must be feasible within the hardware and connectivity 
constraints stated above. Do not recommend steps requiring [excluded requirements].

Return as a numbered checklist grouped by the 5 sections above.
```
