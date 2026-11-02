"""
StartupIQ - Unified AI Pipeline Orchestrator
Executes all 9 AI/ML modules in parallel / cohesive sequence:
1. Category Detection (TF-IDF + Logistic Regression)
2. Innovation Score (0-100, novelty signals)
3. Market Potential Score (0-100, Low/Med/High)
4. Technical Complexity Analyzer (Simple/Moderate/Complex + factors)
5. Success Predictor (0-100%)
6. Similar Startup Discovery (Top 5 + %)
7. SWOT Analysis (4-quadrant matrix)
8. Investor Readiness Engine (0-100 + 4 factors)
9. Startup Improvement Recommendations (5-10 actionable items)
"""
from typing import Dict, Any
from backend.services.category_service import category_service
from backend.services.innovation_service import innovation_service
from backend.services.market_service import market_service
from backend.services.complexity_service import complexity_service
from backend.services.success_service import success_service
from backend.services.similarity_service import similarity_service
from backend.services.swot_service import swot_service
from backend.services.investor_service import investor_service
from backend.services.recommendation_service import recommendation_service

class AIPipeline:
    def run_full_analysis(
        self,
        startup_name: str,
        description: str,
        problem_statement: str,
        industry: str,
        target_audience: str,
        technology_stack: str
    ) -> Dict[str, Any]:
        """Runs complete multi-module analysis across all 9 dimensions."""

        # Module 1: Category Detection
        cat_result = category_service.predict_category(
            name=startup_name,
            description=description,
            problem=problem_statement,
            tech_stack=technology_stack
        )
        detected_category = cat_result["category"]
        category_confidence = cat_result["confidence_score"]

        # Use user-specified industry if valid or fallback to predicted category
        effective_category = industry if industry and industry != "Other" else detected_category

        # Module 2: Innovation Score (0-100)
        innovation_result = innovation_service.analyze_innovation(
            name=startup_name,
            description=description,
            problem=problem_statement,
            tech_stack=technology_stack,
            category=effective_category
        )
        innovation_score = innovation_result["score"]

        # Module 3: Market Potential Engine (0-100, Low/Medium/High)
        market_result = market_service.predict_market_potential(
            category=effective_category,
            target_audience=target_audience,
            problem=problem_statement,
            description=description,
            tech_stack=technology_stack
        )
        market_score = market_result["score"]
        market_tier = market_result["tier"]

        # Module 4: Technical Complexity Analyzer (Simple, Moderate, Complex)
        complexity_result = complexity_service.analyze_complexity(
            tech_stack=technology_stack,
            problem=problem_statement,
            description=description,
            category=effective_category
        )
        complexity_score = complexity_result["score"]
        complexity_tier = complexity_result["tier"]
        complexity_factors = complexity_result["factors"]

        # Module 5: Success Predictor (0-100%)
        success_result = success_service.predict_success(
            innovation_score=innovation_score,
            market_score=market_score,
            complexity_score=complexity_score
        )
        success_probability = success_result["success_probability"]

        # Module 6: Similar Startup Finder (Top 5 + %)
        similar_startups = similarity_service.find_similar_startups(
            name=startup_name,
            category=effective_category,
            description=description,
            problem=problem_statement,
            audience=target_audience,
            tech_stack=technology_stack,
            top_k=5
        )

        # Module 7: SWOT Generator (Strengths, Weaknesses, Opportunities, Threats)
        swot_matrix = swot_service.generate_swot(
            name=startup_name,
            category=effective_category,
            description=description,
            problem=problem_statement,
            audience=target_audience,
            tech_stack=technology_stack,
            innovation_score=innovation_score,
            market_score=market_score,
            complexity_score=complexity_score
        )

        # Module 8: Investor Readiness Engine (0-100 + 4 factors)
        investor_result = investor_service.evaluate_investor_readiness(
            innovation_score=innovation_score,
            market_score=market_score,
            complexity_score=complexity_score,
            success_probability=success_probability,
            category=effective_category
        )
        investor_readiness_score = investor_result["score"]

        # Module 9: Recommendation Engine (5-10 actionable recommendations)
        recommendations = recommendation_service.generate_recommendations(
            name=startup_name,
            category=effective_category,
            problem=problem_statement,
            description=description,
            audience=target_audience,
            tech_stack=technology_stack,
            innovation_score=innovation_score,
            market_score=market_score,
            complexity_score=complexity_score,
            success_probability=success_probability
        )

        # Composite overall score
        overall_score = round((
            innovation_score * 0.25 +
            market_score * 0.25 +
            success_probability * 0.30 +
            investor_readiness_score * 0.20
        ), 1)

        return {
            "startup_name": startup_name,
            "category": effective_category,
            "detected_category": detected_category,
            "category_confidence": category_confidence,
            "category_details": cat_result,
            "overall_score": overall_score,
            "innovation_score": innovation_score,
            "innovation_details": innovation_result,
            "market_score": market_score,
            "market_tier": market_tier,
            "market_details": market_result,
            "complexity_score": complexity_score,
            "complexity_tier": complexity_tier,
            "complexity_factors": complexity_factors,
            "complexity_details": complexity_result,
            "success_probability": success_probability,
            "success_details": success_result,
            "investor_readiness_score": investor_readiness_score,
            "investor_readiness_data": investor_result,
            "swot_analysis": swot_matrix,
            "recommendations": recommendations,
            "similar_startups": similar_startups
        }

ai_pipeline = AIPipeline()
