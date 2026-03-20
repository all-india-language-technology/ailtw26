# Appendix A: Glossary
## Key AI and Prompting Terms for Bible Translation Practitioners

*Terms are listed alphabetically. Where a term has a specific meaning in prompting practice that differs from its general usage, the prompting meaning is prioritised.*

---

**Additional Info (Master Formula Component 4)**  
The stable reference documents you supply at the start of every AI session — AI session brief, key-term list, style guide, decision log. Unlike context (which comes from your current task), Additional Info travels with you across all sessions and prevents repeated re-briefing.

---

**Automation Bias**  
The tendency to over-trust AI outputs simply because they are produced by a machine and presented in confident, fluent language. The most dangerous form in Bible Translation work: accepting a hallucinated reference because it *sounds* authoritative. Corrective: verify all specific claims independently.

---

**Chain of Thought (CoT)**  
A prompting technique that instructs the model to work through its reasoning step-by-step before arriving at a final answer. Prevents the model skipping to a confident-sounding conclusion without adequate reasoning. Especially important for key-term decisions and back-translation analysis. Activated by instructions like: *"Work through the following steps before answering…"*

---

**Context (Master Formula Component 2)**  
The material the model can actually see and reason over in a given session — pasted text, uploaded documents, connected project sources. Distinct from Additional Info (standing references). If the relevant source text is not in the context, the model fills gaps with statistical guesses.

---

**Context Window**  
The total amount of text an AI model can hold in its working memory at one time. As a session grows longer, older content (including your guardrails and AI session brief) scrolls out of the window silently. The model cannot flag this. One task per chat, the Summarise & Restart technique, and system prompts are all defences against context window overflow. See Chapter 4.

---

**Custom GPT**  
An OpenAI feature that allows a system prompt and uploaded documents to be permanently associated with a specific AI assistant. All chat sessions with that GPT inherit the system prompt, making it a practical way to deploy AI session briefs and guardrails persistently for a team.

---

**Few-Shot Prompting**  
Providing one or more examples of the desired output before asking the model to produce new output. The model learns your team's format, vocabulary, style, and register from the example rather than from an abstract description. One well-chosen example (one-shot) is usually sufficient.

---

**Frontier Model**  
A large, state-of-the-art AI model hosted in the cloud — ChatGPT, Claude, Gemini, and similar. Requires internet access. Most capable for complex research and long-document analysis. Data privacy depends on plan type: free consumer tiers may train on session data; enterprise API plans are private.

---

**Guardrail**  
A negative constraint in a prompt — an explicit instruction about what the model must *not* do. Examples: *"Do not speculate beyond the text," "Do not cite reference codes," "Do not use theological jargon."* Guardrails are essential in BT work to prevent hallucination, doctrinal drift, and inappropriate register. See Chapter 2.3.

---

**Hallucination**  
When an AI model produces content that is confidently stated but factually invented — fake Louw-Nida codes, non-existent scholarly citations, fabricated Greek forms, incorrect verse numbers. Not deliberate deception; the model is completing patterns plausibly rather than accurately. See Appendix B, Risk 1.

---

**Informed Pilot**  
The operating posture taught throughout this handbook: using AI as a capable co-pilot while the human practitioner sets the parameters, monitors outputs, intervenes when something is wrong, and remains accountable for the final product. Contrasted with passive use (accepting all outputs uncritically) and with avoidance (refusing to use AI tools).

---

**Instruction (Master Formula Component 1)**  
The prompt itself — the role, task, constraints, and output format. One of four components in the Master Formula. The most commonly optimised component, but not the only one that matters.

---

**Iteration Loop**  
The practice of treating an AI conversation as a multi-turn refinement process rather than a single question-and-answer exchange. Each follow-up message steers the previous output toward the required result. More efficient than attempting to write a perfect first prompt. See Chapter 3.2.

---

**Knowledge Cutoff**  
The fixed date at which an AI model's training data ends. Events, publications, tool updates, and decisions after that date are invisible to the model. Typically 12–18 months before deployment. Workaround: supply the current document and ask the model to reason only from what you provide. See Appendix B, Risk 2.

---

**LLM (Large Language Model)**  
The technology underlying most modern AI chat tools. A statistical model trained on large amounts of text that predicts likely next words given previous context. Does not understand language in the human sense — predicts plausible completions based on patterns in training data.

