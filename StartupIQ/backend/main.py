"""
StartupIQ - Production FastAPI Application
Complete API service implementing all 9 AI/ML modules, SQLite persistence,
analytics endpoints, and CORS middleware.
"""
import sys
from pathlib import Path
from contextlib import asynccontextmanager

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.config import settings
from backend.schemas import (
    AnalyzeRequest,
    PredictCategoryRequest,
    PredictMarketRequest,
    PredictComplexityRequest,
    PredictSuccessRequest,
    InvestorReadinessRequest,
    GenerateSwotRequest,
    RecommendationsRequest,
    SimilarStartupsRequest
)
from backend.services.ai_pipeline import ai_pipeline
from backend.services.category_service import category_service
from backend.services.market_service import market_service
from backend.services.complexity_service import complexity_service
from backend.services.success_service import success_service
from backend.services.similarity_service import similarity_service
from backend.services.swot_service import swot_service
from backend.services.investor_service import investor_service
from backend.services.recommendation_service import recommendation_service
from database.db_manager import (
    init_tables,
    save_idea,
    save_analysis,
    get_analysis_by_id,
    get_all_history,
    delete_history_entry,
    get_dashboard_metrics
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on startup
    init_tables()
    print("[StartupIQ] Database initialized & models ready.")
    yield
    print("[StartupIQ] Application shutdown gracefully.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=f"{settings.TAGLINE} - Multi-Module AI/ML Analysis API",
    version=settings.VERSION,
    lifespan=lifespan
)

# Enable CORS for React frontend & external clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================================================================
# 1. CORE PIPELINE ANALYSIS ENDPOINT
# ==============================================================================

@app.post("/analyze", tags=["Analysis"])
@app.post("/api/analyze", tags=["Analysis"])
async def analyze_startup_idea(payload: AnalyzeRequest):
    """
    Executes all 9 AI/ML modules on the submitted startup idea,
    saves the idea and results to SQLite, and returns the comprehensive report.
    """
    try:
        # Step 1: Execute full AI pipeline
        analysis_result = ai_pipeline.run_full_analysis(
            startup_name=payload.startup_name,
            description=payload.description,
            problem_statement=payload.problem_statement,
            industry=payload.industry,
            target_audience=payload.target_audience,
            technology_stack=payload.technology_stack
        )

        # Step 2: Persist into database
        idea_id = save_idea(
            startup_name=payload.startup_name,
            description=payload.description,
            problem_statement=payload.problem_statement,
            industry=payload.industry,
            target_audience=payload.target_audience,
            technology_stack=payload.technology_stack,
            user_id=1
        )

        analysis_id = save_analysis(idea_id=idea_id, analysis_data=analysis_result)
        analysis_result["id"] = analysis_id
        analysis_result["idea_id"] = idea_id

        return {
            "status": "success",
            "message": "Analysis completed and saved successfully.",
            "data": analysis_result
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Analysis pipeline error: {str(e)}")


# ==============================================================================
# 2. INDIVIDUAL AI MODULE ENDPOINTS
# ==============================================================================

@app.post("/predict-category", tags=["AI Modules"])
@app.post("/api/predict-category", tags=["AI Modules"])
async def predict_category_endpoint(payload: PredictCategoryRequest):
    """Module 1: Category Detection (TF-IDF + Logistic Regression)."""
    res = category_service.predict_category(
        name=payload.startup_name,
        description=payload.description,
        problem=payload.problem_statement,
        tech_stack=payload.technology_stack or ""
    )
    return {"status": "success", "data": res}


@app.post("/predict-market", tags=["AI Modules"])
@app.post("/api/predict-market", tags=["AI Modules"])
async def predict_market_endpoint(payload: PredictMarketRequest):
    """Module 3: Market Potential Engine (Score 0-100, Low/Medium/High)."""
    res = market_service.predict_market_potential(
        category=payload.category,
        target_audience=payload.target_audience,
        problem=payload.problem_statement,
        description=payload.description,
        tech_stack=payload.technology_stack or ""
    )
    return {"status": "success", "data": res}


@app.post("/predict-complexity", tags=["AI Modules"])
@app.post("/api/predict-complexity", tags=["AI Modules"])
async def predict_complexity_endpoint(payload: PredictComplexityRequest):
    """Module 4: Technical Complexity Analyzer (Simple, Moderate, Complex + factors)."""
    res = complexity_service.analyze_complexity(
        tech_stack=payload.technology_stack,
        problem=payload.problem_statement,
        description=payload.description,
        category=payload.category or ""
    )
    return {"status": "success", "data": res}


@app.post("/predict-success", tags=["AI Modules"])
@app.post("/api/predict-success", tags=["AI Modules"])
async def predict_success_endpoint(payload: PredictSuccessRequest):
    """Module 5: Success Predictor (Success Probability 0-100%)."""
    res = success_service.predict_success(
        innovation_score=payload.innovation_score,
        market_score=payload.market_score,
        complexity_score=payload.complexity_score
    )
    return {"status": "success", "data": res}


@app.post("/similar-startups", tags=["AI Modules"])
@app.post("/api/similar-startups", tags=["AI Modules"])
async def similar_startups_endpoint(payload: SimilarStartupsRequest):
    """Module 6: Similar Startup Finder (TF-IDF + Cosine Similarity Top 5)."""
    res = similarity_service.find_similar_startups(
        name=payload.startup_name,
        category=payload.category,
        description=payload.description,
        problem=payload.problem_statement,
        audience=payload.target_audience or "",
        tech_stack=payload.technology_stack or "",
        top_k=payload.top_k or 5
    )
    return {"status": "success", "data": res}


@app.post("/generate-swot", tags=["AI Modules"])
@app.post("/api/generate-swot", tags=["AI Modules"])
async def generate_swot_endpoint(payload: GenerateSwotRequest):
    """Module 7: SWOT Generator (Strengths, Weaknesses, Opportunities, Threats)."""
    res = swot_service.generate_swot(
        name=payload.startup_name,
        category=payload.category,
        description=payload.description,
        problem=payload.problem_statement,
        audience=payload.target_audience,
        tech_stack=payload.technology_stack,
        innovation_score=payload.innovation_score or 70.0,
        market_score=payload.market_score or 70.0,
        complexity_score=payload.complexity_score or 50.0
    )
    return {"status": "success", "data": res}


@app.post("/investor-readiness", tags=["AI Modules"])
@app.post("/api/investor-readiness", tags=["AI Modules"])
async def investor_readiness_endpoint(payload: InvestorReadinessRequest):
    """Module 8: Investor Readiness Engine (Score 0-100 + 4 Core Factors)."""
    res = investor_service.evaluate_investor_readiness(
        innovation_score=payload.innovation_score,
        market_score=payload.market_score,
        complexity_score=payload.complexity_score,
        success_probability=payload.success_probability,
        category=payload.category or ""
    )
    return {"status": "success", "data": res}


@app.post("/recommendations", tags=["AI Modules"])
@app.post("/api/recommendations", tags=["AI Modules"])
async def recommendations_endpoint(payload: RecommendationsRequest):
    """Module 9: Recommendation Engine (5-10 actionable recommendations)."""
    res = recommendation_service.generate_recommendations(
        name=payload.startup_name,
        category=payload.category,
        problem=payload.problem_statement,
        description=payload.description,
        audience=payload.target_audience,
        tech_stack=payload.technology_stack,
        innovation_score=payload.innovation_score or 70.0,
        market_score=payload.market_score or 70.0,
        complexity_score=payload.complexity_score or 50.0,
        success_probability=payload.success_probability or 70.0
    )
    return {"status": "success", "data": res}


# ==============================================================================
# 3. DASHBOARD STATS & TRENDS ENDPOINTS
# ==============================================================================

@app.get("/dashboard-stats", tags=["Dashboard"])
@app.get("/api/dashboard-stats", tags=["Dashboard"])
async def get_dashboard_stats():
    """Returns platform-level metrics, average scores, and category distribution."""
    metrics = get_dashboard_metrics()
    return {"status": "success", "data": metrics}


@app.get("/trends", tags=["Analytics"])
@app.get("/api/trends", tags=["Analytics"])
async def get_startup_trends():
    """Returns trend distribution data for charts, radars, and comparative analytics."""
    metrics = get_dashboard_metrics()

    # Pre-calculated benchmarks across all 10 categories
    category_trends = [
        {"category": "AI", "innovation": 88, "market": 92, "success": 82, "volume": 340},
        {"category": "SaaS", "innovation": 74, "market": 86, "success": 79, "volume": 290},
        {"category": "FinTech", "innovation": 79, "market": 89, "success": 76, "volume": 260},
        {"category": "Cybersecurity", "innovation": 85, "market": 84, "success": 78, "volume": 210},
        {"category": "HealthTech", "innovation": 83, "market": 82, "success": 71, "volume": 195},
        {"category": "Developer Tools", "innovation": 86, "market": 79, "success": 75, "volume": 180},
        {"category": "E-Commerce", "innovation": 62, "market": 78, "success": 68, "volume": 220},
        {"category": "EdTech", "innovation": 69, "market": 71, "success": 66, "volume": 160},
        {"category": "Agriculture", "innovation": 76, "market": 74, "success": 70, "volume": 140},
        {"category": "FoodTech", "innovation": 68, "market": 72, "success": 64, "volume": 130}
    ]

    return {
        "status": "success",
        "data": {
            "category_trends": category_trends,
            "platform_overview": metrics
        }
    }


# ==============================================================================
# 4. HISTORY ENDPOINTS
# ==============================================================================

@app.get("/history", tags=["History"])
@app.get("/api/history", tags=["History"])
async def list_history(
    search: str = Query(None, description="Search term for startup name or summary"),
    category: str = Query(None, description="Filter by category"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    order: str = Query("desc", description="Sort direction (asc or desc)"),
    limit: int = Query(50, ge=1, le=100)
):
    """Retrieves paginated and filtered historical analysis records."""
    records = get_all_history(
        search=search,
        category=category,
        sort_by=sort_by,
        order=order,
        limit=limit
    )
    return {"status": "success", "data": records, "total": len(records)}


@app.get("/history/{analysis_id}", tags=["History"])
@app.get("/api/history/{analysis_id}", tags=["History"])
async def get_history_detail(analysis_id: int):
    """Retrieves the complete analysis details for a given analysis ID."""
    res = get_analysis_by_id(analysis_id)
    if not res:
        raise HTTPException(status_code=404, detail="Analysis record not found.")
    return {"status": "success", "data": res}


@app.delete("/history/{history_id}", tags=["History"])
@app.delete("/api/history/{history_id}", tags=["History"])
async def delete_history(history_id: int):
    """Deletes an analysis history item and associated records."""
    success = delete_history_entry(history_id)
    if not success:
        raise HTTPException(status_code=404, detail="Record not found or already deleted.")
    return {"status": "success", "message": f"Analysis #{history_id} deleted successfully."}


# ==============================================================================
# 5. HEALTH & STATUS ENDPOINT
# ==============================================================================

@app.get("/health", tags=["System"])
@app.get("/api/health", tags=["System"])
async def health_check():
    """Health check endpoint for deployment monitoring."""
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "tagline": settings.TAGLINE,
        "version": settings.VERSION,
        "python_version": "3.13"
    }

# ==============================================================================
# 6. STATIC ASSETS & SPA ROUTING (OPTIONAL INTEGRATED SINGLE-PORT MODE)
# ==============================================================================
frontend_dist = PROJECT_ROOT / "frontend" / "dist"
if frontend_dist.exists():
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse

    assets_dir = frontend_dist / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(full_path: str):
        file_path = frontend_dist / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(frontend_dist / "index.html")

if __name__ == "__main__":
    import uvicorn
    print(f"Starting {settings.PROJECT_NAME} on http://{settings.HOST}:{settings.PORT}")
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
