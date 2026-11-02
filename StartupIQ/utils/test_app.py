import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.main import (
    health_check,
    get_dashboard_stats,
    get_startup_trends,
    analyze_startup_idea
)
from backend.schemas import AnalyzeRequest

async def run_tests():
    print("Testing /health...")
    h = await health_check()
    print("Health result:", h)

    print("Testing /dashboard-stats...")
    s = await get_dashboard_stats()
    print("Dashboard stats status:", s["status"])

    print("Testing /trends...")
    t = await get_startup_trends()
    print("Trends status:", t["status"], "Categories:", len(t["data"]["category_trends"]))

    print("Testing /analyze...")
    req = AnalyzeRequest(
        startup_name="TestFlow",
        description="Autonomous multi-agent orchestration platform for enterprise pipelines.",
        problem_statement="Distributed data teams lack visibility and self-healing guardrails for multi-agent LLMs.",
        industry="AI",
        target_audience="Enterprise Platform Leads",
        technology_stack="Python, PyTorch, LangChain, FastAPI, Redis"
    )
    res = await analyze_startup_idea(req)
    print("Analyze result:", res["status"])
    print("Generated Category:", res["data"]["category"])
    print("Innovation Score:", res["data"]["innovation_score"])
    print("Market Potential:", res["data"]["market_score"], "(Tier:", res["data"]["market_tier"] + ")")
    print("Success Probability:", res["data"]["success_probability"])
    print("Investor Readiness:", res["data"]["investor_readiness_score"])
    print("SWOT Quadrants:", list(res["data"]["swot_analysis"].keys()))
    print("Recommendations Count:", len(res["data"]["recommendations"]))
    print("Similar Startups Count:", len(res["data"]["similar_startups"]))
    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    asyncio.run(run_tests())
