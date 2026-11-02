"""
StartupIQ Database Package
"""
from database.connection import get_connection, get_db, DB_PATH
from database.db_manager import (
    init_tables,
    save_idea,
    save_analysis,
    get_analysis_by_id,
    get_all_history,
    delete_history_entry,
    get_dashboard_metrics
)

__all__ = [
    "get_connection",
    "get_db",
    "DB_PATH",
    "init_tables",
    "save_idea",
    "save_analysis",
    "get_analysis_by_id",
    "get_all_history",
    "delete_history_entry",
    "get_dashboard_metrics"
]
