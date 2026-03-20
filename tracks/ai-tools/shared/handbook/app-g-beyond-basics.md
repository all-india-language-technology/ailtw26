# Appendix G: Beyond the Basics — Expanding Your Practice
## Topics for Further Exploration After the Workshop

*This appendix is not required for the workshop sessions. It is a signpost — a guided orientation to the territory that lies beyond the core techniques in Chapters 1–5. Each section is a starting point, not a complete guide. Use it when you are ready to go deeper.*

---

## G.1 Prompting in Regional and Minority Languages

The quality of AI output degrades significantly when you move away from English and other high-resource languages. This is not a bug to be fixed by a better prompt — it is a data problem baked into how these models were trained.

**Why it happens:** Every major AI model was trained predominantly on English text — with substantial representation of French, German, Spanish, and Chinese, and progressively less of everything else. Most languages in which Bible Translation work is being done today occupy the thin edge of that distribution.

**What this means in practice:**

| Language situation | What to expect |
|---|---|
| **High-resource language** (English, French, Hindi) | Reliable output; standard prompting techniques fully apply |
| **Mid-resource language** (many national languages) | Competent output with more variability; test before trusting; grammar suggestions less reliable |
| **Low-resource language** (most minority / regional languages) | High hallucination risk; grammatical suggestions unreliable; any AI-generated text in the target language must be reviewed by a mother-tongue speaker before use |
| **Unwritten / oral language** | Do not use AI for generation in the target language at all — it has nothing to draw from |

**What you can do:**

- **Work in English or a strong regional language for reasoning tasks** — use AI to reason about translation problems (exegesis, cultural analysis, back-translation review), then apply the reasoning in your target language yourself. The AI's reasoning can be strong even when its output in the target language is weak.
- **Use AI output in minority languages as zero-draft only** — treat it the way you would treat any unreviewed back-translation: useful for surfacing issues, not authoritative.
- **Prompt explicitly for uncertainty** — include: *"If you are uncertain about any term or grammatical form in this language, flag it as UNCERTAIN rather than guessing."*
- **Test systematically** — before relying on AI assistance for a new language, run a few known passages through it and verify the output independently. This tells you what quality level to expect.

**The longer horizon:** Several organisations are actively working to improve AI capability for minority languages — including work connected to Bible Translation communities. This is discussed in §G.8.

**The rule:** For generation tasks in low-resource languages, AI output is zero-draft at best. Always have a mother-tongue speaker review before any content enters checking workflows.

---

## G.2 Offline and Local LLMs

Not everyone on your team has reliable internet. Some field locations cannot use cloud AI at all — and for sensitive content (see §G.3), you may not want to even if you could.

**What local LLMs are:** AI models that run entirely on your own device without sending any data to an external server. The model files are downloaded once and run locally — no internet required at inference time.

**Main tools:**

| Tool | How it works | Best for |
|---|---|---|
| **LM Studio** | Desktop app; download and run models via a simple interface; no coding required | Non-technical users who need a chat interface |
| **Ollama** | Command-line tool; runs models efficiently; can be integrated with other software | Technical users; team deployments; IDE integration |

**The trade-off:** Local models are smaller than cloud models. A model running on a laptop cannot match GPT-4 or Claude Sonnet in reasoning depth or language breadth. For well-defined, structured tasks (classification, extraction, formatting, comprehension question generation), the quality gap is often acceptable. For deep exegetical reasoning or nuanced cultural analysis, cloud models are still significantly stronger.

**Practical guidance for the field:**
- Test your most common task types against a local model before committing to it for field use.
- Local models work best with clean, well-structured prompts — the lower the model quality, the more important prompt precision becomes.
- A capable laptop (8–16 GB RAM, modern processor) can run models in the 7–13 billion parameter range reasonably well. Larger models require dedicated hardware.

**Who should pursue this:** Primarily Lane 3 (Technical). The decision to deploy a local model for a team is an infrastructure decision — it involves model evaluation, hardware assessment, and policy. Individual translators should not set this up independently without IT guidance.

**The rule:** Local LLMs are viable for structured, well-defined tasks in field contexts without reliable internet or with strict data privacy requirements. Evaluate before deploying — do not assume cloud-equivalent quality.

