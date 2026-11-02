"""
StartupIQ - Module 5: Success Predictor Trainer
Architecture: Multi-Factor Regressor combining Innovation, Market, Complexity, and Semantic signals
Outputs: Success Probability (0-100%).
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_success_model():
    dataset_path = PROJECT_ROOT / "datasets" / "startups.csv"
    df = pd.read_csv(dataset_path)
    print(f"[Success Trainer] Loaded {len(df)} records from {dataset_path}")

    # Feature matrix: innovation_score, market_score, complexity_score, and non-linear interactions
    features = []
    for _, row in df.iterrows():
        inn = row["innovation_score"]
        mkt = row["market_score"]
        cpx = row["complexity_score"]
        
        # Interaction terms
        inn_mkt = (inn * mkt) / 100.0
        cpx_penalty = abs(cpx - 50.0)
        feasibility_ratio = mkt / max(cpx, 1.0)
        
        features.append([inn, mkt, cpx, inn_mkt, cpx_penalty, feasibility_ratio])

    X = np.array(features)
    y = df["success_probability"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=42
    )

    model = Ridge(alpha=0.5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"[Success Trainer] Test RMSE: {np.sqrt(mse):.2f}, R2 Score: {r2:.3f}")

    models_dir = PROJECT_ROOT / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "success_model.joblib"

    joblib.dump(model, model_path)
    print(f"[Success Trainer] Saved model to {model_path}")

    return {"rmse": float(np.sqrt(mse)), "r2": float(r2)}

if __name__ == "__main__":
    train_success_model()
