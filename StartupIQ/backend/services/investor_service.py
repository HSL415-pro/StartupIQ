"""
StartupIQ - Module 8: Investor Readiness Engine Service
Computes composite Investor Readiness Score (0-100) and multi-factor breakdown across:
1. Innovation
2. Scalability
3. Market Size
4. Technical Feasibility
Outputs detailed investor perspective, funding tier, and round fit.
"""
from typing import Dict, Any
from utils.scoring import compute_investor_readiness

class InvestorService:
    def evaluate_investor_readiness(
        self,
        innovation_score: float,
        market_score: float,
        complexity_score: float,
        success_probability: float,
        category: str = ""
    ) -> Dict[str, Any]:
        """Calculates investor readiness score and 4 constituent factors."""
        data = compute_investor_readiness(
            innovation=innovation_score,
            market=market_score,
            complexity=complexity_score,
            success_prob=success_probability
        )

        score = data["score"]
        tier = data["tier"]
        factors = data["factors"]

        # Venture capital pitch positioning summary
        if score >= 80:
            pitch_advice = "Pitch with strong emphasis on network effects, proprietary moat, and rapid multi-million ARR scalability."
            target_round = "Series A / Institutional Seed"
            check_size = "$2.5M - $6.0M"
        elif score >= 65:
            pitch_advice = "Focus narrative on acute customer pain, early retention signals, and disciplined payback periods."
            target_round = "Seed / Angel Syndicate"
            check_size = "$750K - $2.0M"
        elif score >= 50:
            pitch_advice = "Highlight founder-market fit, prototype customer feedback, and low-cost customer discovery traction."
            target_round = "Pre-Seed / Top Accelerator"
            check_size = "$150K - $500K"
        else:
            pitch_advice = "Focus on de-risking the core product assumptions, validating willingness-to-pay, and narrowing customer persona."
            target_round = "Founder Bootstrapped / Friends & Family"
            check_size = "Sub-$100K"

        return {
            "score": score,
            "tier": tier,
            "target_round": target_round,
            "estimated_check_size": check_size,
            "pitch_advice": pitch_advice,
            "badge_color": data["color"],
            "factors": [
                {
                    "name": "Innovation & Moat",
                    "score": factors["innovation"],
                    "weight": "25%",
                    "description": "Technological uniqueness, IP defensibility, and barrier to replication."
                },
                {
                    "name": "Scalability & Flywheel",
                    "score": factors["scalability"],
                    "weight": "30%",
                    "description": "Operational margin leverage, automated workflows, and marginal cost of customer delivery."
                },
                {
                    "name": "Market Size & Headwinds",
                    "score": factors["market_size"],
                    "weight": "25%",
                    "description": "Total addressable market depth, customer willingness-to-pay, and sector expansion."
                },
                {
                    "name": "Technical Feasibility",
                    "score": factors["technical_feasibility"],
                    "weight": "20%",
                    "description": "Pragmatic path to production stability, infrastructure reliability, and timeline certainty."
                }
            ]
        }

investor_service = InvestorService()
