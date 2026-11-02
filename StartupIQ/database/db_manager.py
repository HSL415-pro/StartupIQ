"""
StartupIQ Database Manager
Handles data persistence, querying, history retrieval, and analytical aggregation for all tables.
"""
import json
from typing import List, Dict, Any, Optional
from database.connection import get_db

def init_tables():
    """Initializes all 4 tables in the SQLite database."""
    with get_db() as conn:
        cursor = conn.cursor()

        # Table 1: users
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            name TEXT NOT NULL DEFAULT 'Founder',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Table 2: startup_ideas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS startup_ideas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            startup_name TEXT NOT NULL,
            description TEXT NOT NULL,
            problem_statement TEXT NOT NULL,
            industry TEXT NOT NULL DEFAULT 'AI',
            target_audience TEXT NOT NULL,
            technology_stack TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
        );
        """)

        # Table 3: analysis_results
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idea_id INTEGER UNIQUE NOT NULL,
            category TEXT NOT NULL,
            category_confidence REAL NOT NULL,
            innovation_score REAL NOT NULL,
            market_score REAL NOT NULL,
            market_tier TEXT NOT NULL,
            complexity_score REAL NOT NULL,
            complexity_tier TEXT NOT NULL,
            complexity_factors TEXT NOT NULL,
            success_probability REAL NOT NULL,
            investor_readiness_score REAL NOT NULL,
            investor_readiness_data TEXT NOT NULL,
            swot_analysis TEXT NOT NULL,
            recommendations TEXT NOT NULL,
            similar_startups TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (idea_id) REFERENCES startup_ideas(id) ON DELETE CASCADE
        );
        """)

        # Table 4: analysis_history
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idea_id INTEGER NOT NULL,
            analysis_id INTEGER NOT NULL,
            startup_name TEXT NOT NULL,
            category TEXT NOT NULL,
            overall_score REAL NOT NULL,
            success_probability REAL NOT NULL,
            investor_readiness_score REAL NOT NULL,
            summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (idea_id) REFERENCES startup_ideas(id) ON DELETE CASCADE,
            FOREIGN KEY (analysis_id) REFERENCES analysis_results(id) ON DELETE CASCADE
        );
        """)

        # Seed default user if not exists
        cursor.execute("SELECT id FROM users WHERE email = 'founder@startupiq.ai';")
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO users (email, name) VALUES ('founder@startupiq.ai', 'Alex Vance');"
            )


def save_idea(
    startup_name: str,
    description: str,
    problem_statement: str,
    industry: str,
    target_audience: str,
    technology_stack: str,
    user_id: Optional[int] = 1
) -> int:
    """Inserts a new startup idea record and returns its ID."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO startup_ideas (
                user_id, startup_name, description, problem_statement,
                industry, target_audience, technology_stack
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, startup_name, description, problem_statement, industry, target_audience, technology_stack))
        return cursor.lastrowid


def save_analysis(idea_id: int, analysis_data: Dict[str, Any]) -> int:
    """Inserts an analysis result record and appends to analysis history."""
    with get_db() as conn:
        cursor = conn.cursor()

        # Serialize complex nested dicts/lists to JSON strings
        complexity_factors_json = json.dumps(analysis_data.get("complexity_factors", []))
        investor_data_json = json.dumps(analysis_data.get("investor_readiness_data", {}))
        swot_json = json.dumps(analysis_data.get("swot_analysis", {}))
        recs_json = json.dumps(analysis_data.get("recommendations", []))
        similar_json = json.dumps(analysis_data.get("similar_startups", []))

        cursor.execute("""
            INSERT INTO analysis_results (
                idea_id, category, category_confidence, innovation_score,
                market_score, market_tier, complexity_score, complexity_tier,
                complexity_factors, success_probability, investor_readiness_score,
                investor_readiness_data, swot_analysis, recommendations, similar_startups
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            idea_id,
            analysis_data["category"],
            float(analysis_data["category_confidence"]),
            float(analysis_data["innovation_score"]),
            float(analysis_data["market_score"]),
            analysis_data["market_tier"],
            float(analysis_data["complexity_score"]),
            analysis_data["complexity_tier"],
            complexity_factors_json,
            float(analysis_data["success_probability"]),
            float(analysis_data["investor_readiness_score"]),
            investor_data_json,
            swot_json,
            recs_json,
            similar_json
        ))
        analysis_id = cursor.lastrowid

        # Also insert into analysis_history
        overall = round((
            analysis_data["innovation_score"] * 0.25 +
            analysis_data["market_score"] * 0.25 +
            analysis_data["success_probability"] * 0.30 +
            analysis_data["investor_readiness_score"] * 0.20
        ), 1)

        summary = (
            f"Rated {analysis_data['category']} idea with {analysis_data['success_probability']}% success "
            f"and {analysis_data['market_tier']} market potential."
        )

        cursor.execute("""
            INSERT INTO analysis_history (
                idea_id, analysis_id, startup_name, category,
                overall_score, success_probability, investor_readiness_score, summary
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            idea_id,
            analysis_id,
            analysis_data.get("startup_name", "Startup"),
            analysis_data["category"],
            overall,
            float(analysis_data["success_probability"]),
            float(analysis_data["investor_readiness_score"]),
            summary
        ))

        return analysis_id


