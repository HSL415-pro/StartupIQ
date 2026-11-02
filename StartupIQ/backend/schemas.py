"""
StartupIQ - Pydantic Request & Response Schemas
Defines structured input validation and response typing for all FastAPI endpoints.
"""
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    startup_name: str = Field(..., min_length=2, max_length=150, example="NeuroFlow")
    description: str = Field(..., min_length=10, example="An autonomous agent orchestration engine with self-healing feedback loops.")
    problem_statement: str = Field(..., min_length=10, example="Enterprises struggle to deploy and monitor autonomous multi-agent workflows.")
    industry: str = Field(default="AI", example="AI")
    target_audience: str = Field(..., min_length=3, example="Enterprise Data Engineering Teams")
    technology_stack: str = Field(..., min_length=3, example="Python, PyTorch, LangChain, FastAPI, Redis, Kubernetes")

class PredictCategoryRequest(BaseModel):
    startup_name: str = Field(..., example="AuraMed")
    description: str = Field(..., example="Ambient clinical scribe transcribing patient dialogues into structured EHR notes.")
    problem_statement: str = Field(..., example="Primary care physicians spend 50% of time typing EHR clinical notes.")
    technology_stack: Optional[str] = Field(default="", example="Python, PyTorch, Whisper, FastAPI, React")

class PredictMarketRequest(BaseModel):
    category: str = Field(..., example="FinTech")
    target_audience: str = Field(..., example="Cross-border Freelancers & SMBs")
    problem_statement: str = Field(..., example="Hidden FX spreads and high wire transaction fees on global invoices.")
    description: str = Field(..., example="Multi-currency virtual treasury with instant localized settlement.")
    technology_stack: Optional[str] = Field(default="", example="Go, React, PostgreSQL, Kafka")

class PredictComplexityRequest(BaseModel):
    technology_stack: str = Field(..., example="Rust, eBPF, Kubernetes, ClickHouse, WebAssembly")
    problem_statement: str = Field(..., example="Distributed tracing latency bottlenecks in high-throughput microservices.")
    description: str = Field(..., example="Zero-overhead observability sensor capturing kernel-level network packets.")
    category: Optional[str] = Field(default="Developer Tools", example="Developer Tools")

class PredictSuccessRequest(BaseModel):
    innovation_score: float = Field(..., ge=0, le=100, example=82.0)
    market_score: float = Field(..., ge=0, le=100, example=78.0)
    complexity_score: float = Field(..., ge=0, le=100, example=65.0)

class InvestorReadinessRequest(BaseModel):
    innovation_score: float = Field(..., ge=0, le=100, example=85.0)
    market_score: float = Field(..., ge=0, le=100, example=80.0)
    complexity_score: float = Field(..., ge=0, le=100, example=60.0)
    success_probability: float = Field(..., ge=0, le=100, example=75.0)
    category: Optional[str] = Field(default="AI", example="AI")

class GenerateSwotRequest(BaseModel):
    startup_name: str = Field(..., example="AgriSense")
    category: str = Field(default="Agriculture", example="Agriculture")
    description: str = Field(..., example="Satellite and soil sensor mesh network automating precision irrigation.")
    problem_statement: str = Field(..., example="Catastrophic groundwater depletion and uncalibrated drip irrigation timers.")
    target_audience: str = Field(..., example="Commercial Orchard Owners")
    technology_stack: str = Field(..., example="Python, LoRaWAN, Flutter, PostgreSQL")
    innovation_score: Optional[float] = Field(default=75.0)
    market_score: Optional[float] = Field(default=72.0)
    complexity_score: Optional[float] = Field(default=55.0)

class RecommendationsRequest(BaseModel):
    startup_name: str = Field(..., example="CyberFort")
    category: str = Field(default="Cybersecurity", example="Cybersecurity")
    problem_statement: str = Field(..., example="10,000+ daily noisy SIEM alerts burning out SOC analysts.")
    description: str = Field(..., example="Autonomous SOC co-pilot triaging and remediating high-fidelity security alerts.")
    target_audience: str = Field(..., example="Enterprise SOC & Incident Response Teams")
    technology_stack: str = Field(..., example="Rust, Python, FastAPI, ClickHouse, Docker")
    innovation_score: Optional[float] = Field(default=84.0)
    market_score: Optional[float] = Field(default=82.0)
    complexity_score: Optional[float] = Field(default=70.0)
    success_probability: Optional[float] = Field(default=76.0)

class SimilarStartupsRequest(BaseModel):
    startup_name: str = Field(..., example="EduCraft")
    category: str = Field(default="EdTech", example="EdTech")
    description: str = Field(..., example="Interactive coding simulator placing students into real-world debugging incidents.")
    problem_statement: str = Field(..., example="Bootcamp graduates lack production debugging intuition.")
    target_audience: Optional[str] = Field(default="Aspiring Software Engineers", example="Aspiring Software Engineers")
    technology_stack: Optional[str] = Field(default="TypeScript, React, Docker, WebGL", example="TypeScript, React, Docker, WebGL")
    top_k: Optional[int] = Field(default=5, ge=1, le=20)
