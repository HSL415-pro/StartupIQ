"""
StartupIQ - Module 6: Similar Startup Finder Service
Uses TF-IDF Vector Space Model and Cosine Similarity against the indexed startup corpus
to discover the Top 5 most semantically and architecturally similar startups.
"""
from pathlib import Path
from typing import List, Dict, Any
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from utils.text_cleaner import clean_text

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

class SimilarityService:
    def __init__(self):
        self.vectorizer = None
        self.matrix = None
        self.corpus = None
        self._load_index()

    def _load_index(self):
        vec_path = MODELS_DIR / "similarity_vectorizer.joblib"
        mat_path = MODELS_DIR / "similarity_matrix.joblib"
        corp_path = MODELS_DIR / "startups_corpus.joblib"

        if vec_path.exists() and mat_path.exists() and corp_path.exists():
            self.vectorizer = joblib.load(vec_path)
            self.matrix = joblib.load(mat_path)
            self.corpus = joblib.load(corp_path)

    def find_similar_startups(
        self,
        name: str,
        category: str,
        description: str,
        problem: str,
        audience: str = "",
        tech_stack: str = "",
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """Finds top K similar startups with similarity percentages."""
        if not self.vectorizer or self.matrix is None or not self.corpus:
            self._load_index()

        query_text = clean_text(
            f"{name} {category} {problem} {description} {audience} {tech_stack}"
        )

        if not self.vectorizer or self.matrix is None or not self.corpus:
            # Fallback return empty list
            return []

        query_vec = self.vectorizer.transform([query_text])
        similarities = cosine_similarity(query_vec, self.matrix)[0]

        # Get top indices
        top_indices = np.argsort(similarities)[::-1][:top_k]

        results = []
        for idx in top_indices:
            record = self.corpus[idx]
            raw_sim = float(similarities[idx])

            # Scale to realistic 0-100 percentage
            # Cosine similarity on sparse TF-IDF typically ranges 0.15 - 0.75 for related docs
            percentage = round(min(max(raw_sim * 135.0, 35.0), 96.5), 1)

            results.append({
                "startup_name": record.get("startup_name"),
                "category": record.get("category"),
                "description": record.get("description"),
                "problem_statement": record.get("problem_statement"),
                "target_audience": record.get("target_audience"),
                "tech_stack": record.get("tech_stack"),
                "similarity_score": round(raw_sim, 4),
                "similarity_percentage": percentage,
                "investor_readiness": record.get("investor_readiness", 70),
                "success_probability": record.get("success_probability", 65)
            })

        return results

similarity_service = SimilarityService()