---

## G.3 What Must Never Leave Your Device — Data Privacy for Field Teams

The AI tools you use in this workshop are, almost without exception, cloud services. When you type a prompt and press send, that text travels to a server — usually operated by a company in a high-income country, under that country's law, with its own data retention and training policies. For most tasks, this is an acceptable trade-off. For some tasks in Bible Translation, it is not.

**What is at risk:**

| Category | Examples | Risk |
|---|---|---|
| **Unpublished Scripture drafts** | Back-translations, draft renderings, checking notes | May become training data; constitutes early disclosure of unpublished Scripture |
| **Community information** | Informant names, village locations, language group identities | Can expose vulnerable communities in restricted or sensitive areas |
| **Project-confidential decisions** | Key-term debates still under review, partnership agreements, funding sources | Premature external disclosure; intellectual property concerns |

**The default rule:** If you would not paste it into an email to a stranger, do not paste it into a public AI tool. If it is not yet published, treat it as confidential until your organisation has a written policy that says otherwise.

**What you can do instead:**

- **Use a local model** — tools like LM Studio and Ollama run a model entirely on your own device. No data leaves. See §G.2 for orientation.
- **Restructure the task** — often you do not need to paste the sensitive content at all. Instead of *"review this draft of Mark 5:3 in [language]"*, describe the translation problem in abstract terms: *"In a shame-honour society, how should a translator handle a passage where a character's dignity is publicly restored?"* The AI reasons on the question; you apply the answer to your draft privately.
- **Use enterprise tiers** — some platforms (Claude Teams, Microsoft Copilot for Enterprise) include data residency and no-training commitments. Verify with your organisation's IT lane before relying on these guarantees — platform terms change, and verification requires reading the current policy, not assumed reputation.

**Who owns this decision:** This is not a translator-level call. Every organisation using AI on live project data needs a written policy. If yours does not have one yet, the Lane 3 deliverable from this workshop is to initiate that conversation — before it becomes a problem.

**The rule:** Published content and abstract reasoning tasks are generally safe for public cloud AI. Unpublished drafts, community identities, and project-confidential data are not — until your organisation's policy says otherwise in writing.

---

## G.4 Beyond Chat: API Platforms and Automation

The chat interface is the most accessible way to use AI, but it is not the only way. Two platforms are particularly relevant for teams that want to go further:

**Google AI Studio** and **OpenAI Platform** are developer-facing interfaces that give you direct access to the underlying models without the chat wrapper — allowing you to send prompts programmatically, build automated workflows, connect AI to other tools, and process large volumes of content in batch. These are the entry points to building AI-powered tools rather than just using them.

**What this enables for BT work:**
- Batch-processing a full chapter's back-translations through a checking rubric with a single script
- Connecting Paratext data to an AI analysis function
- Building a team-specific checking assistant with project data baked in
- Automating repetitive formatting or classification tasks across large datasets

**Who this is for:** Primarily Lane 3 (Technical). API access requires programming skills (Python is the most common language) and introduces cost considerations (API usage is typically metered per token). However, even non-technical practitioners benefit from knowing this tier exists — it allows them to brief a technical colleague on what is possible rather than assuming the chat interface is AI's only mode.

**The realistic starting point:** If your team has someone with basic Python knowledge and a specific repetitive task that currently takes hours, API automation is worth exploring. The platforms provide extensive documentation and introductory tutorials.

**A caution:** Building custom AI workflows introduces new governance questions — who reviews the automation logic, who handles errors, who is accountable when the batch output contains mistakes? These questions need answers before deployment, not after.

---

## G.5 Multi-Modal Prompting

Most AI prompting in BT work uses text. But modern AI models can also work with images, documents, audio, and combinations of all of these. This is called **multi-modal** input.

