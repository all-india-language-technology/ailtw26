# Chapter 4: Advanced Techniques — Managing the Context Window

> **Session tag:** Advanced  
> **Key question:** How do I keep my AI sessions reliable when they grow long?

---

## 4.0 The Context Window: Your AI's Working Memory

Every AI conversation sits inside a **context window** — the total amount of text the model can hold in its working memory at one time. Context windows are measured in **tokens** — roughly one common word per token, with punctuation marks each counting as a separate token. To anchor the numbers: a 128,000-token window holds approximately 350–400 pages of standard English text; a 1,000,000-token window holds roughly 2,500–3,000 pages. In practice, most working BT sessions comfortably fit within these limits — the risk is not running out of space, but the subtler problem of *behavioural drift* as the session grows (see below). Note also that non-Latin scripts (Tamil, Telugu, Ge'ez, etc.) tokenise less efficiently — often 2–3 tokens per word — so sessions with non-Latin pasted text fill the window faster than equivalent English content.

There is a deeper mechanism behind drift that is worth understanding. The architecture underlying all modern LLMs — introduced in Google's landmark 2017 paper *"Attention Is All You Need"* — uses a mechanism called **attention** to decide how much weight to give to each token in the context when generating each new word. Tokens that are close together in the conversation receive strong mutual attention; tokens that are far apart receive progressively weaker attention. In practical terms: as your session grows, the guardrails you set at the beginning become not just older — they become *less influential*. The model can technically still see them, but it attends to them with diminishing weight compared to the recent exchanges filling the foreground of the window. This is why drift can begin before anything has literally scrolled off: distance within the context window is itself a form of forgetting.

The model does not flag this. From its perspective, the conversation simply begins at whatever is currently within view. It has no awareness of what has scrolled out — and no ability to tell you that something important has been lost. This is the defining characteristic of context loss as a failure mode: the model cannot detect an absence, so it produces no warning. The full discussion of why this makes it distinctively dangerous is in Chapter 1, §1.4 (Failure Mode 6).

### Why this matters for BT sessions

Your guardrails, role instructions, and AI session brief are written at the very *start* of a session. They are therefore the *first things* to scroll out of the window as the session grows.

A session that began with *"Do not speculate beyond the text — flag all uncertain interpretations as NEEDS VERIFICATION"* may, after 40–50 exchanges, be operating with that instruction entirely out of scope. The model will begin speculating freely, not because it is misbehaving, but because it genuinely cannot see the instruction anymore.

This is not a failure of the tool. It is the expected behaviour — and it is your responsibility to manage it.

### The three stages of a session

| Stage | What is happening | Risk level |
|---|---|---|
| **Session start** | All instructions, brief, and guardrails are in scope | Low |
| **Mid-session** | Context filling; older content approaching the edge | Medium |
| **Overflow** | Earliest content (your guardrails) silently dropped | High — silent rule-breaking |

---

## 4.1 Defence 1: Task Chunking

**The principle:** One task per chat. Never mix unrelated work in a single long session.

A session that covers exegesis of Mark 5, then back-translation review, then key-term analysis, then formatting a report — over two hours — will be unreliable by the end. The constraints you set for exegesis work may not apply to the formatting task, and vice versa. Cross-contamination of instructions is as dangerous as context loss.

**Practice:**
- Exegesis session → one chat
- Back-translation review → separate chat
- Administrative summary → separate chat

Starting a new chat costs you nothing. A fresh chat starts with a full, clean context window ready for your brief. The habit of *one chat per task* is the single most impactful change most practitioners can make to improve the reliability of their AI work.

**One critical step:** A new chat is blank. The AI has no memory of previous sessions by default — it does not know your project, your guardrails, your key-term decisions, or what was decided last week. Before typing your first prompt in any new session, paste your AI Session Brief and (if continuing from a prior session) a summary of where you left off. Skip this step and you are briefing a stranger who has never heard of your project. Defence 3 (the AI Session Brief) exists precisely to make this re-injection fast and consistent.

---

## 4.2 Defence 2: Summarise and Restart

**The principle:** When a session grows long, ask the model to summarise what was decided, then carry that summary into a fresh chat.

**How to do it:**

When you notice a session becoming long, ask:
> *"Summarise all key findings and decisions from this session as a compact bullet-point list. Include any items flagged as NEEDS VERIFICATION."*

Copy the summary. Open a new chat. Paste the summary along with your AI session brief as the opening context. Continue from where you left off — but with a full, clean window.

This takes about 90 seconds and completely resets the context. The new session begins with the decisions intact and the guardrails fully in scope.

**When to do it:** Length alone is a poor trigger — modern frontier models handle context windows of 128,000 tokens or more, and even a long conversation rarely approaches that limit through text exchange alone. The real trigger is *behavioural drift*: the model stops following your format, starts speculating when it was told not to, changes register, or produces output that no longer matches the constraints you set at the start. When you notice any of these, the session has drifted and a summarise-and-restart will reset it cleanly. A second trigger is document volume: if you have pasted multiple large texts (source passage, back-translation, key-term list, AI session brief) in a single session, the window fills faster than conversation alone — consider restarting when you are about to add a large paste to an already substantial session.

---

## 4.3 Defence 3: Keep an AI Session Brief

**A note on terminology:** In Bible Translation, *project brief* already has a specific meaning — the foundational document that defines the translation's purpose, target audience, and scope. That is not what this section is describing. The document here is an **AI Session Brief**: a short, structured file you paste at the start of every AI chat to orient the model to your project. The two documents are related but distinct.

**The good news:** You do not need to create this from scratch. Your existing translation project brief already contains most of what the AI needs. A useful first step is to ask the AI to help you convert it:

> *"Below is our translation project brief. Extract from it a compact AI session brief covering: project context, theological guardrails, key-term decisions so far, style rules, and output format defaults. Structure it so I can paste it at the start of every AI session."*

Then review and supplement the result with any AI-specific instructions (output format defaults, uncertainty flags, etc.) that are not in the original brief.

**The principle:** Maintain a single `ai-session-brief.md` file that contains everything the model needs to know about your project and your standing rules. Paste or upload it at the start of *every* new chat session.

**What goes in an AI Session Brief:**

```markdown
# AI Session Brief — [Project Name]

## Project context
- Target language: [name]
- Target audience: [description — literacy level, cultural framing, etc.]
- Current phase: [FIA / Drafting / Checking / etc.]

## Theological guardrails
- Do not speculate beyond what the source text states
- Flag any uncertain interpretation as: NEEDS VERIFICATION
- Do not paraphrase or reword source text quotations
- Do not add theological commentary not present in the source

## Key-term decisions
- [Term] → [Approved rendering]
- [Term] → [Approved rendering]

## Style rules
- Reading level: [primary school / secondary / expert]
- Register: [formal / conversational / plain]
- Avoid: [specific vocabulary or framing to avoid]

## Output format defaults
- Tables use: Issue | Verse | Suggestion
- Flag unchecked items as: NEEDS VERIFICATION
```

**The brief costs you three minutes to write once — or a few minutes to generate from your existing translation brief. It saves you re-briefing at the start of every session and prevents the silent erosion of constraints that happens when you rely on memory alone.**

Keep this file where you can find it quickly — a desktop shortcut, a pinned Notion page, a printed card. The faster you can paste it, the more consistently you will use it.

---

## 4.4 Defence 4: Use a System Prompt

**The principle:** In tools that support it, move your standing instructions into a **system prompt** — a special instruction layer that sits *outside* the conversation scroll and is always visible to the model, regardless of session length.

### What is a system prompt?

In a standard chat, all content — your instructions, the model's responses, your follow-ups — occupies the same scrolling context window. When the window fills, the oldest content goes.

A system prompt is different. It is loaded into the model's context *before* the conversation begins, in a privileged position that does not scroll. Your guardrails and AI session brief placed in the system prompt are permanently in scope — the context window filling up cannot touch them.

### Where to find system prompts

| Tool | How to set a system prompt |
|---|---|
| **Claude Projects** | Create a new Project; add instructions in the Project Instructions field. All chats within the Project inherit those instructions. |
| **Custom GPTs (OpenAI)** | In the GPT editor, add instructions in the System field. All chats with that GPT use those instructions. |
| **Chipp.ai** | Custom agent system prompt field. |
| **API access** | The `system` parameter in the request. |

### For Lane 3 practitioners

System prompts are the strongest defence for team-level and production use. If your translation team runs multiple checking sessions per week, creating a project-specific Custom GPT or Claude Project — with the AI Session Brief, key-term list, and theological guardrails loaded as the system prompt — means every team member starts every session with fully correct constraints, without needing to copy and paste anything.

This is the architectural upgrade from individual best-practice to team-level reliability.

---

## 4.5 The AI Ecosystem: Choosing the Right Tool

### Not all AI is the same — and data sensitivity matters

The five-building-block prompting skills in this handbook apply across all major AI tools. But which tool you use for a given task depends on two factors: **capability** and **data sensitivity**.

| Tool type | Best for | Data sensitivity |
|---|---|---|
| **Frontier cloud models** (ChatGPT, Claude, Gemini — paid/enterprise) | Deep research, complex exegesis, long-document analysis | Enterprise API plans: private. Free consumer tiers: may train on your data. |
| **Local models** (LM Studio on your laptop) | Any task involving unpublished draft text in the field | Highest privacy — model runs entirely on your device, no internet required |
| **Specialist BT tools** (Scripture Forge, Faithbridge, AQuA) | Workflow-integrated tasks (drafting, FIA, quality checking) | Covered by your organization's data agreements |

### The data-sensitivity decision rule

A simple question determines which tool to use:

> **"Is this draft text published?"**
> - Yes → cloud tools are acceptable
> - No → use a local model (LM Studio) or an enterprise-licensed API only

**Never paste unpublished, sensitive, or community-private draft text into a free consumer chat interface.** Free tiers of ChatGPT, Gemini, and similar tools may use session data for model training. Treat them like a public forum: do not share anything you would not publish openly.

> **Beyond these guidelines:** The decision rule above is a practical baseline. Teams should also check with their own IT and administration teams — many organisations have their own data handling policies, approved tool lists, and acceptable-use guidelines that may be stricter than the baseline here. If your organisation has such policies, follow them. If it does not, treat this decision rule as the floor, not the ceiling.

---

*Continue to Chapter 5: Prompting by Lane →*
