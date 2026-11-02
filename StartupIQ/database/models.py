"""
StartupIQ SQLAlchemy Database Models
Defines schema for users, startup_ideas, analysis_results, and analysis_history.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=True)
    name = Column(String(255), default="Founder")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    ideas = relationship("StartupIdea", back_populates="user", cascade="all, delete-orphan")


class StartupIdea(Base):
    __tablename__ = "startup_ideas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    startup_name = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=False)
    problem_statement = Column(Text, nullable=False)
    industry = Column(String(100), default="AI")
    target_audience = Column(String(255), nullable=False)
    technology_stack = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="ideas")
    result = relationship("AnalysisResult", back_populates="idea", uselist=False, cascade="all, delete-orphan")
    history_entries = relationship("AnalysisHistory", back_populates="idea", cascade="all, delete-orphan")


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey("startup_ideas.id"), unique=True, nullable=False)

    # Category Detection
    category = Column(String(100), nullable=False)
    category_confidence = Column(Float, nullable=False)

    # Core Metric Scores
    innovation_score = Column(Float, nullable=False)
    market_score = Column(Float, nullable=False)
    market_tier = Column(String(50), nullable=False)
    complexity_score = Column(Float, nullable=False)
    complexity_tier = Column(String(50), nullable=False)
    complexity_factors = Column(JSON, nullable=False)
    success_probability = Column(Float, nullable=False)

    # Investor Readiness
    investor_readiness_score = Column(Float, nullable=False)
    investor_readiness_data = Column(JSON, nullable=False)

    # Rich AI Outputs
    swot_analysis = Column(JSON, nullable=False)
    recommendations = Column(JSON, nullable=False)
    similar_startups = Column(JSON, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    idea = relationship("StartupIdea", back_populates="result")
    history_entry = relationship("AnalysisHistory", back_populates="result", uselist=False, cascade="all, delete-orphan")


class AnalysisHistory(Base):
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey("startup_ideas.id"), nullable=False)
    analysis_id = Column(Integer, ForeignKey("analysis_results.id"), nullable=False)

    startup_name = Column(String(255), index=True, nullable=False)
    category = Column(String(100), nullable=False)
    overall_score = Column(Float, nullable=False)
    success_probability = Column(Float, nullable=False)
    investor_readiness_score = Column(Float, nullable=False)
    summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    idea = relationship("StartupIdea", back_populates="history_entries")
    result = relationship("AnalysisResult", back_populates="history_entry")
