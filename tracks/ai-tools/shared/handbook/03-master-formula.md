# Chapter 3: The Master Formula

> **Session tag:** Framework  
> **Key question:** Beyond writing a good prompt, what else shapes the quality of AI output?

---

## 3.0 Why the Prompt Alone Is Not Enough

By now you have the tools to write a technically strong prompt — with a persona, guardrails, the right format, and a chain of thought. But you may have noticed that a well-crafted prompt can still produce weak results when something crucial is missing *outside the prompt itself*.

The reason is that the prompt you write is only one of four components that the AI draws on when generating a response. A skilled practitioner manages all four — consciously, every session.

---

## 3.1 The Four Components

```
Strong AI Output = [Instruction] + [Materials] + [Tools] + [Additional Info]
```

Think of this as the full briefing you would give an expert colleague before asking them to start work. The prompt is the instruction — but without documents, access, and standing references, even the best instruction produces guesswork.

---

### Component 1: Instruction

**What it is:** The prompt itself — the role, task, constraints, and output format you craft using the techniques in Chapter 2.

**Weak instruction:**
> *"Explain Mark 5."*

No role. No boundaries. No structure. The model defaults to a general audience and produces a Sunday-school overview.

**Strong instruction:**
> *"Act as a translation consultant. Analyse Mark 5:1–20 for a rural translation team in a shame-honour culture. Do not speculate beyond the text. Return a table: Verse | Cultural Insight | Translation Risk."*

Role + scope + cultural anchoring + constraint + format.

**The most common missing element:** Most practitioners have the task right but omit the format. Specifying output format alone — adding *"return as a table"* or *"return as a numbered checklist"* — often doubles the immediate usability of the output.

---

### Component 2: Materials

**What it is:** The material the model can actually see and reason over — pasted text, uploaded files, and connected project sources. If the relevant text is not present in the conversation, the model fills the gap with statistical guesses.

**No materials — generate a sample translation:**
> *"Act as a translator. Generate a Tamil rendering of Mark 5:1–5 suitable for a rural oral audience."*

The model will produce something. It has seen Tamil text and the Gospel of Mark in training. But it has no knowledge of your project's key-term decisions, your team's style choices, or the renderings your community has already tested. The output is a generic reconstruction — not a step forward in your actual translation.

**With materials — improve the real translation:**
> *"Below is our current Tamil draft of Mark 5:1–5 alongside the ESV source text. Identify three phrases in the draft that could be made more natural for a rural oral audience, and suggest a specific alternative rendering for each.*
>
> *[paste ESV source text]*
> *[paste Tamil draft]"*

Now the model works on your team's real text. Its suggestions engage directly with the choices your translators have already made — and the improvements it proposes are grounded in what is actually on the page.

**Materials you can supply:**

| Source | How to supply it |
|---|---|
| Current draft passage | Paste into the chat |
| Back-translation | Paste alongside the draft |
| ESV / ULT source text | Paste in clearly labelled |
| Team checking notes | Paste or upload as a text file |
| AI session brief / style guide | Upload or paste at session start |
| Key-term decisions | Paste or upload your key-terms CSV |
| Commentary excerpt | Paste the relevant section |

**Rule of thumb:** No source text in the materials = no trustworthy translation output. The model cannot reason accurately over material it cannot see.

---

### Component 3: Tools

**What it is:** Registered capabilities that the AI can call programmatically — operations that go beyond generating text. When a tool is available to the AI, the model does not just produce an answer: it *invokes* the tool, passes the relevant data to it, and works with what the tool returns.

This is a different relationship to tools than "using an app." The AI becomes an orchestrator — deciding which tool is needed, fetching the right data, calling the tool with the right inputs, and assembling the result — all driven by a single prompt.

---

#### Two tiers: chat window vs. connected environments

**Tier 1 — Standard chat interface (where most practitioners are today)**

In a standard chat window (Claude, ChatGPT, Gemini), the AI's built-in tools are limited to what it can do *with text you supply*. You paste a passage; the AI reads, searches, compares, and transforms it. Powerful, but manual: you are the bridge between the AI and your project files.

**Tier 2 — MCP-connected / agentic environments (emerging)**

