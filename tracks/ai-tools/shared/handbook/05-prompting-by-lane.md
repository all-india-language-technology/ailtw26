# Chapter 5: Prompting by Lane

> **Session tag:** Application  
> **Key question:** How do I apply everything I have learned to my specific role and tasks?

---

## How to Use This Chapter

This chapter works through the full set of prompting techniques applied to realistic scenarios for each of the three lanes. Each section is self-contained — you can jump directly to your lane and work through the examples, or read all three to understand how the same technique plays out differently across roles.

Each scenario follows the same structure:
1. **The task** — what you are trying to accomplish
2. **The weak prompt** — what most people type first
3. **The strong prompt** — the upgraded version with building blocks labelled
4. **What changed** — a brief explanation of the key moves

---

## 5.1 Lane 1 — Translation & Language Practitioners

*Mother Tongue Translators · Translators · Linguists · Literacy Workers*

### Scenario A: Cultural and Historical Background (FIA Support)

**The task:** Before drafting Mark 5:1–20, you need to understand the cultural and historical background of the pigs in the story — specifically how this would affect translation for an audience where pigs are an important wealth symbol.

**Weak prompt:**
> *"Tell me about pigs in the Bible."*

This gives you a general survey of pig references across the Old and New Testaments. Not wrong — but not targeted to your task, your audience, or your passage.

**Strong prompt:**
> *"Act as a biblical scholar specialised in Second Temple Judaism and Mediterranean economics. [Persona]*
> 
> *Explain the cultural and economic significance of pigs in Mark 5:1–20 for a translation team working with a community where pigs represent significant household wealth. Focus on: (1) what the pig herd would have meant to the local economy, (2) what cultural weight the destruction of the herd carries, (3) why that detail matters for how the passage will be received by a community that prizes pigs. [Task + cultural anchor]*
> 
> *Use plain English. Do not speculate beyond what the text and historical record support. Do not cite specific reference codes — I will verify those independently. [Guardrails]*
> 
> *Return as 3 numbered paragraphs, one per focus point above. Maximum 80 words each. [Format]"*

**What changed:** Persona grounds the language. The three focus points create structure before the output is generated. The cultural anchor ("community where pigs represent wealth") pulls the response toward the actual translation challenge. Guardrails prevent fabricated citations. Format prevents a sprawling essay.

---

### Scenario B: Naturalness Check

**The task:** You have a draft of Mark 5:3–5 and want to identify phrasings that sound unnatural to a native speaker of your target language.

**Weak prompt:**
> *"Check if this translation is natural."*

Without the draft, the model cannot help at all. Even with the draft pasted in, "natural" is undefined — natural *for whom?*

**Strong prompt:**
> *"Act as a mother-tongue speaker of [language name] hearing this passage for the first time as spoken narrative — not as written text. [Persona]*
> 
> *Below is a draft rendering of Mark 5:3–5. [paste draft]*
> 
> *Identify up to 3 phrases that would sound unnatural, awkward, or overly formal to an oral listener. For each phrase: quote it exactly, explain what sounds wrong, and suggest a more natural alternative. [Task]*
> 
> *Do not change the meaning of any phrase — only adjust for naturalness. Flag any suggestion you are uncertain about. [Guardrails]*
> 
> *Return as: Phrase | Problem | Suggested Alternative. [Format]"*

**What changed:** The persona is an *oral listener*, not a written-language proofreader — which is the correct frame for spoken naturalness. The task is bounded to 3 items. The meaning-preservation constraint prevents the model from "improving" the translation beyond what you asked.

---

### Scenario C: Storyboard Scripting for Oral / Literacy Contexts

**The task:** You want an AI-scripted storyboard for Mark 5:1–20 to brief a local illustrator on a 6-panel stick-figure series for oral community engagement.

**The common mistake:** Many practitioners try to ask AI to *draw* something. Text-based AI cannot generate images. But it can script a storyboard with precision that a human artist can follow exactly.

