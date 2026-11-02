"""
StartupIQ Database Connection and Session Handling
Built on Python's native sqlite3 engine with thread-safe connections and dict row factories.
"""
import sqlite3
import threading
from pathlib import Path
from contextlib import contextmanager

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_DIR = PROJECT_ROOT / "database"
DB_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / "startupiq.db"

_local = threading.local()

def get_connection() -> sqlite3.Connection:
    """Returns a thread-local SQLite connection with Row factory enabled."""
    conn = getattr(_local, "connection", None)
    if conn is None:
        conn = sqlite3.connect(
            str(DB_PATH),
            check_same_thread=False,
            timeout=30.0
        )
        conn.row_factory = sqlite3.Row
        # Enable foreign key constraints and WAL mode for high concurrency
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        _local.connection = conn
    return conn

@contextmanager
def get_db():
    """Context manager for database transactions."""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