When tools are registered to the AI via an MCP (Model Context Protocol) server or similar integration, the model gains direct access to external systems. It can *fetch* data it needs without you pasting it, *call* specialist tools and pass them the right inputs, and *chain* multiple operations in a single session.

The clearest way to understand this is to imagine a **Copilot for Paratext**.

---

#### The Paratext Copilot model

A Copilot built on top of Paratext via MCP would give the AI access to your Paratext project as a live data source — and to the specialist tools in your workflow:

| Tool available via MCP | What the AI can do with it |
|---|---|
| **Paratext project files** | Fetch the current draft of any passage directly — no copy-paste required |
| **AQuA** (quality assessment) | Submit a back-translation for automated scoring; retrieve the results as structured data |
| **Whisper** (speech-to-text) | Pass an audio file of a community testing session; receive a transcript |
| **PTXprint** (typesetting) | Generate or modify the configuration file; trigger a typeset run and retrieve the PDF |
| **ElevenLabs** (text-to-speech) | Pass a passage; receive an audio rendering for oral community distribution |

In this environment, a single prompt can orchestrate a multi-step workflow:

> *"Fetch our current draft of Mark 5:1–10 from the project. Call AQuA to score the back-translation against the ULT source. For any verse scoring below 0.7, generate a checking question. Return the results as a table: Verse | Score | Checking Question."*

The AI fetches the text (Read), submits it to AQuA (Execute), interprets the scores (Verify), generates checking questions for weak verses (Transform), and assembles a table (Format) — all without the user touching a file.

---

#### The three tool categories — reframed as agent operations

These categories apply whether you are in a chat window today or a fully connected environment tomorrow. In a chat window, you perform the fetch manually (pasting). In a connected environment, the AI performs the fetch automatically.

| Category | What the AI does | Chat window today | Connected environment |
|---|---|---|---|
| **Read + Search** | Fetch text; find terms, patterns, references | Works on text you paste | Fetches directly from Paratext, Scripture Forge, or a key-term database |
| **Compare + Transform** | Compare versions; reformat into tables, structured data | Compares pasted texts | Compares live project draft against ULT/ESV; outputs to Paratext notes |
| **Execute + Verify** | Call a specialist tool; validate results | Simulates checks within the conversation | Calls AQuA, PTXprint, or Whisper; returns verified structured output |

---

#### BT tools an AI agent can be given access to

| Category | Tool | What it does |
|---|---|---|
| **Text & drafting** | Paratext (SIL) | Primary translation platform — drafts, checking tasks, notes |
| | Scripture Forge | Cloud-based collaborative drafting on Scripture data |
| **Quality & checking** | AQuA (SIL) | AI quality scoring of back-translations against source text |
| | USFM Validator | Syntax checking — catches malformed markers before import |
| **Typesetting** | PTXprint (SIL) | Publication-ready booklets and community Scripture portions |
| | XeLaTeX | Academic typesetter; full Unicode and non-Latin script support |
| **Audio & oral** | Whisper (offline) | Speech-to-text in 100+ languages; runs locally, no internet required |
| | HearThis (SIL) | Chapter-by-chapter audio Scripture recording workflow |
| | ElevenLabs | Text-to-speech; regional voice styles for oral community distribution |
| **Visualisation** | Mermaid | Text-to-diagram; AI writes the syntax, tool renders the image |

> **Data sensitivity note:** *Offline/local* tools (Whisper via LM Studio, PTXprint, XeLaTeX) are safe for unpublished draft text — no data leaves the device. Cloud tools (ElevenLabs, AQuA web, Scripture Forge) should only receive text covered by your organisation's data agreements. See Chapter 4, §4.5 for the full decision rule.

---

### Component 4: Additional Info

**What it is:** Persistent reference documents that should guide *every* AI session on your project — uploaded or pasted at the start of each new chat. This is your stable memory layer.

**The problem it solves:** Without standing references, you repeat the same project briefing in every session. Each new chat starts from zero. Guardrails drift. Key-term choices are forgotten. The model does not know what decisions your team has already made.

**What to include in your Additional Info pack:**

