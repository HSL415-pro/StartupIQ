"""
StartupIQ - Module 6: Similar Startup Finder Trainer & Indexer
Architecture: TF-IDF Vector Space Model + Cosine Similarity Matrix
Outputs: Top 5 Similar Startup Ideas with similarity percentages.
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.text_cleaner import clean_text

def train_similarity_index():
    dataset_path = PROJECT_ROOT / "datasets" / "startups.csv"
    df = pd.read_csv(dataset_path)
    print(f"[Similarity Indexer] Loaded {len(df)} records from {dataset_path}")

    # Build rich search corpus for each startup
    corpus = []
    for _, row in df.iterrows():
        doc = clean_text(
            f"{row['startup_name']} {row['category']} {row['problem_statement']} "
            f"{row['description']} {row['target_audience']} {row['tech_stack']}"
        )
        corpus.append(doc)

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=8000,
        sublinear_tf=True
    )
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(f"[Similarity Indexer] TF-IDF Matrix shape: {tfidf_matrix.shape}")

    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    vec_path = models_dir / "similarity_vectorizer.joblib"
    matrix_path = models_dir / "similarity_matrix.joblib"
    corpus_path = models_dir / "startups_corpus.joblib"

    # Store startup metadata for instant retrieval
    startup_records = df[[
        "startup_name", "category", "description", "problem_statement",
        "target_audience", "tech_stack", "innovation_score", "market_score",
        "complexity_score", "success_probability", "investor_readiness"
    ]].to_dict(orient="records")

    joblib.dump(vectorizer, vec_path)
    joblib.dump(tfidf_matrix, matrix_path)
    joblib.dump(startup_records, corpus_path)
    print(f"[Similarity Indexer] Saved vectorizer, matrix, and corpus index to {models_dir}")

    return {"records_indexed": len(startup_records), "vocab_size": len(vectorizer.vocabulary_)}

if __name__ == "__main__":
    train_similarity_index()
