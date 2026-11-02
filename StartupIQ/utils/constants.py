"""
StartupIQ Constants and Static Reference Data
"""

CATEGORIES = [
    "AI",
    "SaaS",
    "FoodTech",
    "HealthTech",
    "FinTech",
    "EdTech",
    "Agriculture",
    "Cybersecurity",
    "E-Commerce",
    "Developer Tools"
]

CATEGORY_DESCRIPTIONS = {
    "AI": "Artificial Intelligence, Foundation Models, Agents, Computer Vision & NLP",
    "SaaS": "Cloud Software-as-a-Service, Enterprise Productivity & Business Operations",
    "FoodTech": "Food Supply Chain, Ghost Kitchens, AgTech Processing & Smart Dining",
    "HealthTech": "Digital Therapeutics, Remote Care, Medical Diagnostics & Clinical Trials",
    "FinTech": "Modern Banking, Payments, Micro-Credit, WealthTech & Algorithmic Trading",
    "EdTech": "Adaptive Learning, Automated Grading, Skills Training & Gamified Education",
    "Agriculture": "Smart Farming, Soil Telemetry, Precision Drone Mapping & Bio-Nutrients",
    "Cybersecurity": "Zero-Trust, Cloud IAM, Threat Telemetry, SIEM Automation & Cryptography",
    "E-Commerce": "Direct-to-Consumer, Headless Commerce, Live Shopping & 3D Fitting",
    "Developer Tools": "CI/CD, Distributed Tracing, Compilers, eBPF & Design-to-Code Engines"
}

MARKET_TIERS = {
    "LOW": {"min": 0, "max": 44, "label": "Niche Market / High Customer Acquisition Cost", "tag": "Low"},
    "MEDIUM": {"min": 45, "max": 74, "label": "Viable Growing Market / Stable Demand", "tag": "Medium"},
    "HIGH": {"min": 75, "max": 100, "label": "Massive TAM / Rapid Sector Headwinds", "tag": "High"}
}

COMPLEXITY_TIERS = {
    "Simple": {"min": 0, "max": 40, "description": "Rapid MVP execution feasible in 2-6 weeks with off-the-shelf tools."},
    "Moderate": {"min": 41, "max": 70, "description": "Requires multi-tenant architecture, third-party integrations, and domain expertise."},
    "Complex": {"min": 71, "max": 100, "description": "Demands proprietary algorithms, deep hardware/IoT, stringent compliance, or edge computing."}
}

KEYWORD_INNOVATION_SIGNALS = {
    "high": [
        "autonomous", "agentic", "diffusion", "reinforcement learning", "zero-knowledge",
        "ebpf", "foundation model", "multimodal", "synthetic biology", "quantum", "patented",
        "edge inferencing", "photorealistic", "proprietary algorithm", "decentralized"
    ],
    "medium": [
        "ai-driven", "automated", "cloud-native", "predictive", "real-time", "headless",
        "orchestration", "biometric", "microservices", "telemetry", "nlp", "llm"
    ],
    "standard": [
        "portal", "dashboard", "marketplace", "app", "directory", "aggregator",
        "booking", "crud", "consulting", "reselling", "matching"
    ]
}

TECH_COMPLEXITY_KEYWORDS = {
    "complex": [
        "pytorch", "tensorflow", "cuda", "ebpf", "rust", "c++", "triton", "distributed",
        "blockchain", "smart contracts", "embedded", "lorawan", "iot", "biometric",
        "fhir", "hl7", "hipaa", "pci-dss", "multi-region", "kafka", "clickhouse"
    ],
    "moderate": [
        "fastapi", "django", "node.js", "docker", "kubernetes", "postgresql", "redis",
        "graphql", "celery", "time-series", "websockets", "microservices", "stripe"
    ],
    "simple": [
        "wordpress", "shopify", "firebase", "airtable", "nocode", "bubble", "react", "html", "css"
    ]
}
