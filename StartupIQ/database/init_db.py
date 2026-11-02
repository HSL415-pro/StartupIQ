"""
StartupIQ Database Initialization Script
Initializes SQLite database schemas for users, startup_ideas, analysis_results, analysis_history.
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.db_manager import init_tables
from database.connection import DB_PATH

def init_database():
    print(f"[Database] Initializing SQLite database at {DB_PATH}...")
    init_tables()
    print("[Database] Successfully created tables: users, startup_ideas, analysis_results, analysis_history.")

if __name__ == "__main__":
    init_database()
