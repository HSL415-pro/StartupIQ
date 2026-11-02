"""
StartupIQ Backend Configuration & Environment Settings
"""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

class Settings:
    PROJECT_NAME: str = "StartupIQ"
    TAGLINE: str = "AI-Powered Startup Idea Analyzer"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
    CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "*"
    ]

settings = Settings()
