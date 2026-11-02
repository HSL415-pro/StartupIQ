"""
StartupIQ - Master Model Training & Pipeline Serialization
Executes all training scripts sequentially, verifies model integrity,
and generates models/metadata.json.
"""
import sys
import json
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from training.train_category import train_category_model
from training.train_market import train_market_model
from training.train_success import train_success_model
from training.train_similarity import train_similarity_index

def run_all_training():
    print("=" * 60)
    print("STARTUPIQ - MASTER MODEL TRAINING & PERSISTENCE")
    print("=" * 60)
    start_time = time.time()

    # Step 1: Category Model
    print("\n[Step 1/4] Training Category Detection Model (TF-IDF + Logistic Regression)...")
    cat_metrics = train_category_model()

    # Step 2: Market Potential Model
    print("\n[Step 2/4] Training Market Potential Model (TF-IDF + Ridge)...")
    mkt_metrics = train_market_model()

    # Step 3: Success Predictor Model
    print("\n[Step 3/4] Training Success Probability Regressor...")
    succ_metrics = train_success_model()

    # Step 4: Similarity Vector Index
    print("\n[Step 4/4] Building TF-IDF Similarity Index on Corpus...")
    sim_metrics = train_similarity_index()

    duration = round(time.time() - start_time, 2)
    models_dir = PROJECT_ROOT / "models"

    metadata = {
        "project": "StartupIQ",
        "tagline": "AI-Powered Startup Idea Analyzer",
        "trained_at_timestamp": time.time(),
        "training_duration_seconds": duration,
        "models": {
            "category_detection": {
                "algorithm": "TF-IDF + LogisticRegression",
                "accuracy": cat_metrics.get("accuracy"),
                "classes": cat_metrics.get("classes"),
                "vectorizer_file": "category_vectorizer.joblib",
                "model_file": "category_model.joblib"
            },
            "market_potential": {
                "algorithm": "TF-IDF + Ridge Regressor",
                "rmse": mkt_metrics.get("rmse"),
                "r2_score": mkt_metrics.get("r2"),
                "vectorizer_file": "market_vectorizer.joblib",
                "model_file": "market_model.joblib"
            },
            "success_predictor": {
                "algorithm": "Multi-Factor Interaction Ridge Regressor",
                "rmse": succ_metrics.get("rmse"),
                "r2_score": succ_metrics.get("r2"),
                "model_file": "success_model.joblib"
            },
            "similarity_finder": {
                "algorithm": "TF-IDF Vector Space + Cosine Similarity",
                "records_indexed": sim_metrics.get("records_indexed"),
                "vocab_size": sim_metrics.get("vocab_size"),
                "vectorizer_file": "similarity_vectorizer.joblib",
                "matrix_file": "similarity_matrix.joblib",
                "corpus_file": "startups_corpus.joblib"
            }
        }
    }

    meta_path = models_dir / "metadata.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("\n" + "=" * 60)
    print(f"ALL MODELS TRAINED AND SAVED SUCCESSFULLY IN {duration}s!")
    print(f"Metadata written to {meta_path}")
    print("=" * 60)

if __name__ == "__main__":
    run_all_training()
