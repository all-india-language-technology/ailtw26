# Appendix B: Risk Quick Reference
## Six Failure Modes — and How to Guard Against Them

*Keep this as a rapid reference during any AI session. If an output surprises or concerns you, check it against this list first.*

---

## Risk 1: Hallucination 💥

**What it looks like:** The AI produces a Louw-Nida domain code, a Greek lexicon entry, a scholar's quotation, or a verse reference that sounds authoritative but cannot be verified — because it was invented.

**Why it happens:** The model optimises for plausibility, not truth. It completes the *pattern of what a confident scholarly answer looks like*, even when it has no reliable content to draw from.

**High-risk prompt types:**
- *"What does [reference work] say about [Greek word]?"*
- *"Cite the scholarly sources on this interpretation."*
- *"What is the Louw-Nida code for…?"*

**Guardrail to add:**
> *"Do not cite specific reference codes, dictionary entries, or scholar names. Describe the semantic range in plain terms. If you are uncertain about any claim, say so explicitly."*

**Verification rule:** Any specific reference (code, citation, verse number, Greek form) produced by AI must be independently verified against the primary source before it enters your documentation.

---

## Risk 2: Knowledge Cutoff 📅

**What it looks like:** The AI describes an older version of a tool, a superseded guideline, or a pre-existing state of your project as if it were the current situation.

**Why it happens:** Training data ends at a fixed date — typically 12–18 months before you are using the tool. The model has no awareness of what has changed since then.

**High-risk prompt types:**
- *"What are the latest [tool] features for [task]?"*
- *"What does the current UBS checking guideline say about…?"*
- *"Is [specific function] available in Paratext now?"*

**Guardrail to add:**
> *"I am pasting the relevant documentation below. Reason only from what I have provided — do not draw on prior knowledge about this tool or guideline. [paste document]"*

**Rule:** For anything time-sensitive or tool-specific, supply the current document and instruct the model to reason exclusively from what you provide.

---

## Risk 3: Bias & Worldview 🧭

**What it looks like:** The AI produces cultural illustrations, metaphors, or theological framings that are Western Protestant by default — inappropriate for your target audience or culture.

**Why it happens:** Training data is weighted heavily toward Western English-language text. The model does not know it is biased; it presents its defaults as culturally neutral.

**High-risk prompt types:**
- *"Give me a culturally appropriate illustration for [theological concept]."*
- *"How would a person in this community understand [concept]?"*
- Any prompt that leaves cultural context undefined.

**Guardrail to add:**
> *"My target audience is [specific description: people group, honour/shame or guilt/innocence framing, literacy level, economic context]. Use only illustrations and metaphors that would be natural in that cultural world. Avoid Western legal, financial, or individualist metaphors."*

**Low-resource language note:** For languages with little digital presence, hallucination risk increases and grammatical suggestions in the target language are unreliable. Always have a mother-tongue speaker review any AI output in the target language.

---

## Risk 4: Math & Counting 🔢

**What it looks like:** The AI produces a confident, precise-looking number — a verse count, a word frequency, a syllable count — that is wrong.

**Why it happens:** The model processes numbers as tokens, not values. Counting is not pattern-matching; it is arithmetic. The AI predicts *what a plausible answer to a counting question looks like*, which often resembles the real answer but is not reliably accurate.

**High-risk prompt types:**
- *"How many times does [word] appear in [passage]?"*
- *"Count the syllables in this verse."*
- *"How many verses are in this chapter?"*

**The safer approach:**
- Use Paratext's Find function, a spreadsheet, or a manual count for exact numbers.
- Ask AI to *list every occurrence* of a term (then you count) rather than to produce a total.
- Use AI for *interpretation* once you have a verified count.

**Rule:** Delegate counting and arithmetic to reliable tools. Delegate interpretation to AI.

---

## Risk 5: Attention Fade 🔍

**What it looks like:** Constraints set at the start of the session gradually lose their grip. Speculation creeps in. Uncertainty flags appear less often. The persona shifts toward a more generic register. No single clear break — it is a slow drift.

**Why it happens:** The Transformer architecture weights attention by proximity. Instructions written at the top of the session are farther from the model's current position than recent exchanges, so they exert less influence — even while they are still within the context window.

**Warning signs:**
- Guardrails seem to be followed less consistently than at the start
- Speculation and elaboration increase gradually
- Flags and uncertainty markers thin out without instruction
- No clear break point — just a general loosening

**The defence:**

| Action | How |
|---|---|
| **Mid-session refresh** | Paste a reminder: *"Reminder: do not speculate beyond the text. Flag all uncertain items as NEEDS VERIFICATION."* |
| **System Prompt** | Load key constraints as the system prompt — they receive elevated attention on every turn, regardless of session length. |

---

## Risk 6: Context Loss 🌊

**What it looks like:** Mid-session, the AI begins speculating freely, changes its output format, stops flagging uncertain items, or drops the cultural constraints you set at the start — with no warning.

**Why it happens:** The session has grown long enough that the earliest content (your guardrails, persona instruction, AI session brief) has scrolled out of the context window. The model is no longer operating under those constraints because it cannot see them.

**Warning signs:**
- AI starts adding theological commentary it was told not to add
- Uncertainty flags ("NEEDS VERIFICATION") stop appearing
- The output format changes without instruction
- Speculative language increases

**The four defences (in order of ease):**

| Defence | How |
|---|---|
| **Task Chunking** | One task per chat. Start a new chat for each new task type. |
| **Summarise & Restart** | Ask “Summarise all key findings as bullet points,” copy the summary, open a new chat, paste summary + AI session brief. |
| **AI Session Brief** | Paste `ai-session-brief.md` at the start of every new chat session. |
| **System Prompt** | In Claude Projects or Custom GPTs, load the brief as the system prompt — permanently in scope, cannot scroll out. |

---

## Quick Decision Guide

> *"AI just gave me something surprising. What do I do?"*

1. **Is it a specific reference (code, citation, Greek form, verse number)?** → Verify against the primary source before using. Risk: Hallucination.

2. **Is it a claim about a tool or a current process?** → Check the current documentation. Risk: Knowledge Cutoff.

3. **Is it a cultural illustration or metaphor?** → Check whether it actually fits your target audience. Risk: Bias.

4. **Is it a count, frequency, or numeric value?** → Recount with a reliable tool. Risk: Math & Counting.

5. **Are constraints becoming looser gradually — increasing speculation, fewer flags — without a clean break?** → Reinforce key guardrails mid-session or switch to a system prompt. Risk: Attention Fade.

6. **Did the output change character mid-session — dropped guardrails, added speculation?** → Summarise, start a fresh chat, re-paste your brief. Risk: Context Loss.
