"""
StartupIQ Scoring Utilities
Provides normalization, tier classification, and investor metric calculations.
"""

def classify_market(score: float) -> str:
    """Classifies market score into Low, Medium, High tiers."""
    if score >= 75:
        return "High"
    elif score >= 45:
        return "Medium"
    return "Low"

def classify_complexity(score: float) -> str:
    """Classifies complexity score into Simple, Moderate, Complex."""
    if score >= 70:
        return "Complex"
    elif score >= 40:
        return "Moderate"
    return "Simple"

def compute_investor_readiness(innovation: float, market: float, complexity: float, success_prob: float) -> dict:
    """
    Computes Investor Readiness Score (0-100) and breakdowns across 4 core factors:
    1. Innovation
    2. Scalability
    3. Market Size
    4. Technical Feasibility
    """
    # Factor 1: Innovation (0-100)
    factor_innovation = round(float(innovation), 1)

    # Factor 2: Scalability (derived from Market potential + execution headroom)
    # SaaS/Cloud ideas scale easily, high complexity slightly drags initial scalability
    scalability_raw = (market * 0.7) + ((100 - (complexity * 0.4)) * 0.3)
    factor_scalability = round(float(min(max(scalability_raw, 10), 99)), 1)

    # Factor 3: Market Size (closely tied to market potential score)
    market_size_raw = (market * 0.85) + (success_prob * 0.15)
    factor_market_size = round(float(min(max(market_size_raw, 10), 99)), 1)

    # Factor 4: Technical Feasibility
    # Feasibility is high if complexity is manageable and innovation is grounded
    # moderate complexity (40-65) is optimal for high defensibility
    if complexity <= 40:
        feasibility_raw = 88.0 - (complexity * 0.2)
    elif complexity <= 70:
        feasibility_raw = 85.0 - ((complexity - 40) * 0.4)
    else:
        feasibility_raw = 73.0 - ((complexity - 70) * 0.7)
    factor_feasibility = round(float(min(max(feasibility_raw, 25), 98)), 1)

    # Overall Investor Readiness Score
    overall = (
        factor_innovation * 0.25 +
        factor_scalability * 0.30 +
        factor_market_size * 0.25 +
        factor_feasibility * 0.20
    )
    overall_score = int(round(min(max(overall, 15), 98)))

    if overall_score >= 80:
        tier = "Series A / Institutional Ready"
        color = "emerald"
    elif overall_score >= 65:
        tier = "Seed / Angel Ready"
        color = "blue"
    elif overall_score >= 50:
        tier = "Pre-Seed / Accelerator Candidate"
        color = "amber"
    else:
        tier = "Ideation / Needs Validation"
        color = "rose"

    return {
        "score": overall_score,
        "tier": tier,
        "color": color,
        "factors": {
            "innovation": factor_innovation,
            "scalability": factor_scalability,
            "market_size": factor_market_size,
            "technical_feasibility": factor_feasibility
        }
    }
