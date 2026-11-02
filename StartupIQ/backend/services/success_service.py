"""
StartupIQ - Module 5: Success Predictor Service
Calculates overall Success Probability (0-100%) by evaluating market demand, technological defensibility,
execution feasibility, and non-linear risk interaction terms.
"""
from pathlib import Path
from typing import Dict, Any
import numpy as np
import joblib

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

class SuccessService:
    def __init__(self):
        self.model = None
        self._load_model()

    def _load_model(self):
        model_path = MODELS_DIR / "success_model.joblib"
        if model_path.exists():
            self.model = joblib.load(model_path)

    def predict_success(
        self,
        innovation_score: float,
        market_score: float,
        complexity_score: float
    ) -> Dict[str, Any]:
        """Predicts success probability percentage using trained interaction regressor."""
        if not self.model:
            self._load_model()

        # Compute engineered features identical to training phase
        inn = float(innovation_score)
        mkt = float(market_score)
        cpx = float(complexity_score)

        inn_mkt = (inn * mkt) / 100.0
        cpx_penalty = abs(cpx - 50.0)
        feasibility_ratio = mkt / max(cpx, 1.0)

        feature_vector = np.array([[inn, mkt, cpx, inn_mkt, cpx_penalty, feasibility_ratio]])

        if self.model:
            try:
                pred = float(self.model.predict(feature_vector)[0])
            except Exception as e:
                print(f"[Warning] Success model prediction error: {e}")
                pred = (mkt * 0.45) + (inn * 0.35) - (cpx_penalty * 0.15)
        else:
            pred = (mkt * 0.45) + (inn * 0.35) - (cpx_penalty * 0.15)

        final_prob = int(round(min(max(pred, 15), 96)))

        if final_prob >= 75:
            tier = "High Probability of Scale"
            color = "emerald"
            verdict = "Exceptional market tailwinds and balanced risk-reward profile."
        elif final_prob >= 55:
            tier = "Moderate Viability"
            color = "blue"
            verdict = "Sound venture foundation; execution speed and go-to-market discipline are pivotal."
        else:
            tier = "High Risk / Pivot Recommended"
            color = "rose"
            verdict = "Significant market friction or complexity mismatch; refine the core value wedge."

        return {
            "success_probability": final_prob,
            "percentage": f"{final_prob}%",
            "tier": tier,
            "color": color,
            "verdict": verdict,
            "percentile": min(99, int(final_prob * 1.05)),
            "key_drivers": [
                f"Market Demand Weight: {int(mkt * 0.45)} pts",
                f"Defensibility Value: {int(inn * 0.35)} pts",
                f"Execution Complexity Risk: -{int(cpx_penalty * 0.15)} pts"
            ]
        }

success_service = SuccessService()
