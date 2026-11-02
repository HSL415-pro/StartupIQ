"""
StartupIQ - Module 3: Market Potential Trainer
Architecture: TF-IDF Text Extraction + Ridge Regressor
Outputs: Continuous Market Potential Score (0-100) and classification (Low/Medium/High).
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from utils.text_cleaner import clean_text

def train_market_model():
    dataset_path = PROJECT_ROOT / "datasets" / "startups.csv"
    df = pd.read_csv(dataset_path)
    print(f"[Market Trainer] Loaded {len(df)} records from {dataset_path}")

    # Combine enriched market signals
    texts = [
        clean_text(f"Category: {row['category']} Target Audience: {row['target_audience']} "
                   f"Problem: {row['problem_statement']} Description: {row['description']} Tech: {row['tech_stack']}")
        for _, row in df.iterrows()
    ]
    targets = df["market_score"].values

    X_train, X_test, y_train, y_test = train_test_split(
        texts, targets, test_size=0.15, random_state=42
    )

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    reg = Ridge(alpha=5.0)
    reg.fit(X_train_vec, y_train)

    y_pred = reg.predict(X_test_vec)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"[Market Trainer] Test RMSE: {np.sqrt(mse):.2f}, R2 Score: {r2:.3f}")

    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    
    vec_path = models_dir / "market_vectorizer.joblib"
    model_path = models_dir / "market_model.joblib"

    joblib.dump(vectorizer, vec_path)
    joblib.dump(reg, model_path)
    print(f"[Market Trainer] Saved models to {vec_path} and {model_path}")

    return {"rmse": float(np.sqrt(mse)), "r2": float(r2)}

if __name__ == "__main__":
    train_market_model()
