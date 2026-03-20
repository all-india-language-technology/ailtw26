# Chapter 1: How LLMs Work — and Why It Matters for Prompting

> **Session tag:** Foundations  
> **Key question:** Why does the exact wording of my prompt change the output so dramatically?

---

**Terms used in this chapter** — plain-language meanings before you encounter them in context:

| Term | What it means in plain language |
|---|---|
| **LLM** (Large Language Model) or **Model** | The type of AI behind ChatGPT, Claude, Gemini, and similar tools — a system trained on vast amounts of text that generates responses by predicting likely next words |
| **Token** | The unit the model counts: roughly one common word, or a fragment of a longer word. Punctuation marks each count as a separate token |
| **Context window** | Everything the AI can "see" at one time: your instructions, the conversation history, and anything you have pasted in |
| **Training data** | The text the model learned from before you started using it — determines its knowledge, vocabulary, and assumptions |
| **Hallucination** | When the model generates confident-sounding content that is factually invented |
| **Knowledge cutoff** | The fixed date beyond which the model has no information — events after that date are invisible to it |
| **System prompt** | Standing instructions loaded before a conversation begins, which shape every response in that session |
| **Attention fade** | The mechanism by which the model gives progressively less weight to older text — meaning instructions set at the start of a session gradually lose influence |
| **Context loss** | When older content (including your guardrails) silently drops out of the context window as a session grows |

Full definitions are in Appendix A (Glossary).

---

## 1.1 What an LLM Actually Does

A Large Language Model (LLM) — the technology behind ChatGPT, Claude, Gemini, and most AI tools you will encounter — does not *understand* text the way a human does. It **predicts** text. More precisely: given everything it has been shown so far (your prompt, the conversation history), it calculates which word is most statistically likely to come next, then the word after that, then the word after that — until it decides to stop.

That is the whole mechanism. Pattern prediction, at extraordinary scale and speed.

### The Scribe Analogy

Imagine a student who copied ten thousand Bible commentaries, lexicons, and theological journals by hand — but never once learned to *read*. They know, from sheer pattern repetition, exactly which words tend to follow which other words in scholarly theological writing. Ask them to complete the sentence *"The Lord is my…"* and they will write *"shepherd"* instantly and correctly — not because they understand Psalm 23, but because that word pair appeared in their copying millions of times.

Ask that same student something rare — a question about a minority language, a newly discovered manuscript, a community practice that was never written down — and they will produce a fluent, confident-sounding completion that may be entirely fabricated. They are not lying. They simply complete patterns. Truth and plausibility feel identical to them.

This is the machine you are prompting. Understanding this changes *everything* about how you write instructions to it.

### Word Embeddings: Words as Positions in Space

LLMs convert words into lists of numbers and store those numbers as points in a vast multi-dimensional space — think of a three-dimensional map but with thousands of dimensions. (This conversion is what the term *word embedding* refers to: each word is "embedded" into the space as a unique numeric position.) Words that frequently appear together in similar contexts end up positioned near each other in that space. *Shepherd, flock, pasture* cluster together. *Lord, holy, temple* form a separate cluster. *Demon, unclean, spirit* gather in another neighborhood.

When you type a prompt, the model geometrically navigates that space — finding the nearest, most statistically coherent next word at each step. It is pure geometry, not comprehension.

**Implication for prompting:** The vocabulary you use in your prompt pulls the model toward specific neighborhoods in that space. Ask for "an explanation" and you will get generic expository prose. Ask for "a consultant's analysis for a checking round" and you pull the model into a completely different cluster of likely outputs — more precise, more structured, more relevant.

### Tokens: What the Model Actually Counts