---

**Local Model**  
An AI model that runs entirely on your own hardware — no internet connection required. Lower capability than frontier models, but maximum data privacy. Recommended for any task involving unpublished draft text in sensitive or field environments. Primary example in the BT context: LM Studio running an open-source model like Llama or Mistral on a laptop.

---

**MCP (Model Context Protocol)**  
An open standard that allows an AI model to connect to approved external data sources through a server, reducing the need for repeated manual copying and pasting. A filesystem MCP server, for example, lets the AI read approved project files directly from a controlled local folder. Not yet widely deployed in BT-specific tools, but increasingly available in general AI environments.

---

**One-Shot Prompting**  
A form of few-shot prompting using exactly one example. Typically sufficient to establish a consistent format and style for subsequent outputs.

---

**Output Format**  
A building block of prompt construction specifying how the response should be structured — table, checklist, numbered list, prose, JSON, and so on. Specifying format is one of the highest-ROI prompt improvements for practitioners who need output they can use directly without manual reformatting.

---

**Persona / Role Assignment**  
A building block of prompt construction that tells the model who to be for the task — *"Act as a translation consultant"*, *"Act as a biblical scholar"*. Sets vocabulary, expertise level, and default framing. Without a persona, the model defaults to a generic helpful assistant targeting a general audience.

---

**AI Session Brief**  
A short, reusable document — typically one page in markdown format — containing all standing instructions for an AI session: project context, theological guardrails, approved key-term renderings, style rules, and output format defaults. Pasted at the start of every new chat session. The manual precursor to a system prompt. Distinct from the BT *translation project brief* (the foundational document defining audience, purpose, and scope) — though the AI session brief can be generated from it. Template: Chapter 4, §4.3.

---

**RAG (Retrieval-Augmented Generation)**  
A technique in which an AI model retrieves relevant passages from a specified document collection before generating a response — allowing it to answer accurately from your team's own data (previous translations, checked passages, approved glossaries) rather than from generic training data alone. Especially relevant for low-resource languages where the model's training data is sparse.

---

**System Prompt**  
A special instruction layer available in tools like Claude Projects and Custom GPTs. Loaded into the model's context *before* the conversation begins, in a privileged position that does not scroll out of the context window regardless of session length. The strongest defence against context loss. Ideal for team-level deployment where consistent guardrails are required across many sessions and multiple users.

---

**Temperature**  
A setting that controls how creative vs deterministic the model's outputs are. High temperature = more varied, imaginative, sometimes surprising responses. Low temperature = more precise, literal, consistent responses. Most chat interfaces do not expose a slider, but temperature can be steered through language: *"Be precise and literal — do not speculate"* (cold) versus *"Generate 3 creative variations"* (warm). Cold is appropriate for checking, exegesis, and key-term work. Warm is appropriate for creative illustrations and community engagement material.

---

**Token**
The basic unit of text that an AI model processes. Common English words are typically one token each (*the*, *and*, *Lord*); longer or rarer words are split into multiple tokens (*incomprehensible* ≈ 4 tokens). Every punctuation mark — comma, full stop, quotation mark, colon — is its own separate token. The context window, API costs, and model speed are all measured in tokens, not words or pages. As a rough guide: 1,000 tokens ≈ 750 English words ≈ 3 pages of standard text. Non-Latin scripts (Tamil, Telugu, Ge'ez, Hebrew, Greek) typically require 2–3 tokens per word, so non-Latin content fills the context window proportionally faster. Typical frontier model context windows in 2025–2026 range from 128,000 tokens (≈ 380 pages) to 1,000,000+ tokens (≈ 3,000 pages). *Practical note: politeness words like "please" and "thank you" consume tokens and have no effect on output quality — the model has no feelings to acknowledge. Keep prompts purposeful.*

---

**Tools (Master Formula Component 3)**  
Operations the AI can perform *on* context: Read + Search (finding terms and patterns), Compare + Transform (comparing versions, reformatting output), Execute + Verify (running structured checks, validating claims). Distinct from connectors, which determine what data is visible. Tools act on the data that context provides.

---

**Zero-Shot Prompting**  
Asking the model to perform a task without providing any example of the desired output. Produces results calibrated to the model's training-data average rather than your team's specific style. Contrast with few-shot prompting, where one or more examples are provided.
