"""
Seba Bondhu — demo chatbot.

A minimal, runnable demonstration of the governance principles laid out
in the toolkit's docs/ folder:

  - Retrieval-grounded answers only (docs/06-ai-risks.md: Hallucination)
  - A confidence threshold with an explicit "not certain" fallback,
    escalating to a human channel (docs/01-problem-definition.md scope;
    docs/07-governance-framework.md: Human oversight)
  - PII detection/redaction before anything is logged
    (docs/05-privacy-risks.md; docs/04-data-classification.md)
  - Structured, reason-coded logging for explainability
    (docs/06-ai-risks.md: Explainability)
  - No transactional capability, no eligibility determinations
    (docs/01-problem-definition.md: scope boundaries)

This is intentionally small: real dialect/discrimination testing,
a real messaging-channel integration, and a real human-escalation
queue are all out of scope for a demo. See docs/08-responsible-ai-checklist.md
for what a production version would still need before launch.

Run:
    python app.py
Type a question in Bangla or English. Type 'quit' to exit.
"""

from __future__ import annotations

from rag.retriever import KnowledgeBaseRetriever
from rag.logger import log_interaction

HUMAN_ESCALATION_MESSAGE = (
    "I'm not confident I have the right answer for that. Rather than guess, "
    "please contact the 333 National Helpline or visit your local Union "
    "Digital Centre — a human agent can help with this directly.\n"
    "(এই বিষয়ে আমি নিশ্চিত নই। অনুগ্রহ করে ৩৩৩ হেল্পলাইনে যোগাযোগ করুন অথবা "
    "নিকটস্থ ইউনিয়ন ডিজিটাল সেন্টারে যোগাযোগ করুন।)"
)

ELIGIBILITY_GUARD_PHRASES = ("am i eligible", "eligible for", "do i qualify")


def format_answer(doc) -> str:
    lines = [
        f"[Source: {doc.title}]",
        "",
    ]
    for section in ("STEPS:", "REQUIRED_DOCUMENTS:", "FEE:", "WHERE_TO_APPLY:"):
        if section in doc.content:
            block = doc.content.split(section, 1)[1].split("\n\n", 1)[0]
            lines.append(section)
            lines.append(block.strip())
            lines.append("")
    if "IMPORTANT_BOUNDARY:" in doc.content:
        boundary = doc.content.split("IMPORTANT_BOUNDARY:", 1)[1].split("\n\n", 1)[0]
        lines.append("Note:")
        lines.append(boundary.strip())
        lines.append("")
    lines.append(
        "(This is demo content for illustration only — always confirm "
        "current fees, documents, and timelines with the official portal "
        "or office named above.)"
    )
    return "\n".join(lines)


def answer_query(retriever: KnowledgeBaseRetriever, query: str) -> str:
    lowered = query.lower()

    results = retriever.retrieve(query, top_k=1)
    top = results[0]

    if any(phrase in lowered for phrase in ELIGIBILITY_GUARD_PHRASES):
        # Scope boundary: never issue a yes/no eligibility determination,
        # even if retrieval found a relevant, high-confidence document.
        log_interaction(query, reason_code="eligibility_boundary",
                         doc_id=top.doc_id, confidence=top.score)
        return (
            "I can explain the general eligibility criteria for this "
            "programme, but I can't determine whether you personally "
            "qualify — that decision is made by the local selection "
            "committee. Here's what I can tell you:\n\n"
            + format_answer(top)
        )

    if not retriever.is_confident(top):
        log_interaction(query, reason_code="low_confidence",
                         doc_id=top.doc_id, confidence=top.score)
        return HUMAN_ESCALATION_MESSAGE

    log_interaction(query, reason_code="answered",
                     doc_id=top.doc_id, confidence=top.score)
    return format_answer(top)


def main() -> None:
    print("Seba Bondhu (demo) — ask about NID correction, birth registration,")
    print("land records, trade licences, or social safety net programmes.")
    print("Type 'quit' to exit.\n")

    retriever = KnowledgeBaseRetriever()

    while True:
        try:
            query = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not query:
            continue
        if query.lower() in ("quit", "exit"):
            print("Goodbye.")
            break
        print("\nSeba Bondhu:")
        print(answer_query(retriever, query))
        print()


if __name__ == "__main__":
    main()