**Strong prompt:**
> *"For Mark 5:1–20, create a detailed storyboard script for a local artist to use as a brief for a 6-panel stick-figure illustration series. [Task]*
> 
> *For each panel provide: (1) the setting, (2) the key characters present, (3) the main action, (4) one short caption in plain language (maximum 10 words). [Format]*
> 
> *Capture the key narrative movements in sequence: arrival by boat, encounter at the tombs, dialogue with Legion, the pigs, the healed man, and the sending. [Content scope]*
> 
> *Do not add theological interpretation to the captions — describe only what can be seen. [Guardrail]"*

**What changed:** The task is correctly scoped as *scripting*, not drawing. The 6-panel structure and the 4-part per-panel format are defined before the model begins. The narrative scope ensures all major movements are represented. Guardrail keeps captions visual rather than interpretive.

---

## 5.2 Lane 2 — Consultants & Advisors

*Translation Consultants · Consultants in Training · Exegetes · Translation Advisors*

### Scenario A: Comparative Analysis — Draft vs Source

**The task:** You have two renderings of Mark 5:9 — the team's draft and the KJV — and want a structured consultant-grade comparison.

**Weak prompt:**
> *"Compare this verse with the KJV and tell me if there are any issues."*

"Issues" is undefined. The model will produce a generic literary comparison that misses translation-accuracy problems entirely.

**Strong prompt:**
> *"Act as a translation consultant conducting a formal checking review. [Persona]*
> 
> *Below are two renderings of Mark 5:9: [paste draft] and [paste KJV].*
> 
> *Identify differences in: (1) theological content, (2) implicit information, (3) natural discourse structure. [Task with defined categories]*
> 
> *For each difference, assess: is this a significant translation issue, an acceptable variation, or a style choice? [Evaluation criteria]*
> 
> *Do not resolve uncertain items — flag them as NEEDS VERIFICATION. [Guardrail]*
> 
> *Return as: Difference | Category | Assessment | Flag. [Format]"*

**What changed:** The three comparison categories (theological content, implicit information, discourse structure) define what "issues" means operationally — the model cannot default to a generic literary comparison. The evaluation criteria distinguish significance levels. The uncertainty guardrail prevents confident-sounding verdicts on genuinely debatable points.

---

### Scenario B: Key-Term Analysis with Chain of Thought

**The task:** Identifying key terms in Mark 5:1–20 that carry significant translation risk.

**Strong prompt (using CoT):**
> *"Act as a translation consultant with expertise in New Testament Greek semantics. [Persona]*
> 
> *From Mark 5:1–20 (ESV text below), work through the following steps before producing your output: [Chain of Thought]*
> 
> *Step 1 — Identify all theologically significant terms: defined as words whose precise rendering will significantly affect doctrinal understanding in translation.*
> 
> *Step 2 — For each term: describe its semantic range in plain language (do not fabricate Greek dictionary codes — I will verify those independently).*
> 
> *Step 3 — For each term: identify the translation risk if the term is rendered too narrowly vs too broadly.*
> 
> *Step 4 — Suggest one checking question for each term that a translation team could use to verify the rendering.*
> 
> *[paste ESV text]*
> 
> *Do not speculate. Flag uncertain items as NEEDS VERIFICATION. [Guardrail]*
> 
> *Return as: Term | Semantic Range | Narrowing Risk | Broadening Risk | Checking Question. [Format]"*

**What changed:** The four-step chain of thought forces the model to reason through all analytical layers before producing any output. This prevents the most common failure: jumping to a translation recommendation without adequately characterising the term's range. The checking-question column transforms the output into a directly usable tool, not just a report.

---

### Scenario C: Back-Translation Review

**The task:** Reviewing a back-translation for implicit information gaps.

**Strong prompt:**
> *"Act as a senior translation consultant. [Persona]*
> 
> *Below are three texts for Mark 5:1–20: the ESV source text, the current draft, and the back-translation of the draft. [paste all three, clearly labelled]*
> 
> *Step 1 — Compare the back-translation to the ESV source. Identify any place where information present in the ESV source is absent from or weakened in the back-translation. [CoT Step 1]*
> 
> *Step 2 — For each gap identified, assess whether the gap is: (a) an implicit-information issue in the draft, (b) a back-translation accuracy issue, or (c) both. [CoT Step 2]*
> 
> *Step 3 — For each gap, suggest a specific checking question the consultant could use with the translation team to surface the issue. [CoT Step 3]*
> 
> *Do not flag minor stylistic variations. Focus only on meaning gaps. Do not speculate about intent. [Guardrail]*
> 
> *Return as: Verse | Gap Description | Type (a/b/both) | Checking Question. [Format]"*

