# Appendix H: LLMs and Minority Languages
## The Capability Gap, What Causes It, and What the Bible Translation Community Can Do About It

*This appendix is written for practitioners and leaders in the Bible Translation movement who want to understand the current state of AI in minority languages — what the gap actually is, why it exists, and what paths exist to close it. It is also intended as a reference for those making the case internally for strategic engagement with the AI research community.*

---

## H.1 The Gap Is Real — But It Is Misunderstood

The standard observation is correct: AI performs poorly on minority languages. ChatGPT, Claude, Gemini — every major model produces less reliable output, more hallucinations, and weaker grammatical accuracy in minority or low-resource languages than in English.

But the *reason* for this gap is misunderstood in ways that matter for how it gets fixed.

**The common assumption:** These languages are too complex, too irregular, or structurally too different from English for AI to handle well.

**The reality:** LLMs are fundamentally language-agnostic. They do not have a preference for English. They do not understand English better in any cognitive sense. They perform well in English for one reason only: there was enough English text in the training data to teach the model the patterns of English. Given equivalent data, a model trained on any language would perform as well in that language as the current models perform in English.

The gap is not architectural. It is a data problem. And data problems are solvable.

This reframing matters for strategy. The question is not *can AI ever work for minority languages?* The question is *what would it take to build the training data, and who is positioned to contribute to that?*

The Bible Translation community is among the most uniquely positioned organisations on earth to answer that second question — and it has not yet fully recognised this.

---

## H.2 Why Minority Language Data Is Scarcer Than It Appears

The data scarcity for minority languages is real, but it has a specific shape that is important to understand.

**The written data problem**

Most AI training pipelines rely on large volumes of written text — web pages, books, newspapers, academic papers. For minority languages, this written corpus is thin. Many smaller languages have:
- No significant presence on the web
- Limited published literature
- Scripture translations, some educational materials, and little else in digital form

This is the layer most people think of when they say "there's no data." But there is another layer that is often overlooked.

**The spoken data advantage**

The data scarcity for minority languages exists primarily in *written and parallel-text* form. In audio, the situation looks different. Many communities that have no written web presence have:
- Hours of recorded oral Scripture, sermons, and teaching
- Community radio
- Recorded interviews, oral histories, and language surveys
- Casual conversation audio from language documentation projects
- **Pure recordings of everyday natural language use** — market conversations, family speech, storytelling — the informal registers that formal Scripture recordings do not capture, and that AI systems need in order to serve real community communication rather than only liturgical contexts

This audio data is not currently in a form that AI systems can easily train on. But multi-modal AI — models that learn from audio as well as text — is advancing rapidly. The pipeline from community audio recordings to language-capable AI models is becoming more tractable every year. The data is already there. The question is whether the community that holds it will participate in making it usable.

**The parallel text opportunity**

Bible Translation work produces, as a byproduct, something that AI research calls a **parallel corpus**: the same content expressed across multiple languages (source text, back-translation, draft, reference translations). Parallel corpora are among the most valuable resources for training multilingual translation models. The BT movement has been generating them for decades, often without recognising their value in this new context.

---

## H.3 What BT Communities Already Have

The existing assets of the Bible Translation movement, viewed through an AI-readiness lens:

| Asset | AI value |
|---|---|
| **Published Scripture translations** | Parallel text data across hundreds of languages and dialects |
| **Back-translations** | Interlinear-style alignment between source meaning and target language expression |
| **Lexicons and key-term registers** | Structured semantic data in minority languages |
| **Checking notes and consultant feedback** | Quality-labelled translation data (corrections, alternatives, rationale) |
| **Oral recordings** (Scripture, teaching, community) | Audio training data in languages with thin written corpora |
| **Language surveys** | Demographic and phonological data for language identification and scoping |
| **Interlinear texts and glossing notes** | Fine-grained linguistic annotation uncommon in other domains |

These assets exist. What is largely missing is the governance framework, the community consent, and the technical infrastructure to make them usable for AI training in a way that protects the communities who generated them.