| Document | Contents |
|---|---|
| `ai-session-brief.md` | Project context, target audience, theological guardrails, standing constraints, key decisions (see Chapter 4, §4.3) |
| `key-terms.csv` | Approved renderings for key theological and cultural terms |
| `style-guide.md` | Tone, register, reading level, what to avoid |
| `decision-log.md` | Checking-round decisions that should not be revisited |

**How to use it:** At the start of every new chat session, paste or upload these documents before writing your first prompt. They set the frame for the entire session.

**Longer-term:** In tools that support custom system contexts (Claude Projects, Custom GPTs), these documents can be loaded permanently into the model's starting context, so you do not need to re-upload them each time. See Chapter 4 for details.

---

## 3.2 The Iteration Loop: Conversational Steering

A strong first prompt does not always produce a perfect first output. This is normal and expected. The model's first response is a starting point, not a final product. The skill of *conversational steering* — building on the previous response rather than starting over — multiplies the value of every prompt you write.

### The three-step steering sequence

**Prompt 1 — Initial ask:**
> *"Explain the significance of the pigs in Mark 5 for a translation team."*

Result: well-structured but too academic — full of technical language your team cannot use directly.

**Prompt 2 — Refinement:**
> *"Good start. Now remove the jargon and rewrite this in plain language — 3 sentences maximum."*

Result: simpler and shorter, but still in paragraph form rather than the table format you need.

**Prompt 3 — Final transformation:**
> *"Now format that as a 2-column table: Verse Range | Cultural Insight."*

Result: ready to paste into your checking notes.

### Why this works

Each message builds on the previous context. You are not starting over — the model still has access to everything it said in Prompt 1 and 2. You are placing a specific, targeted correction on top of what it already produced. This is far more efficient than trying to write a perfect first prompt that specifies every nuance.

### Steering language

| Situation | How to steer |
|---|---|
| Output is too long | *"Good. Now reduce this to 3 bullet points maximum."* |
| Output is too generic | *"This is too general. Add specific examples from Mark 5:1–20."* |
| Output used wrong vocabulary | *"Replace all theological jargon with plain English equivalents."* |
| Output missed a key point | *"You didn't address the role of the pigs as a symbol of economic wealth. Add that as a separate point."* |
| Output used the wrong format | *"Reformat this as a table: Insight | Verse Reference | Risk."* |
| Output speculated too freely | *"Remove any speculation. Only state what is supported by the text itself."* |

### When to start a new chat vs continue steering

Continue the same chat when: you are refining the same output toward a final version.

Start a new chat when: you are moving to a different passage, a different task type, or a different topic entirely. Mixing unrelated tasks in one long session creates two problems: earlier instructions (guardrails, persona, format) quietly drop out as the window fills — and earlier conversation about a different task creeps in and skews output for the current one. See Chapter 4 for both effects and how to manage them.

---

## 3.3 Putting the Formula Together: A Full Workflow Example

**Scenario:** A Lane 2 consultant preparing for a checking round on Mark 5:1–20.

**Step 1 — Load Additional Info (session start)**

> *[Paste ai-session-brief.md, key-terms.csv, and style-guide.md into the chat with a brief framing note: "The following documents govern all work in this session."]*

**Step 2 — Instruction + Materials**

> *"Act as a senior translation consultant. Below are three texts: our draft of Mark 5:1–20, the back-translation of the same passage, and the ESV source text. Identify passages where the back-translation diverges from the ESV source in a way that could indicate a translation accuracy issue. [paste all three texts]*
> 
> *Do not speculate. If you are uncertain whether a divergence is significant, flag it as NEEDS VERIFICATION. Return as: Verse | Divergence | Severity (Major/Minor/Flag) | Suggested Checking Question."*

**Step 3 — Review and steer**

Review the output. If several items seem too minor, steer:

> *"Remove all Minor flagged items. Show only Major and Flag items. Add a column: Which Louw-Nida semantic domain is most relevant to each issue? (I will verify the codes myself.)"*

**Step 4 — Extract and save**

Copy the final table into your checking documentation. This is the output of the session — not a draft to prompt further, but a tool-ready deliverable.

---

*Continue to Chapter 4: Advanced Techniques — Managing the Context Window →*
