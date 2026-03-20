# Appendix C: Lane Reference Card
## Quick-Access Prompt Pairs by Role

*This appendix is designed to be printed as a single reference card and kept at your workstation. Each pair shows a weak prompt and its strong equivalent for the most common tasks in each lane.*

---

## Lane 1 — Translation & Language Practitioners

### A1: Cultural Background (FIA)

| | Prompt |
|---|---|
| ✗ Weak | *"Help me understand this verse."* |
| ✓ Strong | *"Act as a biblical scholar specialised in Second Temple Judaism. Explain the key cultural and historical background of Mark 5:1–5 that a mother-tongue translator in a shame-honour culture needs to understand before drafting. Keep it under 150 words. Do not speculate beyond the text."* |

**Why the weak prompt fails:** No verse cited. No purpose stated. No audience. You get a Sunday-school overview aimed at a general reader.

---

### A2: Meaning-Faithful Re-expression

| | Prompt |
|---|---|
| ✗ Weak | *"Express the message of this verse for a first-generation Christian."* |
| ✓ Strong | *"Using Mark 5:18–20 (ESV below), rewrite the passage in plain contemporary language accessible to a first-generation Christian in a non-literate oral culture. Do not change the meaning or add theological interpretation. Flag any phrase you are uncertain about. [paste ESV text]"* |

**Why the weak prompt fails:** No verse provided. No constraint on meaning change. Result may paraphrase or drift theologically.

---

### A3: Storyboard Scripting

| | Prompt |
|---|---|
| ✗ Weak | *"Draw a stick-figure series explaining this passage."* |
| ✓ Strong | *"For Mark 5:1–20, create a detailed storyboard script for a local artist: 6 panels. For each panel: setting, key characters, main action, one short plain-language caption (max 10 words). Cover: arrival, encounter, dialogue with Legion, the pigs, healing, sending. Do not add theological interpretation to the captions."* |

**Why the weak prompt fails:** Text AI cannot draw. No passage specified. Correct approach: script the storyboard; give it to a human artist.

---

## Lane 2 — Consultants & Advisors

### A4: Comparative Rendering Analysis

| | Prompt |
|---|---|
| ✗ Weak | *"Compare this verse with the KJV verse and tell me if there are any issues."* |
| ✓ Strong | *"Below are two renderings of Mark 5:9: [Draft] vs [KJV]. Act as a translation consultant. Identify differences in: (1) theological content, (2) implicit information, (3) natural discourse. For each difference, state whether it is a significant issue or an acceptable variation. Flag uncertain items as NEEDS VERIFICATION."* |

**Why the weak prompt fails:** "Issues" is undefined. Produces generic literary comparison, not translation-accuracy analysis.

---

### A5: Key-Term Identification

| | Prompt |
|---|---|
| ✗ Weak | *"What are the key terms in this passage?"* |
| ✓ Strong | *"From Mark 5:1–20 (ESV below), identify theologically significant terms — words whose precise rendering will significantly affect doctrinal understanding. For each: (1) semantic range in plain language, (2) risk if rendered too narrowly, (3) risk if rendered too broadly, (4) one checking question. Do not fabricate reference codes. Mark uncertain items. [paste ESV]"* |

**Why the weak prompt fails:** "Key term" is not defined operationally. Result: a list of common words with no translation-relevance weighting.

---

### A6: Back-Translation Review

| | Prompt |
|---|---|
| ✗ Weak | *"Review my back-translation for problems."* |
| ✓ Strong | *"Act as a senior translation consultant. Compare the back-translation below with the ESV source. Step 1 — identify implicit-information gaps (content in ESV absent from the back-translation). Step 2 — for each gap, assess: draft issue, back-translation issue, or both. Step 3 — suggest one checking question per gap. Return as: Verse | Gap | Type | Checking Question. Do not speculate. [paste ESV, draft, and back-translation]"* |

---

## Lane 3 — Leadership & Technical Enablers

### A7: Email Action Extraction

| | Prompt |
|---|---|
| ✗ Weak | *"Look through my emails and prepare a to-do list for me."* |
| ✓ Strong | *"I am pasting 5 emails below. For each: identify (1) any action required from me, (2) the deadline if mentioned, (3) who else is involved. Ignore greetings and signatures. Return as: Action | Owner | Deadline | Waiting On. [paste emails with sender and date labels]"* |

**Why the weak prompt fails:** AI has no access to your inbox. You must supply the data.

---

### A8: Meeting-to-Report Conversion

| | Prompt |
|---|---|
| ✗ Weak | *"Write up these meeting notes into a report."* |
| ✓ Strong | *"Act as a project manager writing a governance report for a non-technical executive. [example format below]. Convert the following notes into the same format. Do not insert information not in the notes. Do not use technical jargon. [paste example report, then paste raw notes]"* |

---

### A9: Discourse Markers (Lane 3 linguist support)

| | Prompt |
|---|---|
| ✗ Weak | *"Suggest better markers for the genealogy in Matthew 1."* |
| ✓ Strong | *"I am marking up Matthew 1:1–17 for [language name], an SOV language with postpositions. Pattern: 'A begot B, B begot C.' We currently use connective particle [X]. Suggest 2–3 alternative discourse markers more natural for a narrative genealogy in a SOV language. Explain why each is or is not appropriate for this text type."* |

**Why the weak prompt fails:** No language context. No current markers provided. "Better" is undefined. Result: generic Western discourse suggestions.

---

*See Appendix D for full production-ready prompt templates, and Appendix B for the complete Risk Reference.*