---

## H.4 Three Paths to Language-Aware AI

There is a spectrum of approaches to making AI more capable in a specific minority language, ranging from immediate and accessible to longer-term and transformative.

### Path 1 — RAG: Immediate, No Model Training Required

**What it is:** Retrieval-Augmented Generation supplies your existing documents to a general-purpose model during a session. The model does not learn from your data permanently — it reads it within the context window and reasons over it. Close the session and the data is gone from the model's working memory.

**What it can do for minority languages:**
- Give a general-purpose model access to your key-term list, checking notes, and style guide — so it reasons from your community's established decisions rather than its own defaults
- Allow Scripture Forge and similar tools to generate drafts that align with your existing rendered passages
- Provide a general model with access to a small lexicon of your target language so it handles key vocabulary correctly

**Trade-offs:**
- The model's underlying language capability is unchanged — it is reading your data, not learning from it
- Context window limits apply; very large corpora cannot all be supplied at once
- Data privacy concerns apply here in full — what you supply via RAG goes to the model provider's servers unless you are using a local model (see §G.2 and §G.3)

**Starting point:** This is accessible now with existing tools. It requires no programming for basic use. It is the right first step for teams that want to make AI more language-aware without infrastructure investment.

### Path 2 — Fine-Tuning: Deeper, Requires Technical Resources

**What it is:** Taking a pre-trained model and continuing to train it on your language's data. The model's weights are adjusted to incorporate the patterns of your language, producing a model that "knows" your language in a more permanent and generalisable way than RAG.

**What it can do:**
- Produce a model that handles your language's grammar, vocabulary, and idiom reliably across tasks — not just the content you supplied in any single session
- Improve performance on translation, back-translation checking, and naturalness evaluation in the target language
- Be deployed locally (see §G.2) without sending community data to external servers

**Trade-offs:**
- Requires sufficient training data (typically thousands to tens of thousands of examples for meaningful improvement)
- Requires technical capability — Python programming, GPU access, model training infrastructure
- Requires data governance decisions: who owns the trained model, who can use it, under what policy?
- The resulting model inherits the base model's architecture and licence terms — check these before investing in fine-tuning

**Who this is for:** Lane 3 technical staff or external AI research partners. Not a practitioner-level decision, but a leadership-level investment decision worth understanding.

### Path 3 — Training Minority Language Foundation Models: Strategic, Long-Term

**What it is:** Training an AI model from scratch (or from a multilingual base) specifically on minority language data — producing a foundation model that is natively capable in that language.

**What it can do:**
- Produce a general-purpose AI capable in the language across any domain — not limited to Scripture or BT workflows
- Enable communities to generate dictionaries, educational materials, newspapers, community communications, and other resources using an AI that actually understands their language
- Provide the foundation for future fine-tuning for specific tasks

**Trade-offs:**
- Requires large volumes of training data (tens to hundreds of millions of tokens at minimum for meaningful capability)
- Requires significant compute resources and AI research expertise
- Data collection, curation, and consent is a multi-year effort
- This is currently being done for some languages — building on or contributing to existing efforts is more efficient than starting independently

**The payoff is broader than BT:** A minority language LLM, once trained, is not a Bible Translation tool. It is a language technology asset for the whole community — enabling digital literacy, cultural documentation, economic participation, and communication infrastructure that go far beyond Scripture. The case for this investment is a community development argument, not just a translation efficiency argument.

---

## H.5 Existing Initiatives — What Is Already Being Built

The BT community is not alone in this work. Several significant efforts are already underway:

**NLLB — No Language Left Behind (Meta AI)**
Meta's 2022 multilingual translation model, trained on data from over 200 languages including many low-resource languages. NLLB was partly motivated by humanitarian and development use cases that overlap significantly with BT community needs. It is open for research use and has been incorporated into downstream tools. It is not yet Bible Translation-ready at the quality level consultants require, but it represents a significant infrastructure investment that BT communities can build on.

