"""
Retrieval module for the Seba Bondhu demo chatbot.

Implements the "grounded, not generated" mitigation described in
docs/06-ai-risks.md (Hallucination): every answer must come from a
retrieved knowledge-base document, never from open-ended generation.

Uses simple TF-IDF + cosine similarity — no external API calls, so the
demo runs fully offline once dependencies are installed. Swapping this
for a stronger embedding-based retriever later is a drop-in change;
the governance property (grounding) is what matters, not the algorithm.
"""

from __future__ import annotations

import os
import glob
from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


KB_DIR = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")

# Below this similarity score, we treat retrieval as "not confident" and
# fall back to a human-escalation message rather than guessing.
# See docs/08-responsible-ai-checklist.md: "explicit not-certain fallback".
CONFIDENCE_THRESHOLD = 0.12


@dataclass
class RetrievedDoc:
    doc_id: str
    title: str
    content: str
    score: float


class KnowledgeBaseRetriever:
    def __init__(self, kb_dir: str = KB_DIR):
        self.kb_dir = kb_dir
        self.doc_ids: list[str] = []
        self.titles: list[str] = []
        self.contents: list[str] = []
        self._load_documents()
        # stop_words="english" matters here: without it, common words like
        # "the", "of", "is" in an off-topic query ("what is the capital of
        # France") were enough to produce a false-positive match against
        # the longest knowledge-base document. Caught by
        # tests/test_governance_checks.py::test_low_confidence_query_would_trigger_fallback
        # — exactly the kind of thing docs/08-responsible-ai-checklist.md
        # ("adversarial/off-topic test cases") exists to catch before launch.
        self.vectorizer = TfidfVectorizer(strip_accents="unicode", stop_words="english")
        self.doc_matrix = self.vectorizer.fit_transform(self.contents)

    def _load_documents(self) -> None:
        paths = sorted(glob.glob(os.path.join(self.kb_dir, "*.md")))
        if not paths:
            raise RuntimeError(f"No knowledge base documents found in {self.kb_dir}")
        for path in paths:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            title_line = next(
                (line for line in text.splitlines() if line.startswith("TITLE:")),
                "TITLE: (untitled)",
            )
            title = title_line.replace("TITLE:", "").strip()
            self.doc_ids.append(os.path.splitext(os.path.basename(path))[0])
            self.titles.append(title)
            self.contents.append(text)

    def retrieve(self, query: str, top_k: int = 1) -> list[RetrievedDoc]:
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_matrix)[0]
        ranked = sorted(
            range(len(scores)), key=lambda i: scores[i], reverse=True
        )[:top_k]
        return [
            RetrievedDoc(
                doc_id=self.doc_ids[i],
                title=self.titles[i],
                content=self.contents[i],
                score=float(scores[i]),
            )
            for i in ranked
        ]

    def is_confident(self, doc: RetrievedDoc) -> bool:
        return doc.score >= CONFIDENCE_THRESHOLD
