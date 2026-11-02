"""
StartupIQ - Module 9: Recommendation Engine Service
Generates 5-10 prioritized, actionable startup improvement recommendations spanning
Product, GTM, Defensibility, Unit Economics, and Technical Execution.
"""
from typing import List, Dict, Any

class RecommendationService:
    def generate_recommendations(
        self,
        name: str,
        category: str,
        problem: str,
        description: str,
        audience: str,
        tech_stack: str,
        innovation_score: float,
        market_score: float,
        complexity_score: float,
        success_probability: float
    ) -> List[Dict[str, Any]]:
        """Generates 6-8 tailored, high-impact recommendations."""
        recs: List[Dict[str, Any]] = []

        # 1. Product & Architecture Wedge (Always critical)
        recs.append({
            "id": 1,
            "title": f"Narrow Initial Customer Wedge to 10 Ideal {audience} Cohorts",
            "category": "Go-To-Market",
            "priority": "High",
            "timeframe": "Days 1 - 14",
            "description": f"Avoid marketing horizontally. Conduct 15 structured problem interviews specifically with {audience} to pinpoint the single painful manual workflow that triggers urgent budget approval.",
            "impact": "Reduces customer acquisition trial cycle by 50%"
        })

        # 2. Defensibility & Proprietary Data Flywheel
        if innovation_score < 75:
            recs.append({
                "id": 2,
                "title": "Engineer a Closed-Loop Data Feedback Flywheel",
                "category": "Defensibility",
                "priority": "High",
                "timeframe": "Month 1 - 2",
                "description": f"Standard CRUD tooling risks fast incumbent replication. Capture telemetry on how {audience} interact with the product to build proprietary heuristics or fine-tuned model weights.",
                "impact": "Creates sustainable switching barriers and IP moat"
            })
        else:
            recs.append({
                "id": 2,
                "title": "Document and Benchmark Proprietary IP Benchmarks",
                "category": "Defensibility",
                "priority": "Medium",
                "timeframe": "Month 1 - 2",
                "description": f"Publish reproducible performance benchmarks demonstrating your proprietary approach outperforming standard open-source baseline models by at least 3x in speed or accuracy.",
                "impact": "Establishes authoritative category leadership"
            })

        # 3. Technical De-risking based on complexity
        if complexity_score > 65:
            recs.append({
                "id": 3,
                "title": "Decouple Deep Infrastructure into Serverless Micro-Modules",
                "category": "Engineering",
                "priority": "High",
                "timeframe": "Sprint 1",
                "description": f"Given the high architectural complexity in {tech_stack[:35]}, build an MVP using managed serverless inference and hosted vector stores before committing to bare-metal Kubernetes clusters.",
                "impact": "Saves 3 months of dev runway and $40K cloud spend"
            })
        else:
            recs.append({
                "id": 3,
                "title": "Ship Rapid Interactive Sandbox Demo Without Signup Friction",
                "category": "Product",
                "priority": "Quick Win",
                "timeframe": "Days 1 - 7",
                "description": f"Provide an interactive playground or self-service sandbox so prospective {audience} experience immediate 'Aha!' value within 60 seconds without booking a sales call.",
                "impact": "Triples inbound conversion from organic traffic"
            })

        # 4. Pricing & Monetization Strategy
        recs.append({
            "id": 4,
            "title": "Implement Value-Metric Pricing Rather Than Flat Seat Tiers",
            "category": "Monetization",
            "priority": "High",
            "timeframe": "Month 2",
            "description": f"Align billing with outcomes (e.g. per workflow automated, per transaction analyzed, or volume saved) rather than per-seat licensing, incentivizing viral internal adoption within customer organizations.",
            "impact": "Boosts Net Revenue Retention (NRR) above 125%"
        })

        # 5. Regulatory & Trust Assurance
        if category in ["HealthTech", "FinTech", "Cybersecurity"]:
            recs.append({
                "id": 5,
                "title": "Pre-Emptively Attain SOC 2 Type 1 / Domain Compliance Seal",
                "category": "Compliance",
                "priority": "High",
                "timeframe": "Months 2 - 3",
                "description": f"Enterprise procurement in {category} will veto unsigned contracts. Implement automated audit logging and zero-trust policies early to eliminate compliance deal-blockers.",
                "impact": "Prevents 4-month procurement deadlocks"
            })
        else:
            recs.append({
                "id": 5,
                "title": "Build One-Click Integration into Customer Ecosystems",
                "category": "Product",
                "priority": "Medium",
                "timeframe": "Month 2",
                "description": f"Meet {audience} inside their daily stack. Offer native webhooks and integrations into Slack, GitHub, Notion, or ERP systems to eliminate workflow friction.",
                "impact": "Reduces daily customer churn by 35%"
            })

        # 6. Investor & Metrics Traction
        recs.append({
            "id": 6,
            "title": "Establish North Star Metric: Weekly Active Workflow Executions",
            "category": "Analytics",
            "priority": "Medium",
            "timeframe": "Continuous",
            "description": "Track high-intent habituation metrics (WAU executing core action >3 times weekly). Institutional investors value sticky retention cohorts over vanity signups.",
            "impact": "Provides clear proof-of-traction for institutional seed"
        })

        # 7. Distribution Partnership Hook
        recs.append({
            "id": 7,
            "title": f"Form 2 Co-Marketing Channel Alliances in the {category} Ecosystem",
            "category": "Growth",
            "priority": "Medium",
            "timeframe": "Month 3",
            "description": f"Partner with non-competing complementary software providers servicing {audience} to co-author whitepapers, webinars, and shared marketplace app listings.",
            "impact": "Cuts blended CAC by up to 40%"
        })

        return recs

recommendation_service = RecommendationService()