The model does not process words — it processes **tokens**. A token is a chunk of text, typically a common word or part of a word. *The* = 1 token. *Legion* = 1 token. [*Incomprehensible*](https://platform.openai.com/tokenizer) = 4 tokens (`In` · `com` · `preh` · `ensible`). Every punctuation mark is its own token: a comma, a full stop, a quotation mark each count separately.

This matters for two practical reasons:

**1. Context window size is measured in tokens, not words or pages.** The **context window** is the total amount of text the model can hold in its working memory at one time — everything it can "see" when generating a response, including your instructions, the conversation history, and any documents you have pasted in. A 128,000-token context window holds roughly 90,000–100,000 English words — approximately 350–400 pages of standard text. A 1 Million-token window holds around 700,000–750,000 words — roughly 2,500–3,000 pages. In practice, a long BT working session with pasted source text, back-translations, and AI session brief is unlikely to approach these limits. The practical risk is not raw capacity; it is *behavioural drift* — which is addressed in Chapter 4.

**2. Non-Latin scripts tokenise less efficiently.** Most models were trained predominantly on English text. Scripts like Tamil, Telugu, or Ethiopian Ge'ez may require 2–3 tokens per word rather than one. A session involving a full chapter pasted in a non-Latin script fills the context window significantly faster than the same content in English. If you are working with non-Latin source or draft text, be alert to this.

**One practical implication that surprises many users:** You do not need to say "please" or "thank you" when prompting an AI. Politeness costs tokens and adds no value — the model has no feelings to acknowledge. Keep prompts precise and purposeful.

---

## 1.2 Why Prompting Is Not Obvious

If LLMs simply predict patterns, why isn't prompting just a matter of asking clearly? Because the model has no idea who you are, what you already know, what you will do with the output, or what "good" looks like in your context. Left to its defaults, it aims for the *average* — the statistical center of who tends to ask questions like yours.

For a Bible Translation practitioner, the average is not good enough. The average person asking about Mark 5 wants a Sunday-school summary. You need translation-grade exegetical analysis for a specific cultural audience in a specific output format for a specific use.

Prompting is the act of replacing the model's dangerous defaults with your specific context and requirements. Every technique in this handbook is a different way of doing exactly that.

---

## 1.3 The Factors That Shape Output

The prediction mechanism in section 1.1 is just one part of the picture. What the model actually produces is shaped by nine distinct factors — only four of which are in your hands.

### The nine factors

- **Training data** — the data (text, images, audio, code, and more) the model learned from, which determines its knowledge, vocabulary, and default assumptions
- **Fine-tuning purpose** — the task the model was further trained to specialise in after its initial training; a model fine-tuned for customer service behaves differently from one fine-tuned for coding or instruction-following, even if both started from the same base model
- **Provider configuration** — platform-level settings the tool provider applies before you open the interface; examples include content safety filters, default response length limits, which features are enabled (image generation, web search, file uploads), and acceptable-use policies
- **System prompt** — standing instructions loaded before the conversation begins, either by the tool maker (defining the assistant's default persona, tone, and limits) or by you as the user (via a Claude Project, Custom GPT, or similar setup); shapes every response in the session and, depending on the platform, may or may not be visible to you
- **Knowledge cutoff** — the date beyond which the model has no training data; different models have different cutoffs, and some tools (such as Perplexity or ChatGPT with web search enabled) can supplement this with live retrieval, but the base model's knowledge remains bounded regardless
- **Augmentation data** — documents, databases, or project files you supply to extend the model's knowledge for a specific session (see Chapter 3)
- **Available tools** — operations the model can perform: searching the web, reading files, running calculations, connecting to external systems via integrations
- **Model choice** — which model or tool you select for the task; GPT-4o, Claude Sonnet, Gemini Pro, and others differ in reasoning ability, language coverage, knowledge depth, and cost, and matching the right model to the task is itself a prompting decision
- **Your prompt** — the instruction you write

Of these nine factors, **four are directly in your hands**: *the model* you choose, *a system prompt* you configure yourself, *the augmentation data* you choose to supply, and *the prompt* you write. You cannot change how the model was trained, when its knowledge ends, or how the provider has set up the platform. But you can select the tool best suited to your task, load standing instructions that persist across every session, decide what documents and context you bring in, and craft the prompt that directs the model to use all of it well. Together, these four levers give a practitioner far more control over output quality than most users realise.

Chapter 2 covers how to construct the prompt itself — the lever with the highest immediate impact. Chapter 3 covers how to use augmentation data to extend the model's knowledge for a specific task.

---

## 1.4 The Risk Radar: Six Failure Modes Every BT Practitioner Must Know

These six failure modes are not hypothetical. Each has caused real problems in Bible Translation work. Know them before you trust any AI output.

---

### Failure Mode 1: Hallucination 💥

**What it is:** The model generates text that sounds authoritative but is factually invented — fake verse references, non-existent Louw-Nida domain codes, fabricated quotations from scholars, invented Greek glosses.

**Why it happens:** The model is optimizing for *plausibility*, not truth. When it encounters a question it cannot reliably answer, it does not say "I don't know." It completes the pattern of *what a confident answer to this kind of question looks like*, whether or not the content is real.

**Why it is especially dangerous in BT:** A hallucinated Louw-Nida code looks exactly like a real one. A fabricated scholarly citation looks authoritative. If you do not verify the reference independently, a false claim about the Greek text can enter your checking documentation and survive into publication.

**Prompt that triggers it:**
> *"What does Louw-Nida say about the Greek word akathartos in Mark 5:2?"*

The model may produce a precise-looking domain number and gloss that sounds ready to copy into your notes. Some details may be accurate. Some may be invented. The danger is that a fluent, scholarly answer does not show you which parts are verified and which parts still need checking.

**Safer alternative:**
> *"Explain the semantic range of the Greek word akathartos as used in Mark 5. Do not cite specific reference codes — I will verify those independently. If you are uncertain about any claim, say so explicitly."*

**The rule:** Ask for reasoning and semantic explanation. Verify all specific references (codes, citations, verse counts, Greek forms) against primary sources.

---

### Failure Mode 2: Knowledge Cutoff 📅

**What it is:** The model's training data ends at a fixed date — typically 12–18 months before you are using it. Events, publications, tool updates, and field decisions after that date simply do not exist for the model.

**Why it matters in BT:** New Paratext versions, updated UBS guidelines, recently completed surveys, your team's latest key-term decisions, changes to checking procedures — the model knows nothing of these. It will describe an older state of affairs as if it were current, with no indication that it is out of date.

**Prompt that triggers it:**
> *"What are the latest Paratext 9.5 features I should use for my checking workflow?"*

The model may confabulate features, or describe an older version accurately while presenting it as the current one.

> **Note:** The original draft of this handbook wrote "Paratext 9.4" here — because that was the version in the model's training data at time of writing. The current version is 9.5. This is the failure mode in action.

**Safer alternative:**
> *"I am pasting the Paratext 9.5 release notes below. Based only on this content, summarise the checking features most relevant to a translation team working on a minority language project. [paste notes]"*

**The rule:** For anything time-sensitive, supply the current document and instruct the model to reason *only from what you provide*.

---

### Failure Mode 3: Bias & Worldview 🧭

**What it is:** The model was trained predominantly on Western, English-language internet text. Its default theological frame, cultural illustrations, and metaphors lean Western Protestant. It does not know this about itself.

**Why it matters in BT:** When you ask for a "culturally appropriate illustration," the model's default is the culture embedded in its training data — which may be entirely foreign to your target audience. Illustrations about debt, legal proceedings, or individual conscience may make no sense to a community organized around honour, shame, and kinship obligations.

**Prompt that triggers it:**
> *"Give me a culturally appropriate illustration of 'redemption' for my translation audience."*

Without knowing your audience, the model defaults to Western financial or legal metaphors.

**Safer alternative:**
> *"My target audience is a tribal community in the Nilgiri hills of South India where honour, shame, and kinship obligations are the primary social structures. Suggest 2–3 illustrations for 'redemption' that draw from that social world. Avoid legal or financial metaphors entirely."*

**The rule:** Always anchor the cultural frame explicitly. Name the people group, the honour/shame dynamics, what is *not* familiar in your context. The model cannot correct for bias it does not know it has — you must supply the correction.

**Additional note — low-resource languages:** AI performance degrades significantly for languages with small digital footprints. If your target language has little or no presence in the training data, hallucination risk increases, grammatical suggestions become unreliable, and the model's translations should be treated as first-draft approximations only, not as authoritative renderings. Always have a mother-tongue speaker review any AI output in the target language.

---

### Failure Mode 4: Math & Counting 🔢

**What it is:** LLMs process numbers as tokens, not values. They are statistically unreliable for arithmetic, syllable counts, verse tallying, word frequency analysis, and any task requiring precise numeric reasoning.

**Why it matters in BT:** A wrong verse count, a miscounted syllable in a poetic text, or a misreported key-term frequency can introduce errors into checking documentation that are hard to catch later.

**Prompt that triggers it:**
> *"How many times does the word 'spirit' appear in Mark 5:1–20? Count them for me."*

The model produces a number with full confidence. It is not actually counting. It is predicting what *a plausible word count response looks like* — which often resembles the real answer but is not reliably accurate.

**The safer approach:** Use Paratext's Find function, a spreadsheet, or any reliable counting tool for anything requiring an exact number. Then bring the AI back in to help you *interpret* the pattern — once you have the verified count.

**The rule:** Delegate counting and arithmetic to reliable tools. Delegate interpretation, synthesis, and explanation to the AI.

---

### Failure Mode 5: Attention Fade 🔍

**What it is:** The Transformer architecture that underlies every modern LLM (introduced in the 2017 Google paper *"Attention Is All You Need"*) uses a mechanism called **attention** to decide how much weight to give to each part of the context when generating each new word. The architecture *can* connect any two tokens directly, regardless of distance — this was the breakthrough over earlier systems (see Appendix F). But through training on real-world text, models develop attention patterns that are recency-biased in practice: tokens that are close together tend to receive stronger mutual attention; tokens that are far apart tend to receive progressively weaker attention. This is a learned behavioural tendency, not a structural limitation of the architecture. The further your instructions are from the model's current position in the conversation, the less influence they have on its output — even while they are still technically within the context window.

**Why it matters in BT:** Guardrails and theological constraints are typically set at the top of a session. In a long checking round, those constraints may be competing for attention against dozens of exchanges about specific verses. By the time you reach verse 18, the instruction from verse 1 — *"do not speculate; flag uncertainty"* — has proportionally less influence than it did at the start. The model is not disobeying. It is attending to what is near.

**How it shows up:** Gradual loosening of constraints rather than sudden failure. Speculation increases incrementally. Flags appear less frequently. The persona shifts subtly toward a more generic register. It is harder to spot than context loss (FM6) precisely because there is no clear before-and-after moment.

**The safer approach:** Repeat key constraints at the start of a new task within a session. If you notice the model's behaviour drifting, a single reinforcing line is often enough: *"Reminder: flag all uncertain interpretations as NEEDS VERIFICATION and do not speculate beyond the text."* Better still, use a system prompt (see Chapter 4, §4.4) — system prompt instructions receive elevated attention on every turn, not just when they were written.

**The rule:** Treat important constraints as needing periodic reinforcement in long sessions, not just a one-time setting. See Appendix F for the attention mechanism explained in plain English.

---

### Failure Mode 6: Context Loss 🌊

**What it is:** Every AI conversation has a fixed "context window" — a maximum amount of text the model can hold in its working memory at one time. As a session grows longer, the oldest content is silently dropped to make room for new content. The model does not warn you. From its perspective, it simply does not have access to what has scrolled off. Attention fade (FM5) is the gradual precursor — instructions weaken with distance before they disappear entirely. Context loss is the terminal stage: the instruction is gone from the window completely.

**The silent failure problem:** This is what makes context loss distinctively dangerous. Hallucination can produce an obviously wrong answer. Knowledge cutoff can be spotted if you know the correct version. But context loss produces no signal at all. The model does not know its guardrails have disappeared — it cannot detect an absence. It continues with apparent confidence, operating under fewer constraints than you set, with no indication that anything has changed. The onus for detecting this falls entirely on the human.

**Why it matters in BT:** The guardrails you carefully set at the start of a session — *"do not speculate beyond the text," "flag any uncertain interpretations," "use plain language"* — are written first. They are therefore the first things to disappear as the session grows. After 40 or 50 exchanges, the AI may be operating with no knowledge of those constraints at all.

**How it shows up:** You notice the AI starting to speculate freely, adding theological commentary it was told not to, or changing its output format — mid-session, with no explanation.

**Do modern tools address this?** Some do, partially:
- **System prompts** (Claude Projects, Custom GPTs) load standing instructions in a privileged position *outside* the conversation scroll, so they cannot be displaced by context fill. This is the strongest current defence.
- **Memory features** (ChatGPT Memory, Notion AI) persist facts across sessions — but these are user-curated notes, not full guardrail sets. They reduce re-briefing effort but do not fully solve in-session drift.
- **RAG (Retrieval-Augmented Generation)** environments can re-inject relevant standing context on each turn, keeping instructions fresh regardless of session length — but this requires a configured environment, not a standard chat interface.
- **Standard chat interfaces** (free tiers of Claude, ChatGPT, Gemini) provide no protection. The window fills; the guardrails go. No warning is issued.

**The rule:** Keep sessions short and task-focused. Refresh key instructions mid-session before they fade or fall out. Use a system prompt for standing constraints wherever your tool supports it. See Chapter 4 for the four defences.

---

## 1.5 What AI Does Well: Seven Core Capabilities

The failure modes in section 1.4 define the boundaries. Within those boundaries, AI is genuinely powerful for specific, well-defined tasks. This section maps those capabilities to your work — and introduces you to the habit of improving your prompts, which every chapter in this handbook will continue to develop.

Each capability below is presented first from a **Lane 1 (Translators & Language Workers)** perspective, then extended with examples for Lane 2 and Lane 3. For every capability, you will see two prompts: a weak version and a stronger version. The difference is the lesson.

---

### Capability 1: Summarization

**What it means:** Condensing a large volume of text into a shorter, focused form — retaining what matters, discarding what does not.

**Where it helps Lane 1:** Background research for FIA; making a lengthy commentary or cultural study usable in a drafting session without reading the whole thing.

| | Prompt |
|---|---|
| ✗ Weak | *"Summarise this article about the Decapolis for me."* |
| ✓ Stronger | *"Summarise the following article about the Decapolis region. Focus only on information relevant to a translator preparing to draft Mark 5:1–20. Ignore Roman administrative history. Use plain English. Maximum 150 words. [paste article]"* |

**What improved:** Added a purpose (FIA preparation), a scope filter (relevant to this passage), a negative constraint (ignore Roman admin), a tone rule (plain English), and a length limit. The model now knows not just *what* to summarise, but *why*, *for whom*, and *what not to include*.

**Lane 2 extension:** Summarise the key disagreements in a set of commentaries on a difficult verse, and flag where they agree and where they diverge — for use in a checking discussion.

**Lane 3 extension:** Summarise a 30-page project report into a one-page executive brief, preserving only decisions made and actions required.

---

### Capability 2: Comparison

**What it means:** Placing two or more items side by side and identifying meaningful differences, similarities, and gaps.

**Where it helps Lane 1:** Comparing a draft rendering against a reference translation to surface meaning gaps before a checking round.

| | Prompt |
|---|---|
| ✗ Weak | *"Compare these two versions of Mark 5:6 and tell me if there are differences."* |
| ✓ Stronger | *"Compare Version A and Version B of Mark 5:6 below. Analyse them across these five dimensions and return a table: (1) Points of agreement — what both versions render the same way; (2) Points of disagreement — where they differ and what the difference is; (3) Actions — how each version renders what the man does; (4) Participant references — how each version refers to the man and to Jesus (titles, pronouns, names); (5) Sequence and timeline — whether the order of events is preserved or shifted. Do not guess at translator intent. Flag any dimension where you are uncertain. [paste Version A and Version B]"* |

**What improved:** Replaced a narrow 3-point comparison with a structured 5-dimension framework covering agreement, disagreement, action, participant reference, and sequence. The table format makes the output directly usable in a checking discussion. Naming dimensions explicitly prevents the model from cherry-picking surface differences and missing structural ones.

**Lane 2 extension:** Compare three back-translations of the same verse and label each difference as: theological content / implicit information / naturalness / style choice.

**Lane 3 extension:** Compare two project plans submitted by different teams and identify gaps in scope, timeline, or resourcing.

---

### Capability 3: Data Extraction

**What it means:** Pulling specific pieces of information out of unstructured text — emails, meeting notes, reports — and organising them into a usable format.

**Where it helps Lane 1:** Extracting all occurrences of a key term from a pasted passage for review; pulling action items from workshop notes.

| | Prompt |
|---|---|
| ✗ Weak | *"Find all the divine title terms in this passage."* |
| ✓ Stronger | *"From the pasted Greek interlinear text of Mark 5:1–20 below, extract every term that could be rendered as a divine or supernatural title in translation. For each: quote the original term, note the verse, and give its plain-language semantic range. Do not assign a rendering — only extract and describe. [paste text]"* |

**What improved:** Defined "divine title terms" operationally. Told the model to extract only, not recommend. Added a format expectation (term / verse / semantic range). The guardrail — *only extract and describe* — prevents the model from rushing to a rendering decision before the team is ready.

**Lane 2 extension:** Extract every place in a set of checking notes where an issue was flagged as unresolved, and return them as a prioritised action list.

**Lane 3 extension:** Extract all budget figures from a set of pasted meeting minutes and organise them by project line item.

---

### Capability 4: Classification and Tagging

**What it means:** Sorting items into defined categories — labelling each item against a fixed taxonomy you supply.

**Where it helps Lane 1:** Tagging discourse features across a passage (narrative / dialogue / aside / reported speech); sorting naturalistic checking issues by type.

| | Prompt |
|---|---|
| ✗ Weak | *"Label the types of speech in Mark 5:1–20."* |
| ✓ Stronger | *"Read Mark 5:1–20 (pasted below) and label each verse unit with its discourse function. Use only these four categories: NARRATIVE (third-person description of events), DIALOGUE (direct speech), ASIDE (explanatory comment), REPORTED-SPEECH (speech about speech). If a verse unit could fit two categories, choose the dominant one and note the ambiguity. Return as: Verses | Category | Brief reason. [paste passage]"* |

**What improved:** Supplied a closed taxonomy. Forced a single label per unit to prevent hedging. Asked for brief reasoning so the output can be checked. Without a defined category list, the model invents its own — which is inconsistent and hard to use.

**Lane 2 extension:** Tag every issue in a checking report as: exegetical / lexical / naturalness / cultural / formatting. Use consistently across all passages so patterns can be identified.

**Lane 3 extension:** Classify a list of training requests by urgency (immediate need / next cycle / long-term) and by delivery mode (in-person / self-directed / tool-embedded).

---

### Capability 5: Re-expressing

**What it means:** Taking existing content and rendering it in a different register, format, reading level, or style — without changing the underlying meaning.

**Where it helps Lane 1:** Naturalness work; adjusting a passage from written register to oral/spoken register; adapting a script for different age groups or literacy levels.

| | Prompt |
|---|---|
| ✗ Weak | *"Make this verse sound more natural for our community."* |
| ✓ Stronger | *"Re-express the following draft of Mark 5:15 in a spoken, conversational register appropriate for a primary-school reading level. The current draft sounds like written formal prose. Do not change the meaning or add any interpretation. Flag any phrase where you are uncertain whether the meaning is preserved. [paste draft]"* |

**What improved:** Defined the target register (spoken, conversational), the target reading level (primary school), the constraint (no meaning change), and the error-flagging rule. Without these, "more natural" is interpreted against the model's training default — which may be Western, written, or academic.

**Lane 2 extension:** Re-express a consultant's technical checking note into plain language a mother-tongue translator can act on without a linguistics background.

**Lane 3 extension:** Re-express a technical project update into a donor-friendly summary paragraph with no jargon.

---

### Capability 6: Question Generation

**What it means:** Producing checking questions, comprehension questions, or reflection questions from source material — calibrated to a specific purpose and audience.

**Where it helps Lane 1:** Generating comprehension questions for community testing of a draft; producing self-check questions for a translation team review session.

| | Prompt |
|---|---|
| ✗ Weak | *"Write some checking questions for Mark 5."* |
| ✓ Stronger | *"Write 5 checking questions for Mark 5:1–20 for use in a community comprehension check with oral communicators. Each question must: test observable meaning only (not feeling or interpretation); be answerable from the passage alone; use simple, spoken language; be one sentence. Here is an example of a good question for this passage: 'Where did the man with the evil spirits live?' Write 5 more questions following this exact pattern."* |

**What improved:** Gave a quantity (5), a purpose (community comprehension check), an audience (oral communicators), and four explicit criteria. Added a one-shot example (see Building Block 4, Chapter 2) to lock in style consistency. The result is checking-round ready.

**Lane 2 extension:** Generate a set of key-term checking questions for a consultant to use with a team — questions that surface whether the community understood the semantic weight of a critical term.

**Lane 3 extension:** Generate a set of reflection questions for a post-project review workshop, based on the project's stated objectives.

---

### Capability 7: Drafting from a Specification

**What it means:** Creating new content — a document, a report, a script, a plan — from a structured brief you provide. Distinct from re-expressing (which transforms existing content): drafting starts from a spec.

**Where it helps Lane 1:** Scripting a storyboard from a passage outline; drafting a simple oral introduction for a recording session; creating a team briefing document from a passage summary.

| | Prompt |
|---|---|
| ✗ Weak | *"Write a script for a story recording of Mark 5."* |
| ✓ Stronger | *"Write a storyboard script for Mark 5:1–20 for a local artist creating 6 illustrated panels. For each panel provide: the scene location, the key characters present, the main action visible in the frame, and one short caption (10 words maximum) in plain language. Base the script only on the text — do not add theological interpretation to the captions. Panels should cover: arrival at the shore / encounter with the man / the dialogue with Legion / the pigs / the healing / the sending. [paste the passage for reference]"* |

**What improved:** Gave a panel count (6), a deliverable for each panel (location / characters / action / caption), a caption constraint (10 words), a content guardrail (no theological interpretation), and a coverage outline (6 key scenes). The model now has a complete specification and cannot misunderstand what is needed.

**Lane 2 extension:** Draft a checking report summary from structured notes — including decisions made, issues still open, and recommended follow-up actions.

**Lane 3 extension:** Draft a tool rollout plan from a brief describing the team size, hardware constraints, connectivity, and training objectives.

---

### Connecting Capabilities to Prompting

These seven capabilities are not separate modes — they are what a well-constructed prompt *directs the model to do*. The building blocks in Chapter 2 are the mechanism; the capabilities are what you are aiming at:

| Capability | Key building blocks that unlock it |
|---|---|
| Summarization | Persona, Guardrails (scope filter), Format |
| Comparison | Persona, defined comparison dimensions, Format |
| Data extraction | Guardrails (extract only, do not recommend), Format |
| Classification | Closed taxonomy in the prompt, Format |
| Re-expressing | Target register/audience in Guardrails, Guardrail (no meaning change) |
| Question generation | Few-Shot (one example), explicit criteria, Format |
| Drafting from spec | Format (detailed specification), Guardrails |

Every chapter from here builds the prompting skills that give you reliable control over these capabilities.

---

## 1.6 The Informed Pilot Posture

Everything in this handbook builds toward one operating posture: the **Informed Pilot**.

A pilot does not sit passively while the autopilot flies. They set the parameters, monitor the outputs, intervene when something is wrong, and remain accountable for the flight. They use instruments — they do not guess. They understand what the autopilot can and cannot do.

That is exactly how a BT practitioner should work with AI:

- **Attitude:** Curious and critical. You are not awed by fluent output. You test it.
- **Skills:** You know how to give precise instructions, how to steer when the output drifts, how to recognize a hallucination.
- **Knowledge:** You understand the failure modes, the context window, the data the model does and does not have.

The chapters that follow build each of these. The Risk Radar you have just read is not a reason to distrust AI — it is the foundation of using it competently.

---

*Continue to Chapter 2: Anatomy of a Great Prompt →*
