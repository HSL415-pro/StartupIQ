"""
StartupIQ - Module 3: Market Potential Engine Service
Predicts continuous Market Potential Score (0-100) and categorizes into Low, Medium, High tiers.
Integrates trained Ridge Regressor with category TAM indicators and addressable market analysis.
"""
from pathlib import Path
from typing import Dict, Any
import joblib
from utils.text_cleaner import clean_text
from utils.scoring import classify_market

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

class MarketService:
    def __init__(self):
        self.vectorizer = None
        self.model = None
        self._load_models()

    def _load_models(self):
        vec_path = MODELS_DIR / "market_vectorizer.joblib"
        model_path = MODELS_DIR / "market_model.joblib"
        if vec_path.exists() and model_path.exists():
            self.vectorizer = joblib.load(vec_path)
            self.model = joblib.load(model_path)

    def predict_market_potential(
        self,
        category: str,
        target_audience: str,
        problem: str,
        description: str,
        tech_stack: str = ""
    ) -> Dict[str, Any]:
        """Calculates market potential score and tier classification."""
        if not self.model or not self.vectorizer:
            self._load_models()

        text = clean_text(
            f"Category: {category} Target Audience: {target_audience} "
            f"Problem: {problem} Description: {description} Tech: {tech_stack}"
        )

        base_score = 65.0
        if self.model and self.vectorizer:
            try:
                vec = self.vectorizer.transform([text])
                pred = float(self.model.predict(vec)[0])
                base_score = pred
            except Exception as e:
                print(f"[Warning] Market model prediction failed: {e}")

        # Category TAM expansion constants
        tam_multipliers = {
            "AI": 1.15, "FinTech": 1.12, "SaaS": 1.10, "Cybersecurity": 1.10,
            "HealthTech": 1.08, "E-Commerce": 1.05, "Developer Tools": 1.06,
            "EdTech": 0.98, "FoodTech": 0.96, "Agriculture": 0.98
        }
        tam_factor = tam_multipliers.get(category, 1.0)
        adjusted_score = base_score * tam_factor

        final_score = int(round(min(max(adjusted_score, 20), 98)))
        tier = classify_market(final_score)

        tam_estimates = {
            "AI": "$450B+ CAGR 36.8%",
            "SaaS": "$380B+ CAGR 18.2%",
            "FinTech": "$320B+ CAGR 20.5%",
            "Cybersecurity": "$270B+ CAGR 13.8%",
            "HealthTech": "$290B+ CAGR 16.4%",
            "E-Commerce": "$6.3T Global B2C/B2B",
            "Developer Tools": "$45B+ CAGR 24.1%",
            "EdTech": "$180B+ CAGR 14.5%",
            "Agriculture": "$130B+ CAGR 11.2%",
            "FoodTech": "$220B+ CAGR 12.1%"
        }.get(category, "$150B+ Global Market")

        tier_details = {
            "High": {
                "badge_color": "emerald",
                "verdict": "High-velocity secular growth sector with large institutional capital flows and rapid customer adoption headroom.",
                "expansion_rate": "Accelerating"
            },
            "Medium": {
                "badge_color": "blue",
                "verdict": "Substantial addressable market with healthy demand, requiring clear product positioning against existing incumbents.",
                "expansion_rate": "Steady"
            },
            "Low": {
                "badge_color": "amber",
                "verdict": "Specialized niche segment; requires high ACV or vertical lock-in to achieve venture-scale returns.",
                "expansion_rate": "Selective"
            }
        }[tier]

        return {
            "score": final_score,
            "tier": tier,
            "estimated_tam": tam_estimates,
            "verdict": tier_details["verdict"],
            "badge_color": tier_details["badge_color"],
            "expansion_rate": tier_details["expansion_rate"],
            "drivers": [
                f"Sector Tailwind: {category} global spending trends",
                f"Target Market: Focused on {target_audience}",
                f"Defensibility: Product integration depth"
            ]
        }

market_service = MarketService()