---

## 5.3 Lane 3 — Leadership & Technical Enablers

*Cluster Managers · Project Executives · IT Support · Facilitators · Software QA*

### Scenario A: Meeting Notes → Action List

**The task:** You have 5 emails from this week and need a structured action list extracted from them.

**Weak prompt:**
> *"Look through my emails and prepare a to-do list for me."*

The AI has no access to your inbox. It cannot read emails you have not given it. This prompt produces a confused refusal or a generic template.

**Strong prompt:**
> *"I am pasting 5 emails from this week below. [Context]*
> 
> *For each email, identify: (1) any action required from me, (2) the deadline if mentioned, (3) who else is involved. [Task]*
> 
> *Ignore greetings, signatures, and social pleasantries — extract only actionable content. [Guardrail]*
> 
> *Return as a markdown checklist table: Action | Owner | Deadline | Waiting On. [Format]*
> 
> *[paste all 5 emails, each clearly labelled with its sender and date]"*

**What changed:** The data is supplied. The extraction categories are defined. The guardrail prevents the model from over-processing social content. The table format produces a deliverable that can be pasted into any project management tool immediately.

---

### Scenario B: Governance Report from Raw Notes

**The task:** Converting a cluster manager's handwritten session notes into a formal governance report.

**Strong prompt (using Few-Shot):**
> *"Act as a project manager writing a formal governance report for a non-technical executive audience. [Persona]*
> 
> *Here is an example of the report format we use for this project: [Few-Shot example — paste one previous report entry] [Example]*
> 
> *Now convert the following session notes into the same format. [Task]*
> 
> *[paste raw notes]*
> 
> *Do not insert information not present in the notes. Do not use technical jargon. [Guardrail]*
> 
> *Return in the same section structure as the example report above. [Format]"*

**What changed:** Few-shot learning replaces the need to describe the report format in abstract terms. One previous report entry communicates the structure, vocabulary, and register more precisely than a paragraph of description.

---

### Scenario C: Rollout Readiness Checklist

**The task:** You are preparing to introduce a new AI tool to a field translation team and need a rollout readiness checklist.

**Strong prompt:**
> *"Act as a deployment project manager in a field technology context. [Persona]*
> 
> *I am preparing to introduce [tool name] to a translation team of 12 people in a low-bandwidth environment. Hardware: i5 laptops, 16GB RAM, no dedicated GPU. Internet: intermittent 3G. Team profile: experienced with Paratext, new to AI tools. [Context]*
> 
> *Generate a rollout readiness checklist covering: (1) pre-deployment infrastructure checks, (2) team training requirements, (3) first-session facilitation plan, (4) risk flags specific to low-bandwidth deployment, (5) success criteria for a 30-day pilot. [Task with structure]*
> 
> *Do not recommend steps that require dedicated GPU or stable broadband — all suggestions must be feasible within the hardware constraints above. [Guardrail]*
> 
> *Return as a numbered checklist grouped by the 5 sections above. [Format]"*

---

## 5.4 Cross-Lane Exercises

The following exercises are designed for use in cross-lane pairs — one participant from Lane 1 or 2, one from Lane 3:

1. **Swap prompts:** Each person shows their strongest prompt from today's lab to their cross-lane partner. Can their partner understand what the prompt is trying to accomplish without explanation? If not, what is unclear?

2. **Translate the output:** Take a Lane 2 checking output (a formatted table of translation issues) and ask Lane 3: "How would you present this to a project executive who is not a translation specialist?" Build a new prompt together.

3. **Build a shared brief:** What would an `ai-session-brief.md` look like that is useful to both a translator and a project manager working on the same project? Draft one together in 10 minutes.

---

*Continue to the Appendices →*
