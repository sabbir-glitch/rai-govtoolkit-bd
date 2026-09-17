# 6. AI Risks

Six risk categories, each with a concrete manifestation *in this specific use case* — not a generic list.

## Bias
**Manifestation**: The bot performs noticeably better for standard, formal-register Bangla (or Banglish/English) typed by literate, urban, Dhaka-dialect users than for regional dialects, phonetic/informal spelling, or voice input from less common accents.
**Why it matters here**: This directly undermines the equity goal in `01-problem-definition.md` — the exact users the system is meant to help most (rural, less formally educated) are the most likely to be underserved.
**Mitigation direction**: A dialect/register-diverse test set built specifically for this system (not just a generic Bangla NLP benchmark); disaggregated quality metrics by user segment where inferable (e.g. by channel/region), not just an overall accuracy number. A real, permissively-licensed dialect-labelled Bangla corpus (10 regional dialects) is available and integrated into the demo's test suite — see `11-real-data-sources.md` and `demo/tests/test_governance_checks.py`. It's a useful starting evaluation set, not a substitute for review by Bangla NLP specialists before a real deployment.

## Hallucination
**Manifestation**: The bot confidently states an incorrect document requirement, fee, or deadline for a government service — the single most damaging failure mode, since users may act on it directly (travel to the wrong office, miss a deadline, pay a fee that doesn't exist).
**Why it matters here**: Unlike a general-purpose assistant, wrong answers here have direct real-world procedural consequences for citizens who often have no easy way to double-check.
**Mitigation direction**: Retrieval-grounded answers only (the bot answers from an approved, version-controlled knowledge base of official circulars/FAQs — see `07-governance-framework.md` — rather than open-ended generation); every answer citing a specific procedural fact links to (or names) its source document; explicit "I'm not certain, please confirm with [office/helpline]" fallback rather than a guess, whenever retrieval confidence is low.

## Discrimination
**Manifestation**: Differential quality of service correlated with a protected or vulnerable characteristic — e.g. the bot handles queries about a majority-religion holiday-related service smoothly but mishandles a minority-community-specific query; or it defaults to male-coded assumptions in family/inheritance-related guidance.
**Why it matters here**: Public services are a legal-equality domain; a discriminatory AI intermediary is a different order of problem than a discriminatory recommendation engine.
**Mitigation direction**: Adversarial/targeted testing of known-sensitive query categories before launch; a standing channel for civil-society groups to flag discriminatory patterns post-launch (see KPI in `09-kpi-dashboard.md`).

## Privacy
**Manifestation**: Covered in depth in `05-privacy-risks.md` — the AI-specific angle is that a language model may *infer* sensitive attributes from a query (e.g. inferring likely religion, ethnicity, or disability status from phrasing) even when the user didn't explicitly state them, and could let that inference leak into its response or downstream logging.
**Mitigation direction**: The response-generation step should not condition on or surface inferred demographic attributes; logging pipeline stores the query, not any model-side inference about the user.

## Security
**Manifestation**: Prompt injection via a crafted query (e.g. attempting to make the bot reveal system instructions, other users' data, or perform an action outside its informational scope); abuse for mass-querying to scrape the knowledge base or probe for weaknesses; SMS-channel spoofing.
**Why it matters here**: A government-branded system is a higher-value target for both reputational attacks and genuine fraud attempts (e.g. impersonating the bot to phish citizens).
**Mitigation direction**: Input/output filtering for injection attempts; rate-limiting per phone number/session; a verified, single official channel (published number/URL) so citizens can distinguish the real bot from phishing lookalikes; regular security review, not a one-time audit. A real, purpose-built Bengali SMS phishing ("smishing") dataset — 7,005 labelled messages across Bengali, English, Banglish, and code-mixed text — is available for grounding this specific risk with real adversarial patterns rather than only hypothetical ones; see `11-real-data-sources.md`.

## Explainability
**Manifestation**: When the bot declines to answer, escalates, or gives a "confirm with your local office" fallback, a citizen (or an auditor, or a journalist) has no way to understand *why* — was it a knowledge-base gap, a low-confidence retrieval, or a deliberate scope boundary?
**Why it matters here**: Explainability here isn't an academic AI-transparency concern — it's what lets the operator diagnose failure patterns (e.g. "we're escalating an unusually high share of queries in Sylheti dialect" is only actionable if that's visible) and what lets citizens and oversight bodies trust the system's boundaries are real, not arbitrary.
**Mitigation direction**: Every escalation/fallback event logged with a machine-readable reason code (not just "escalated"); a plain-language "why did I get this answer / why was I redirected to a human" explainer accessible from the chat interface itself.