**What is currently available in most tools:**
- **Images** — paste or upload an image and ask the AI to describe, analyse, or reason about it
- **Documents** — upload a PDF or Word file and ask the AI to work with its contents
- **Audio** — some tools (notably tools built on Whisper, OpenAI's transcription model) can transcribe speech to text, which can then be processed by a language model

**Practical applications for BT:**

| Task | How multi-modal helps |
|---|---|
| **Handwritten field notes** | Photograph notes and ask the AI to transcribe and organise them |
| **Scanned commentaries** | Upload a scanned page and ask for a summary relevant to your passage |
| **Diagram or map analysis** | Share a geographical or cultural diagram and ask for context relevant to your translation |
| **Oral community recordings** | Transcribe audio using Whisper-based tools, then use the transcript in standard prompting workflows |
| **Checking illustrations** | Share an illustration draft and ask: "Does this image accurately represent the events of Mark 5:1–20? List any discrepancies." |

**Current limitations:**
- Image analysis quality varies significantly by tool and model.
- Audio transcription introduces its own error rate, especially for low-resource languages or heavy accents — always verify the transcript before using it.
- Multi-modal workflows involve larger data volumes and raise sharper privacy questions (images and recordings may contain identifiable information).

**The rule:** Treat multi-modal outputs with the same verification habits as text outputs. Transcription errors and image misreadings are as possible — and as consequential — as text hallucinations.

---

## G.6 Agentic Workflows

Standard prompting is a single-turn or multi-turn conversation: you ask, the model responds, you act on the response. **Agentic AI** goes further: an AI agent can plan a multi-step task, execute steps sequentially, use tools (search, code execution, file access), make decisions along the way, and produce a complex output — with minimal human input at each step.

You have probably already encountered a basic form of this: ChatGPT using web search, or Claude reading a file you uploaded. These are simple agents. More complex agents can write and run code, browse websites, check facts, and chain tasks together autonomously.

**Prompting in IDEs — AI at Your Desk, Not in the Cloud**

Most AI interaction happens in a browser tab: you type into a chatbot, get a response, copy it somewhere useful. An **Integrated Development Environment (IDE)** with AI built in works differently. Think of it as a personal AI workbench — one that sits on your machine, has direct access to the files you are actually working on, and can coordinate multiple tools and steps on your behalf without you uploading anything. Tools like **Cursor**, **VS Code with GitHub Copilot**, or **Windsurf** are increasingly used not just by programmers, but by any practitioner who works with text files and wants AI close to their work.

*What makes this relevant for Bible translators*

An AI-equipped IDE gives you something no chatbot tab does: the AI can already see what is in your files. You do not describe your key-term list or paste your draft — you open the folder and the AI reads across everything in it. Because it runs locally, your translation files and community data can stay on your machine (see §G.2).

Some practical possibilities, all achievable through natural language prompting once you have a feel for the interface:

- **Draft generation against your own reference material.** Point the AI at your existing Scripture translation files and a reference lexicon. Ask it to generate a draft of a new passage that is consistent with your team's established key-term decisions. It reads both at once — no manual copy-pasting.

- **RAG without infrastructure.** A full RAG pipeline normally requires a server and technical setup. In an AI-equipped IDE you can approximate the same effect by prompting: *"Here is my translation style guide [file A]. Here are my checking notes [file B]. Evaluate this draft for consistency with both."* The AI reads your documents, reasons over them, and responds — all without sending data to a third-party storage service.

- **Formatting and batch transformation.** Reformatting USFM files, extracting key terms into a spreadsheet, converting back-translation notes into a checking report — tasks that would take hours of manual work can often be described in plain language. *"Take all the consultant notes in this folder and produce a summary table with passage reference, issue type, and resolution status."* One prompt, a multi-step task, structured output.

- **Multi-step checking workflows.** Ask the AI to read a draft passage, compare it against the UBS checking questions for that section, and flag any question the draft does not clearly answer. The AI carries out the full sequence across your working files.

The key shift in posture: you are not asking one question per session. You are describing a workflow — and the AI carries it out.

*For the technically oriented*

If you have programming capability — or are willing to learn a little Python — the possibilities expand further. An AI IDE will write the code for you: a script that processes a whole folder of USFM files, a tool that checks your key-term register against every chapter of a translation, a formatter that converts from one tool's export format to another's import format. You describe what you need in plain language; the AI writes the code; you run it. This is not the same as becoming a programmer — but it is a level of technical agency that was previously unavailable to people who had not spent years learning to code.

*Honest limitations*

- The learning curve is steeper than a chatbot. Initial setup takes time.
- AI-generated code must be reviewed — it writes plausible scripts that may contain errors.
- Complex agentic tasks require precise task descriptions; vague instructions produce adjacent results.

The investment is real. So is the capability. For translation teams working with large file sets, multi-language comparisons, or repetitive formatting tasks, the time saved at scale makes the initial learning curve worthwhile.

*This handbook is itself a worked example of this workflow — produced in an AI-equipped IDE over the course of a few days. Appendix I documents exactly how it was done.*

**A governance note:** Agents can act on your behalf — sending emails, modifying files, publishing content. Any agentic tool given access to production systems needs explicit governance: what is it authorised to do, who can override it, and how are errors caught?

---

## G.7 Prompt Maintenance — Treating Prompts as Institutional Assets

Individual prompts written for one task and discarded are a missed opportunity. When a prompt works well, it encodes hard-won knowledge — about your team's workflow, your target community, your style requirements, your theological guardrails. That knowledge should not live only in one person's chat history.

**Why prompts decay**

A prompt that produces excellent output today may produce noticeably different output six months from now — because the underlying model has been updated, because the platform has changed its default behaviour, or because your project's context has evolved. This is **prompt decay**: the gradual divergence between what a prompt was designed to do and what it actually produces.

Treating prompts as living documents — with version dates, review cycles, and ownership — prevents this from becoming invisible drift.

**Building a team prompt library**

A prompt library is a shared, maintained collection of production-ready prompts for your team's most common tasks. It should include:

| Field | What to record |
|---|---|
| **Task** | What workflow step this prompt serves |
| **Lane** | Which role(s) it is designed for |
| **Date tested** | When it was last verified to produce good output |
| **Model tested on** | Which model it was verified with (prompts are not always portable across models) |
| **Known limitations** | What it does not handle well |
| **Guardrails** | What safety constraints are built in |

For small teams, a shared document or spreadsheet is sufficient. For larger networks, a structured digital resource is worth the setup investment.

**Prompt ownership**

Someone needs to own each prompt — to review it when the model updates, to revise it when project context changes, and to retire it when it is no longer fit for purpose. This is a Lane 3 function in larger organisations, but the culture of maintenance needs to be shared across all lanes.

**The rule:** A prompt that works is worth keeping. A prompt worth keeping is worth maintaining.

---

## G.8 Diagnostic Prompting — When the Output Is Wrong

When an AI produces a bad output, the instinct is to re-prompt immediately. Often this makes things worse — you change the wrong thing, or you obscure the underlying problem with new instructions. **Diagnostic prompting** is a structured alternative: you interrogate *why* the output failed before you change anything.

**A simple diagnostic loop**

When an output is wrong or weak, run through these checks before re-prompting:

1. **Is this a hallucination?** Did the AI invent a fact, reference, or detail? If so, the fix is a stronger verification guardrail, not a rephrased question.

2. **Is this a knowledge cutoff problem?** Is the AI describing a state of affairs that has since changed? If so, supply the current document and instruct the model to reason from it only.

3. **Is the persona too generic?** Is the output aimed at the statistical average reader rather than your specific context? Sharpen the Persona and audience description.

4. **Is the context missing?** Did the AI have to guess at information you have but didn't provide — the target community, the passage scope, the checking stage? Add it.

5. **Is the output format wrong?** Did the AI produce prose when you needed a table, or a table when you needed a running analysis? Specify the format explicitly.

6. **Is the task too broad?** Did you ask for multiple things in one prompt, causing the AI to average across them? Break it into sequential tasks.

Most bad outputs fail for one of these six reasons. Identifying which one before re-prompting produces a more targeted fix and a better prompt for reuse.

---

## G.9 Red-Teaming Your Own Prompts

Before deploying a prompt in a real workflow — especially a prompt that will be used by your team, or applied to sensitive content — try to break it deliberately. This is called **red-teaming**.

**What red-teaming looks like in practice:**

- Run the prompt with input that is deliberately ambiguous, incomplete, or edge-case. Does the output hold? Does the guardrail trigger when it should?
- Ask the AI to roleplay as a careless user deliberately trying to bypass the constraints. Does the prompt hold?
- Run the same prompt on several different passages or tasks. Is the output quality consistent, or does it work only for the original test case?
- Have a colleague run the prompt independently on the same input. Do they get the same output? If not, why?

A prompt that survives simple red-teaming is significantly more trustworthy than one that was only ever tested on the ideal case.

**For theological guardrails specifically:** before using a prompt in a checking round, test it on content where you already know what the correct answer is. Does the prompt produce the right constraint behaviour? Does it flag what it should flag? Does it refrain from speculating where it should?

This investment is proportional to the stakes. A prompt for formatting meeting notes needs less red-teaming than one used in a key-term checking session.

---

## G.10 The Future: Minority Languages and What Comes Next

**The capability gap**

AI capability in minority languages is currently poor — and this is not a marginal problem for Bible Translation communities. The languages where BT work is most needed are precisely the languages least represented in AI training data. The communities most dependent on accurate Scripture in their mother tongue are the ones for whom AI assistance is currently least reliable.

This should not be a source of despair. It should be a source of strategic clarity: AI is a powerful accelerant for work in well-resourced languages and a useful — but heavily caveated — assistant for work in low-resource languages right now. The gap is real. It is also closing.

**Three paths toward language-aware AI**

BT communities are not passive consumers in this story. There are three concrete paths through which existing BT data and expertise can feed back into expanding AI capability for minority languages:

1. **RAG (Retrieval-Augmented Generation)** — supplying your existing translated texts, back-translations, and lexicons to a general-purpose model so it reasons over your data during a session. No model training required; can be implemented with existing tools. The trade-offs (data privacy, context window limits, output verification) are covered in this handbook — see Chapter 4 and §G.3.

2. **Fine-tuning** — taking a pre-trained model and continuing to train it on your language's data, producing a model that has absorbed your community's patterns. Requires technical resources and data governance decisions that go well beyond prompting, but produces more durable capability gains.

3. **Tools built on existing BT data** — Scripture Forge is a current example: a tool that uses already-translated texts and back-translations to assist with generating new drafts in related languages or registers. This is AI augmentation from within the BT ecosystem, not dependent on general model improvements.

**What is being done more broadly**

- **NLLB (No Language Left Behind)** — Meta's multilingual translation model trained on data that includes many minority languages; directly relevant to BT communities.
- **FLORES and similar benchmarks** — measure AI performance across hundreds of languages, identifying where gaps are largest.
- **Masakhane** — building training data and models specifically for under-resourced African languages.
- **Omnilingual-ASR and audio-first initiatives** — recognise that the data scarcity for minority languages exists primarily in *written and parallel* form; audio data already exists in communities and is increasingly usable for training.
- **OPUS** — growing multilingual training datasets that include minority language texts.

The BT movement has been generating parallel text data — source, back-translation, draft, checking notes — for decades. This data is potentially one of the most valuable minority language resources in existence. Engaging with the AI research community around how this data can be responsibly shared and used is an unfinished conversation the tech side of BT needs to initiate.

**The AI automation trajectory**

A common concern among participants is: *as AI gets better, will it replace human translators and consultants?*

For high-resource languages, AI capability will continue to advance rapidly. Human oversight will remain essential — but the nature of that oversight shifts from manual execution to quality assurance, community accountability, and the judgment no compute can replace: does this rendering land correctly with the people it is for?

For minority languages, the trajectory is slower. But it is not zero — and a minority language LLM, once trained, is not limited to Scripture. It enables dictionaries, newspapers, educational materials, and community communication across every domain. That is not just a Bible Translation outcome. It is a community capacity outcome. The case for investing in it goes well beyond any single organisation's mission.

*For a full treatment of this topic — including the strategic case for BT involvement in the minority language AI movement — see Appendix H: LLMs and Minority Languages.*

**The skills you already have**

The Informed Pilot posture is not a temporary stance while AI is primitive. Precise prompting, critical evaluation, structured output, diagnostic thinking — these are the foundation for using AI responsibly at whatever capability level the tools reach. They are also the foundation for knowing when to trust an output, when to push back, and when the tool has reached the limit of what it can do for your community today.

---

*Return to Chapter 1: How LLMs Work →*  
*Return to Appendix B: Risk Quick Reference →*  
*Return to Appendix D: Prompt Template Library →*
