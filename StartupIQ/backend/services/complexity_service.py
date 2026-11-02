"""
StartupIQ - Module 4: Technical Complexity Analyzer Service
Analyzes technology stack, architectural requirements, regulatory constraints, and algorithmic depth.
Outputs: Classification (Simple, Moderate, Complex), score (0-100), and detailed contributing factors.
"""
from typing import Dict, Any, List
from utils.text_cleaner import clean_text
from utils.scoring import classify_complexity
from utils.constants import TECH_COMPLEXITY_KEYWORDS

class ComplexityService:
    def analyze_complexity(
        self,
        tech_stack: str,
        problem: str,
        description: str,
        category: str = ""
    ) -> Dict[str, Any]:
        """Analyzes engineering overhead, infrastructure hurdles, and architectural complexity."""
        text = clean_text(f"{tech_stack} {problem} {description} {category}")

        factors: List[Dict[str, Any]] = []
        score = 30.0  # Base level

        # 1. AI/ML Deep Inference Check
        ai_terms = ["pytorch", "tensorflow", "cuda", "onnx", "triton", "llm", "diffusion", "rag", "vector", "embedding"]
        matched_ai = [t for t in ai_terms if t in text]
        if matched_ai:
            score += 18.0
            factors.append({
                "factor": "AI/ML Infrastructure & Model Inferencing",
                "impact": "High",
                "details": f"Leverages deep learning workloads ({', '.join(matched_ai[:3])}) demanding GPU orchestration, quantization, and context-window latency guarantees.",
                "color": "rose"
            })

        # 2. Real-Time Streaming & High Throughput
        stream_terms = ["kafka", "clickhouse", "webrtc", "websockets", "mqtt", "lorawan", "ebpf", "redis"]
        matched_stream = [t for t in stream_terms if t in text]
        if matched_stream:
            score += 14.0
            factors.append({
                "factor": "Low-Latency Event Streaming & Real-Time Telemetry",
                "impact": "High" if len(matched_stream) > 1 else "Medium",
                "details": f"Requires high-concurrency event-driven pipeline ({', '.join(matched_stream[:3])}) for sub-second telemetry and state synchronization.",
                "color": "indigo"
            })

        # 3. Regulatory & Strict Compliance
        comp_terms = ["hipaa", "fhir", "hl7", "pci", "gdpr", "soc2", "biometric", "finance", "medical", "banking"]
        matched_comp = [t for t in comp_terms if t in text]
        if matched_comp:
            score += 15.0
            factors.append({
                "factor": "Regulatory Compliance & Cryptographic Data Isolation",
                "impact": "High",
                "details": f"Involves sensitive domain compliance ({', '.join(matched_comp[:3])}) necessitating zero-trust audit trails and strict encryption at rest.",
                "color": "purple"
            })

        # 4. Distributed Systems & Multi-Cloud
        dist_terms = ["kubernetes", "docker", "microservices", "grpc", "temporal", "multi-region", "rust", "go"]
        matched_dist = [t for t in dist_terms if t in text]
        if matched_dist:
            score += 12.0
            factors.append({
                "factor": "Distributed Microservice & Cloud-Native Topology",
                "impact": "Medium",
                "details": f"Architected with containerized microservices ({', '.join(matched_dist[:3])}) requiring service-mesh routing and distributed failure recovery.",
                "color": "blue"
            })

        # 5. Core Web / Standard CRUD stack
        simple_terms = ["wordpress", "shopify", "firebase", "airtable", "nocode", "bubble", "react", "html"]
        matched_simple = [t for t in simple_terms if t in text]
        if matched_simple and not matched_ai and not matched_stream:
            score -= 10.0
            factors.append({
                "factor": "Standard Web MVC & Off-the-Shelf Integrations",
                "impact": "Low",
                "details": "Standard application patterns allowing rapid prototyping with minimal bespoke infrastructure overhead.",
                "color": "emerald"
            })

        # Category intrinsic complexity adjustments
        cat_adjustments = {
            "HealthTech": 12, "Cybersecurity": 12, "AI": 10,
            "Developer Tools": 8, "FinTech": 8, "Agriculture": 6,
            "SaaS": 2, "FoodTech": 2, "EdTech": 0, "E-Commerce": -2
        }
        score += cat_adjustments.get(category, 0)

        # Ensure at least 3 informative factors
        if len(factors) < 3:
            factors.append({
                "factor": "Data Persistence & Multi-Tenant Data Modeling",
                "impact": "Medium",
                "details": "Relational or document store indexing, schema migration strategies, and tenant-level authorization filters.",
                "color": "sky"
            })
        if len(factors) < 3:
            factors.append({
                "factor": "Frontend Client State & Visual Rendering Engine",
                "impact": "Low",
                "details": "Modern reactive UI pipeline with optimistic rendering, client caching, and responsive device adaptations.",
                "color": "amber"
            })

        final_score = int(round(min(max(score, 18), 98)))
        tier = classify_complexity(final_score)

        timeline_map = {
            "Simple": "3 - 6 Weeks (1-2 Engineers)",
            "Moderate": "2 - 4 Months (2-4 Engineers)",
            "Complex": "5 - 9 Months (4-8 Specialized Engineers)"
        }

        return {
            "score": final_score,
            "tier": tier,
            "estimated_timeline": timeline_map[tier],
            "factors": factors,
            "summary": f"{tier} technical profile. {len(factors)} structural engineering factors identified."
        }

complexity_service = ComplexityService()