**FLORES-200 benchmark**
A standard evaluation benchmark covering 200 languages. Measures how well current AI systems perform translation and comprehension tasks across languages — making the capability gap visible and measurable. BT communities working in languages not currently on FLORES can contribute evaluation data that puts those languages on the measurement map.

**Masakhane**
A community of African researchers and practitioners building NLP (Natural Language Processing) resources for African languages — data sets, models, benchmarks, and research. A model for how community-led, distributed language work can scale. BT communities working in African languages should be in active conversation with Masakhane rather than working in parallel.

**Omnilingual-ASR and audio-first initiatives**
Speech recognition systems designed to work with low-resource languages by training on limited audio data. As these systems mature, the oral recordings held by BT and partner organisations become more directly useful for training language models.

**Scripture Forge**
A BT-ecosystem tool that uses existing translated texts and their back-translations to assist with generating new drafts. This is the closest current example of a RAG-style approach built specifically for BT workflow needs — and a template for what deeper data integration could produce.

---

## H.6 The Case for BT Community Engagement

The Bible Translation movement has three things the AI research community needs and currently lacks for minority language work:

1. **Data** — decades of parallel texts, back-translations, lexicons, and oral recordings across hundreds of languages, at a quality level that automated web scraping cannot produce

2. **Community relationships** — access to mother-tongue speakers, language communities, and cultural context required for meaningful data collection consent and quality evaluation

3. **Domain expertise** — translators, linguists, and consultants who can evaluate AI output in minority languages with the depth required to produce reliable quality labels

The AI research community has the model training infrastructure, the compute, and the technical expertise. The combination is potentially powerful. What is currently missing is the partnership.

**The challenge:** BT data is not currently in a form that is easily usable for AI training. It is distributed across organisations, in proprietary formats, under varying IP frameworks, and often without the community consent frameworks that responsible AI data collection requires. Making it usable would require:

- Standardised data formats and metadata
- Clear IP and licensing policies across organisations
- Community consent frameworks that centre the languages communities' interests
- Technical partnerships with AI research teams

None of these are insurmountable. They are governance and coordination problems, not technical problems. They require organisational will more than engineering capability.

**A call to the tech side of the BT movement:** The window of maximum influence on how minority language AI develops is open now — while foundation models are still being designed, training pipelines are still being shaped, and research communities are still looking for collaborators. Passive observation of this process is a strategic mistake. Active engagement — contributing data, building evaluation sets, partnering with research communities — positions the BT movement as a shaping partner rather than a downstream consumer of whatever the broader AI industry eventually produces for minority languages.

---

## H.7 What This Means for Participants at This Workshop

The participants of this workshop are not AI researchers or ML engineers. But they are:
- Users of AI tools in minority language contexts — with direct experience of the gap
- Holders of institutional knowledge about what quality means in these languages
- Potential evaluators of AI outputs — the human quality signal that training pipelines need
- Ambassadors within their organisations for why this investment matters

**Immediate actions within reach:**
- Document where AI currently fails in your target language — specific failure types, specific passages. This is valuable data even before any formal research partnership exists.
- When using AI tools, note which ones perform better or worse in your language and share that with your Lane 3 colleagues. This builds the evidence base for tool selection and investment decisions.
- Ask your organisation what its data policy is for minority language content — and if there isn't one, ask for one to be written.

**For Lane 3 leaders specifically:**
- Identify which of your existing data assets (parallel texts, lexicons, recordings) are in a form that could potentially contribute to AI training, and what governance decisions would be needed to make that possible.
- Explore the NLLB and FLORES documentation to understand which of your target languages already have AI evaluation data and which do not.
- Consider whether a relationship with Masakhane or a similar research community is appropriate for your language region.

---

*For the practical day-to-day implications of working with AI in low-resource language contexts, return to §G.1: Prompting in Regional and Minority Languages.*  
*For the data privacy considerations that govern how existing BT data can or cannot be used with external AI services, return to §G.3: Data Privacy.*  
*For the offline deployment options that make some of these paths feasible in field conditions, return to §G.2: Offline and Local LLMs.*