def get_analysis_by_id(analysis_id: int) -> Optional[Dict[str, Any]]:
    """Retrieves full analysis result joined with idea info."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                r.*,
                i.startup_name, i.description, i.problem_statement,
                i.industry, i.target_audience, i.technology_stack
            FROM analysis_results r
            JOIN startup_ideas i ON r.idea_id = i.id
            WHERE r.id = ?
        """, (analysis_id,))
        row = cursor.fetchone()
        if not row:
            return None

        res = dict(row)
        res["complexity_factors"] = json.loads(res["complexity_factors"])
        res["investor_readiness_data"] = json.loads(res["investor_readiness_data"])
        res["swot_analysis"] = json.loads(res["swot_analysis"])
        res["recommendations"] = json.loads(res["recommendations"])
        res["similar_startups"] = json.loads(res["similar_startups"])
        return res


def get_all_history(
    search: Optional[str] = None,
    category: Optional[str] = None,
    sort_by: str = "created_at",
    order: str = "desc",
    limit: int = 50
) -> List[Dict[str, Any]]:
    """Retrieves paginated and filtered historical analysis records."""
    with get_db() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM analysis_history WHERE 1=1"
        params = []

        if search:
            query += " AND (startup_name LIKE ? OR summary LIKE ?)"
            params.extend([f"%{search}%", f"%{search}%"])

        if category and category.lower() != "all":
            query += " AND category = ?"
            params.append(category)

        # Sanitize sort fields
        allowed_sorts = {
            "created_at": "created_at",
            "overall_score": "overall_score",
            "success_probability": "success_probability",
            "investor_readiness_score": "investor_readiness_score",
            "startup_name": "startup_name"
        }
        col = allowed_sorts.get(sort_by, "created_at")
        direction = "ASC" if order.lower() == "asc" else "DESC"

        query += f" ORDER BY {col} {direction} LIMIT ?"
        params.append(limit)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(r) for r in rows]


def delete_history_entry(history_id: int) -> bool:
    """Deletes a history entry and its associated analysis/idea."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT idea_id, analysis_id FROM analysis_history WHERE id = ?", (history_id,))
        row = cursor.fetchone()
        if not row:
            return False
        idea_id = row["idea_id"]
        cursor.execute("DELETE FROM startup_ideas WHERE id = ?", (idea_id,))
        return True


def get_dashboard_metrics() -> Dict[str, Any]:
    """Computes high-level platform statistics and category distribution."""
    with get_db() as conn:
        cursor = conn.cursor()

        # Total counts
        cursor.execute("SELECT COUNT(*) AS total_analyzed FROM analysis_results")
        total_analyzed = cursor.fetchone()["total_analyzed"]

        # Averages
        cursor.execute("""
            SELECT 
                AVG(innovation_score) AS avg_innovation,
                AVG(market_score) AS avg_market,
                AVG(success_probability) AS avg_success,
                AVG(investor_readiness_score) AS avg_investor
            FROM analysis_results
        """)
        avgs = cursor.fetchone()

        # Category breakdown
        cursor.execute("""
            SELECT category, COUNT(*) AS count, AVG(success_probability) as avg_success
            FROM analysis_results
            GROUP BY category
            ORDER BY count DESC
        """)
        category_stats = [dict(r) for r in cursor.fetchall()]

        # Recent 5 analyses
        cursor.execute("""
            SELECT id, startup_name, category, overall_score, success_probability, created_at
            FROM analysis_history
            ORDER BY created_at DESC
            LIMIT 5
        """)
        recent = [dict(r) for r in cursor.fetchall()]

        return {
            "total_analyzed": total_analyzed,
            "avg_innovation": round(avgs["avg_innovation"] or 0, 1),
            "avg_market": round(avgs["avg_market"] or 0, 1),
            "avg_success": round(avgs["avg_success"] or 0, 1),
            "avg_investor": round(avgs["avg_investor"] or 0, 1),
            "category_distribution": category_stats,
            "recent_analyses": recent
        }
