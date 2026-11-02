"""
StartupIQ - Module 2: Innovation Analyzer Service
Evaluates idea novelty, frontier technological depth, and differentiation from standard paradigms.
Outputs: Innovation Score (0-100) with detailed component factor ratings.
"""
from typing import Dict, Any
from utils.text_cleaner import clean_text
from utils.constants import KEYWORD_INNOVATION_SIGNALS

class InnovationService:
    def analyze_innovation(
        self,
        name: str,
        description: str,
        problem: str,
        tech_stack: str,
        category: str = ""
    ) -> Dict[str, Any]:
        """Calculates innovation score (0-100) based on semantic novelty, tech signals, and uniqueness."""
        text = clean_text(f"{name} {description} {problem} {tech_stack}")
        words = set(text.split())

        # 1. Frontier Tech Keyword Signal
        high_hits = sum(1 for kw in KEYWORD_INNOVATION_SIGNALS["high"] if kw in text)
        med_hits = sum(1 for kw in KEYWORD_INNOVATION_SIGNALS["medium"] if kw in text)
        std_hits = sum(1 for kw in KEYWORD_INNOVATION_SIGNALS["standard"] if kw in text)

        frontier_score = min(40.0, (high_hits * 10.0) + (med_hits * 4.5))

        # 2. Solution Depth and Specificity (Word variety and sentence density)
        word_count = len(text.split())
        depth_score = min(25.0, (word_count / 35.0) * 20.0)

        # 3. Category frontier baseline
        cat_frontier_bonus = {
            "AI": 18, "Cybersecurity": 16, "Developer Tools": 15,
            "HealthTech": 16, "FinTech": 14, "Agriculture": 14,
            "FoodTech": 12, "EdTech": 13, "SaaS": 12, "E-Commerce": 10
        }.get(category, 14)

        # 4. Standard paradigm penalty (if it sounds like a generic directory/portal)
        penalty = min(15.0, std_hits * 3.0)

        raw_score = 35.0 + frontier_score + (depth_score * 0.5) + (cat_frontier_bonus * 0.6) - penalty
        final_score = int(round(min(max(raw_score, 25), 98)))

        # Sub-dimension metrics
        arch_novelty = round(min(max(final_score * 0.95 + (high_hits * 3), 20), 99), 1)
        uniqueness = round(min(max(final_score * 1.02 - (penalty * 1.2), 20), 99), 1)
        tech_frontier = round(min(max(30.0 + frontier_score * 1.6, 25), 98), 1)

        if final_score >= 80:
            badge = "Breakthrough Frontier"
            badge_color = "emerald"
            summary = "Highly differentiated product architecture with distinctive frontier competitive moat."
        elif final_score >= 60:
            badge = "Strong Evolutionary"
            badge_color = "blue"
            summary = "Meaningful workflow improvements with clear differentiation against legacy solutions."
        else:
            badge = "Incremental Iteration"
            badge_color = "amber"
            summary = "Standard feature iteration; recommend introducing proprietary automated data or workflow loops."

        return {
            "score": final_score,
            "badge": badge,
            "badge_color": badge_color,
            "summary": summary,
            "breakdown": {
                "architectural_novelty": arch_novelty,
                "market_uniqueness": uniqueness,
                "technology_frontier": tech_frontier
            }
        }

innovation_service = InnovationService()
