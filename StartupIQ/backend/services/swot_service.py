"""
StartupIQ - Module 7: SWOT Generator Service
Synthesizes professional, context-rich 4-quadrant SWOT Matrix
(Strengths, Weaknesses, Opportunities, Threats) tailored to domain, tech stack, and risk profile.
"""
from typing import Dict, Any, List

class SwotService:
    def generate_swot(
        self,
        name: str,
        category: str,
        description: str,
        problem: str,
        audience: str,
        tech_stack: str,
        innovation_score: float,
        market_score: float,
        complexity_score: float
    ) -> Dict[str, List[Dict[str, str]]]:
        """Generates comprehensive contextual SWOT items for each quadrant."""

        # Strengths
        strengths = [
            {
                "title": "Tailored Vertical Wedge",
                "detail": f"Hyper-focused on solving acute friction for {audience}, avoiding the generic pitfalls of horizontal incumbents."
            },
            {
                "title": "Modern Agile Tech Stack",
                "detail": f"Leverages contemporary framework ({tech_stack[:45]}...) enabling faster iteration velocity than legacy systems."
            }
        ]
        if innovation_score >= 70:
            strengths.append({
                "title": "High Algorithmic Defensibility",
                "detail": "Novel workflow and proprietary data processing mechanisms establish an early technical moat."
            })
        else:
            strengths.append({
                "title": "Lean Delivery Architecture",
                "detail": "Pragmatic technical footprint allows rapid proof-of-concept deployment with minimal cloud overhead."
            })
        strengths.append({
            "title": "Direct Problem-Solution Alignment",
            "detail": f"Directly addresses core pain point: '{problem[:90]}...'."
        })

        # Weaknesses
        weaknesses = [
            {
                "title": "Early Distribution Friction",
                "detail": f"Zero existing brand equity in {category}; requires proactive outbound sales or high-velocity content marketing to seed initial cohorts."
            },
            {
                "title": "Nascent Proprietary Data Moat",
                "detail": "Early deployments lack historical flywheel telemetry; fine-tuning relies on initial user feedback loops."
            }
        ]
        if complexity_score >= 65:
            weaknesses.append({
                "title": "High Engineering & Maintenance Overhead",
                "detail": "Advanced architecture increases initial runway burn and demands specialized engineering talent."
            })
        else:
            weaknesses.append({
                "title": "Low Barrier to Feature Mimicry",
                "detail": "Core workflow can be approximated by well-funded incumbents if customer switching barriers remain low."
            })

        # Opportunities
        opportunities = [
            {
                "title": f"Secular Tailwinds in {category}",
                "detail": f"Rising enterprise budgets and workflow modernization across {category} create fertile expansion territory."
            },
            {
                "title": "Adjacent Workflow Monopolization",
                "detail": f"Natural expansion opportunity from solving immediate problem into full end-to-end management cockpit for {audience}."
            },
            {
                "title": "Predictive AI & Automation Upsell",
                "detail": "Transforming passive record-keeping into autonomous decision-making commands premium B2B enterprise contract pricing."
            },
            {
                "title": "Global Market Penetration",
                "detail": "Digital delivery model enables frictionless cross-border customer acquisition without physical deployment friction."
            }
        ]

        # Threats
        threats = [
            {
                "title": "Incumbent Bundling & Fast-Follow",
                "detail": f"Established enterprise suites could integrate lightweight versions of this feature into existing subscription bundles."
            },
            {
                "title": "Customer Procurement Latency",
                "detail": f"Enterprise decision-makers in {audience} may impose lengthy 6-9 month security and compliance evaluation cycles."
            }
        ]
        if category in ["HealthTech", "FinTech", "Cybersecurity"]:
            threats.append({
                "title": "Regulatory & Audit Compliance Shifts",
                "detail": "Evolving statutory regulations (GDPR, HIPAA, SOC2 Type II, Open Banking) could mandate unexpected architectural audits."
            })
        else:
            threats.append({
                "title": "Customer Acquisition Cost (CAC) Inflation",
                "detail": "Ad network saturation in competitive digital channels could compress early unit economics."
            })

        return {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "opportunities": opportunities,
            "threats": threats
        }

swot_service = SwotService()
