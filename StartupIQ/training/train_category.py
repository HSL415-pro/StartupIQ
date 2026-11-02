"""
StartupIQ - Module 1: Category Detection Trainer
Architecture: TF-IDF Vectorizer + Logistic Regression Classifier
Detects startup industry category with confidence scores.
"""
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from utils.text_cleaner import clean_text

def train_category_model():
    dataset_path = PROJECT_ROOT / "datasets" / "startups.csv"
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found at {dataset_path}")

    df = pd.read_csv(dataset_path)
    print(f"[Category Trainer] Loaded {len(df)} records from {dataset_path}")

    # Combine description and problem statement for rich semantic context
    texts = [
        clean_text(f"{row['description']} {row['problem_statement']} {row['tech_stack']}")
        for _, row in df.iterrows()
    ]
    labels = df["category"].tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.15, random_state=42, stratify=labels
    )

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    clf = LogisticRegression(C=2.0, max_iter=1000, random_state=42)
    clf.fit(X_train_vec, y_train)

    y_pred = clf.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)
    print(f"[Category Trainer] Test Accuracy: {acc * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Save artifacts
    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    
    vec_path = models_dir / "category_vectorizer.joblib"
    model_path = models_dir / "category_model.joblib"

    joblib.dump(vectorizer, vec_path)
    joblib.dump(clf, model_path)
    print(f"[Category Trainer] Saved models to {vec_path} and {model_path}")

    return {"accuracy": float(acc), "classes": list(clf.classes_)}

if __name__ == "__main__":
    train_category_model()
