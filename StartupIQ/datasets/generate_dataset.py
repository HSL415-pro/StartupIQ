"""
StartupIQ Dataset Generator
Generates a realistic synthetic dataset of 1,200+ startups across 10 distinct categories
with realistic problem descriptions, tech stacks, audiences, and correlated evaluation scores.
"""
import random
import pandas as pd
import numpy as np
from pathlib import Path

random.seed(42)
np.random.seed(42)

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

CATEGORY_TEMPLATES = {
    "AI": {
        "prefixes": ["Neuro", "Cogni", "Synapse", "Deep", "Agentic", "Hyper", "Apex", "Tensor", "Omni", "Lumi"],
        "suffixes": ["Mind", "AI", "Intelligence", "Labs", "Core", "Brain", "Flow", "Logic", "Sense", "Matrix"],
        "problems": [
            "Enterprises struggle to deploy and monitor autonomous multi-agent workflows across legacy software without hallucinations.",
            "Customer support teams are overwhelmed by unstructured multimodal queries across audio, chat, and email channels.",
            "Data science teams waste weeks standardizing and fine-tuning open-source LLMs on proprietary domain data.",
            "Healthcare researchers lack fast multimodal generative models to simulate clinical trial molecular interactions.",
            "Legal teams spend hundreds of billable hours manually cross-checking regulatory clauses and compliance documents.",
            "Video creators spend disproportionate budgets rendering real-time photorealistic localized voice and avatar dubbing.",
            "E-commerce merchants cannot dynamically personalize 3D product visual assets and recommendations at scale.",
            "Logistics dispatchers lack predictive reinforcement learning systems to optimize real-time route rerouting."
        ],
        "solutions": [
            "an autonomous agent orchestration platform with self-healing feedback loops and deterministic governance guarantees.",
            "a multimodal context-aware assistant with sub-100ms latency and domain-adapted vector retrieval capabilities.",
            "a zero-code fine-tuning and evaluation platform featuring automated synthetic dataset generation and guardrails.",
            "a generative bio-molecular diffusion foundation model accelerating preclinical drug candidate screening by 10x.",
            "a context-aware contract intelligence platform parsing cross-border regulatory compliance in real time.",
            "a photorealistic generative video synthesis engine translating scripts into multilingual marketing assets instantly.",
            "a real-time visual recommendation engine delivering dynamic personalized 3D storefronts with edge inferencing.",
            "a reinforcement learning dispatch co-pilot cutting fleet idle times and reducing fuel emissions by 28%."
        ],
        "stacks": ["Python, PyTorch, LangChain, FastAPI, Redis, Triton Inference Server", "Python, HuggingFace, Ray, Kubernetes, Milvus, React", "FastAPI, ONNX, PostgreSQL, Celery, VectorDB, Next.js"],
        "audiences": ["Enterprise Data Teams", "Fortune 500 Customer Support", "Biotech Researchers", "Legal & Compliance Departments", "Growth Marketing Agencies"]
    },
    "SaaS": {
        "prefixes": ["Work", "Cloud", "Sync", "Task", "Omni", "Pulse", "Desk", "Flow", "Vibe", "Base"],
        "suffixes": ["Hub", "HQ", "Stack", "Sync", "Flow", "Sphere", "Ops", "Track", "Desk", "Point"],
        "problems": [
            "Remote distributed teams lose 4 hours weekly juggling fragmented asynchronous project updates and meeting notes.",
            "Mid-market finance teams suffer from manual multi-entity subscription billing reconciliation and revenue leakage.",
            "HR departments fail to track cross-border compliance, contractor payroll, and global tax withholding accurately.",
            "Customer success managers lack predictive health scoring to identify account churn risks before renewals.",
            "Field operations teams rely on paper clipboards and siloed spreadsheets for maintenance audit logging.",
            "B2B sales teams lack real-time conversational battlecards during high-stakes enterprise procurement calls.",
            "Procurement departments endure slow, opaque purchase approval workflows across distributed vendor contracts."
        ],
        "solutions": [
            "an intelligent workspace unifying asynchronous standups, AI meeting summaries, and unified action-item tracking.",
            "an automated revenue operations engine unifying multi-currency recurring billing, tax, and GAAP compliance.",
            "an all-in-one global payroll and contractor management platform with built-in statutory compliance checks.",
            "a proactive customer retention cockpit aggregating product analytics and support sentiment into early warnings.",
            "a mobile-first offline-capable field inspection suite with automated work-order generation and IoT sensor syncing.",
            "a real-time sales co-pilot surfacing relevant competitor intelligence and objection-handling scripts live.",
            "a collaborative procurement cockpit streamlining RFP evaluation, supplier contracting, and budget sign-offs."
        ],
        "stacks": ["TypeScript, React, Node.js, PostgreSQL, TailwindCSS, AWS", "Python, FastAPI, React, PostgreSQL, Docker, Redis", "Go, Next.js, GraphQL, DynamoDB, Temporal"],
        "audiences": ["Remote Knowledge Workers", "Chief Financial Officers", "Enterprise People Teams", "Customer Success Executives", "B2B Sales Organizations"]
    },
    "FoodTech": {
        "prefixes": ["Nutri", "Fresh", "Taste", "Bite", "Meal", "Urban", "Harvest", "Agro", "Green", "Pure"],
        "suffixes": ["Bite", "Kitchen", "Table", "Eats", "Fork", "Plate", "Craft", "Farm", "Roots", "Box"],
        "problems": [
            "Commercial ghost kitchens suffer from unpredictable ingredient spoilage and 30% weekly food waste.",
            "Consumers with acute dietary restrictions struggle to verify allergen safety in ghost kitchen delivery orders.",
            "Traditional indoor vertical farming struggles with exorbitant LED energy consumption and inconsistent crop yield.",
            "Restaurants suffer 35% margin erosion due to predatory third-party delivery marketplace commissions.",
            "Artisanal food producers lack cold-chain logistics traceability leading to spoilage during interstate shipping.",
            "Hospitality venues struggle to predict daily footfall causing over-staffing and food prep overproduction."
        ],
        "solutions": [
            "an AI-driven inventory replenishment engine forecasting batch demand to minimize commercial kitchen waste.",
            "a certified allergen verification platform integrating laboratory testing data with menu allergen tracing.",
            "an autonomous aeroponic vertical farming controller optimizing spectral LED lighting and micro-nutrient delivery.",
            "a direct-to-consumer decentralized restaurant ordering network offering 0% commissions and white-label loyalty.",
            "an IoT-connected smart thermal packaging system providing continuous temperature and humidity tracking in transit.",
            "a predictive restaurant demand scheduling engine aligning staff rotas and prep schedules with weather and events."
        ],
        "stacks": ["Python, FastAPI, Flutter, PostgreSQL, MQTT, AWS IoT", "React Native, Node.js, Express, MongoDB, Stripe", "Python, Django, Vue.js, TimeScaleDB, Docker"],
        "audiences": ["Ghost Kitchen Operators", "Dietary Restricted Diners", "Commercial Urban Farmers", "Independent Restaurateurs", "Artisanal Food Brands"]
    },
    "HealthTech": {
        "prefixes": ["Care", "Vital", "Pulse", "Medi", "Heal", "Bio", "Cure", "Geno", "Aura", "Cardio"],
        "suffixes": ["Care", "Health", "Sync", "Med", "Pulse", "Vitals", "Doc", "Life", "Clinic", "Path"],
        "problems": [
            "Patients with chronic hypertension experience dangerous treatment delays between quarterly physician visits.",
            "Primary care clinics spend 50% of consultation time typing clinical documentation into clunky EHR interfaces.",
            "Rural psychiatric clinics face months-long waiting lists for cognitive behavioral therapy intake triage.",
            "Radiology clinics face massive backlogs analyzing cross-sectional MRI scans for micro-fractures and nodules.",
            "Clinical research coordinators struggle to recruit ethnically representative cohorts for phase-2 trials.",
            "Post-operative orthopedic patients suffer high readmission rates due to poor physical therapy home compliance."
        ],
        "solutions": [
            "a cellular-connected continuous biometric monitoring platform alerting care teams to acute clinical anomalies.",
            "an ambient acoustic clinical scribe transcribing patient dialogues into structured HL7 and FHIR notes instantly.",
            "an evidence-based conversational CBT triage assistant supporting mental health clinics between appointments.",
            "a computer vision diagnostic co-pilot flagging subtle radiographic anomalies with 99.1% sensitivity.",
            "a decentralized clinical trial matching platform matching diverse genomic profiles to prospective studies.",
            "a smartphone camera motion-tracking rehabilitation app guiding surgical patients through recovery routines."
        ],
        "stacks": ["Python, FastAPI, PyTorch, React, HIPAA-Compliant AWS, PostgreSQL", "TypeScript, React, Node.js, FHIR API, Docker, GCP", "Python, TensorFlow, Swift, Kotlin, MongoDB"],
        "audiences": ["Chronic Disease Patients", "Primary Care Doctors", "Community Mental Health Clinics", "Radiology Networks", "Orthopedic Recovery Clinics"]
    },
    "FinTech": {
        "prefixes": ["Pay", "Fin", "Cash", "Ledger", "Vault", "Wealth", "Capital", "Mint", "Trust", "Alpha"],
        "suffixes": ["Pay", "Vault", "Capital", "Flow", "Ledger", "Fin", "Trade", "Invest", "Coin", "Shield"],
        "problems": [
            "Cross-border freelance contractors lose 6-8% of total billings to hidden FX spreads and wire transaction fees.",
            "Underbanked gig-economy workers are denied fair credit because traditional credit bureaus ignore alternative cashflow.",
            "SME exporters wait 90-120 days for accounts receivable factoring approval from conservative commercial banks.",
            "Web3 decentralized finance treasuries struggle with institutional auditability and automated tax compliance.",
            "Retail micro-investors lack algorithmic risk hedging strategies used by quantitative hedge funds.",
            "E-commerce merchants experience checkout drop-offs from fraud false-positives during international checkouts."
        ],
        "solutions": [
            "a multi-currency virtual treasury providing instant local settlement with zero FX markups across 45 countries.",
            "an alternative credit underwriting engine analyzing recurring open-banking cashflows to issue fair micro-loans.",
            "an automated supply-chain invoice factoring marketplace releasing instant working capital against verified POs.",
            "an institutional crypto treasury platform automating balance sheet reconciliation, auditing, and tax reports.",
            "a fractionalized quantitative portfolio management app executing systematic hedging strategies automatically.",
            "an adaptive fraud prevention gateway evaluating 200+ behavioral biometric indicators to slash false declines."
        ],
        "stacks": ["Go, gRPC, React, PostgreSQL, Kafka, Kubernetes", "Python, FastAPI, Scikit-Learn, React, Plaid API, AWS", "Node.js, TypeScript, PostgreSQL, Redis, Next.js, Stripe"],
        "audiences": ["Global Freelancers", "Gig-Economy Workers", "Import-Export SMEs", "Web3 Foundation Treasuries", "First-Time Retail Investors"]
    },
    "EdTech": {
        "prefixes": ["Learn", "Edu", "Skill", "Brain", "Tutor", "Mind", "Study", "Academia", "Mentor", "Scholar"],
        "suffixes": ["Hub", "Verse", "Academy", "Path", "Lab", "Flow", "Craft", "IQ", "Zone", "Camp"],
        "problems": [
            "Computer science bootcamp graduates struggle to bridge theoretical algorithms with real-world production codebases.",
            "K-12 educators spend 15 hours weekly manually grading open-ended essay assignments and providing feedback.",
            "Language learners achieve passive vocabulary recognition but freeze during spontaneous native speech.",
            "Corporate compliance training suffers from 12% employee completion rates and zero practical knowledge retention.",
            "Neurodivergent students struggle with rigid linear video curriculums that ignore individual pacing needs.",
            "Medical students lack hands-on interactive 3D anatomy simulation tools accessible on mobile devices."
        ],
        "solutions": [
            "an interactive code simulator throwing students into production-scale microservices debugging simulations.",
            "an automated pedagogical grading assistant providing contextual rubric feedback and revision suggestions.",
            "an AI-powered conversational language tutor with voice tone analysis and situational roleplay scenarios.",
            "a gamified bite-sized micro-learning platform delivering scenario-based simulations within Slack and Teams.",
            "an adaptive sensory learning platform adjusting visual contrast, pacing, and multimodal prompts dynamically.",
            "an interactive WebGL 3D surgical dissection simulator with haptic touch guidance and quiz assessments."
        ],
        "stacks": ["TypeScript, React, Node.js, WebGL, PostgreSQL, AWS", "Python, FastAPI, Next.js, Redis, Docker, TailwindCSS", "Vue.js, Python, Flask, MongoDB, WebRTC"],
        "audiences": ["Junior Software Engineers", "K-12 School Districts", "Adult Language Learners", "Enterprise HR L&D Teams", "Medical & Nursing Students"]
    },
    "Agriculture": {
        "prefixes": ["Agri", "Crop", "Terra", "Soil", "Flora", "Farm", "Verdant", "Yield", "Bio", "Harvest"],
        "suffixes": ["Sense", "Farm", "Grow", "Terra", "Yield", "Soil", "Tech", "Field", "Sync", "Crop"],
        "problems": [
            "Smallholder grain farmers lose 30% of their harvest to fungal blights caught too late for organic remediation.",
            "Commercial orchards suffer catastrophic groundwater depletion from uncalibrated drip irrigation timers.",
            "Precision drone operators struggle to stitch multispectral farm aerial imagery within acceptable turnarounds.",
            "Cattle ranchers cannot monitor herd estrus cycles and early viral infection signs across open pastures.",
            "Greenhouse managers rely on manual pest scouting resulting in widespread pesticide over-application.",
            "Agri-chemical retailers struggle to supply farmers with just-in-time micro-fertilizer formulations."
        ],
        "solutions": [
            "a smartphone leaf scanning diagnostic tool identifying 150+ crop diseases in milliseconds without internet.",
            "a satellite and soil sensor mesh network automating precision irrigation based on real evapotranspiration data.",
            "an edge-computed drone orthomosaic engine generating multispectral NDVI crop stress maps in 10 minutes.",
            "an ingestible IoT rumen bolus continuously relaying core temperature and movement metrics to the farm dashboard.",
            "an autonomous greenhouse rover utilizing microscopic imaging to target localized bio-control treatments.",
            "a hyper-local soil chemistry advisory platform recommending precision custom nutrient blends for acreage."
        ],
        "stacks": ["Python, PyTorch, Fastify, PostgreSQL, MQTT, LoRaWAN", "Flutter, Python, FastAPI, TensorFlow Lite, SQLite", "Go, React, TimeScaleDB, AWS Greengrass, Docker"],
        "audiences": ["Smallholder Farmers", "Commercial Orchard Growers", "Precision Agronomists", "Cattle Ranchers", "Commercial Greenhouse Operators"]
    },
    "Cybersecurity": {
        "prefixes": ["Cyber", "Shield", "Guard", "Sentin", "Zero", "Sec", "Fortress", "Armor", "Cipher", "Vigil"],
        "suffixes": ["Guard", "Shield", "Sec", "Defense", "Wall", "Lock", "Vault", "Trust", "Safe", "Ops"],
        "problems": [
            "Security teams are flooded with 10,000+ daily noisy SIEM alerts resulting in dangerous analyst burnout.",
            "Developers unknowingly commit secrets and API keys to public repositories causing devastating cloud breaches.",
            "Remote workforces are increasingly vulnerable to sophisticated generative voice deepfake phishing attacks.",
            "Cloud infrastructure teams suffer from IAM privilege creep across multi-cloud AWS, Azure, and GCP setups.",
            "Open source software dependencies introduce zero-day supply-chain vulnerabilities into production builds.",
            "Critical infrastructure SCADA systems lack air-gapped intrusion detection against nation-state malware."
        ],
        "solutions": [
            "an autonomous SOC co-pilot triaging, investigating, and remediating high-fidelity security alerts in seconds.",
            "an automated pre-commit secret scanner with decentralized token revocation and cryptographic rotation.",
            "a real-time acoustic biometric defense layer detecting synthetic deepfakes during enterprise calls.",
            "a continuous zero-trust cloud entitlement management platform auto-revoking dormant IAM permissions.",
            "an automated software bill of materials (SBOM) analyzer verifying package provenance and binary integrity.",
            "an anomaly-detection network sensor monitoring industrial control protocol telemetry without cloud exposure."
        ],
        "stacks": ["Rust, Python, FastAPI, React, ClickHouse, Docker", "Go, React, PostgreSQL, eBPF, Kubernetes, Redis", "Python, PyTorch, Next.js, Elasticsearch, Kafka"],
        "audiences": ["Enterprise SOC Teams", "DevOps & Platform Engineers", "Corporate Risk Officers", "Cloud Architecture Teams", "Industrial Infrastructure Operators"]
    },
    "E-Commerce": {
        "prefixes": ["Shop", "Cart", "Market", "Store", "Omni", "Buy", "Retail", "Brand", "Trade", "Vend"],
        "suffixes": ["ify", "Hub", "Flow", "Cart", "Wave", "Bay", "Mart", "Drop", "Zone", "Nest"],
        "problems": [
            "Independent Shopify brands experience 70% cart abandonment due to unexpected shipping fees and clunky checkouts.",
            "Direct-to-consumer apparel brands suffer 35% return rates due to inaccurate online sizing and fabric fit.",
            "Multichannel sellers struggle to sync real-time inventory counts across Amazon, TikTok Shop, and brick-and-mortar.",
            "Wholesale suppliers waste days managing manual PDF purchase orders and reconciling B2B trade credit.",
            "Live-stream sellers cannot keep up with thousands of live chat buying queries and coupon requests.",
            "Subscription box brands experience high subscriber churn due to static, unpersonalized monthly curation."
        ],
        "solutions": [
            "a one-click universal checkout widget optimizing shipping rates and offering localized interest-free installment options.",
            "an AI virtual fitting room rendering 3D garments onto customer phone scans with 95% accurate measurements.",
            "a headless multichannel inventory orchestration hub synchronizing order fulfillment across all channels in real time.",
            "a digital B2B wholesale marketplace automating credit risk assessment, trade terms, and invoicing.",
            "an automated live-commerce chatbot pinning promotional products and processing in-stream checkouts.",
            "a dynamic preference curation engine predicting monthly subscriber tastes to slash churn by half."
        ],
        "stacks": ["TypeScript, Next.js, Node.js, PostgreSQL, Stripe, Redis", "Python, FastAPI, Three.js, React, MongoDB, AWS", "Ruby on Rails, React, GraphQL, Sidekiq, Redis, TailwindCSS"],
        "audiences": ["DTC Brand Founders", "Apparel Retailers", "Multichannel E-commerce Sellers", "B2B Wholesale Distributors", "Live Shopping Creators"]
    },
    "Developer Tools": {
        "prefixes": ["Dev", "Code", "Git", "Stack", "Build", "Test", "Deploy", "Debug", "Script", "Ops"],
        "suffixes": ["Kit", "Flow", "Hub", "Pilot", "Forge", "Craft", "Scale", "Trace", "Lint", "Engine"],
        "problems": [
            "Engineering organizations waste 20% of sprint time waiting for brittle end-to-end integration test suites.",
            "Microservice architectures make diagnosing distributed latency bottlenecks like searching for a needle in a haystack.",
            "Frontend engineers spend hours manually converting Figma mockups into accessible, pixel-perfect Tailwind components.",
            "Database administrators struggle to detect and rewrite unindexed slow SQL queries before they bring down production.",
            "DevOps engineers struggle to write and validate complex Kubernetes YAML manifests and Helm charts safely.",
            "Mobile developers suffer 45-minute iOS and Android compilation build times on shared continuous integration runners."
        ],
        "solutions": [
            "an autonomous test generation engine that monitors production traffic and synthesizes self-healing E2E tests.",
            "an eBPF-powered distributed tracing agent providing microsecond telemetry without modifying application code.",
            "an intelligent design-to-code compiler transforming Figma tokens into semantic clean React and Vue components.",
            "an automated database performance optimization agent recommending index creation and query rewrites in PRs.",
            "a declarative cloud infrastructure co-pilot catching misconfigurations and validating Kubernetes security policies.",
            "a distributed remote build cache slashing iOS and Android compilation times by up to 75% across teams."
        ],
        "stacks": ["Rust, Go, React, ClickHouse, Docker, Kubernetes", "TypeScript, Next.js, Rust, PostgreSQL, WebAssembly", "Python, FastAPI, C++, LLVM, Redis, React"],
        "audiences": ["Senior Software Engineers", "Site Reliability Engineers", "Frontend Developers", "Database Administrators", "DevOps & Platform Leads"]
    }
}

def generate_startups(target_count=1200):
    records = []
    per_cat = target_count // len(CATEGORIES)
    
    for category in CATEGORIES:
        info = CATEGORY_TEMPLATES[category]
        for i in range(per_cat):
            prefix = random.choice(info["prefixes"])
            suffix = random.choice(info["suffixes"])
            modifier = random.choice(["", " Pro", " X", " Labs", " AI", " Cloud", " Sync", " Flow", " Engine"])
            name = f"{prefix}{suffix}{modifier}".strip()
            
            problem = random.choice(info["problems"])
            solution = random.choice(info["solutions"])
            stack = random.choice(info["stacks"])
            audience = random.choice(info["audiences"])
            
            description = (
                f"{name} is {solution} Designed specifically for {audience.lower()}, "
                f"it tackles the core challenge where {problem.lower()} "
                f"Powered by a modern architecture leveraging {stack}."
            )
            
            # Generate realistic, correlated scores
            # Base quality factor (latent startup quality 0.3 - 0.95)
            quality = np.random.beta(5, 3)  # centered around 0.62
            
            # Category-specific tendencies
            cat_inn_bias = {
                "AI": 12, "Cybersecurity": 8, "Developer Tools": 6,
                "HealthTech": 7, "FinTech": 5, "Agriculture": 4,
                "FoodTech": 2, "EdTech": 3, "SaaS": 1, "E-Commerce": -2
            }.get(category, 0)
            
            cat_mkt_bias = {
                "FinTech": 10, "SaaS": 9, "AI": 11,
                "E-Commerce": 7, "HealthTech": 8, "Cybersecurity": 8,
                "EdTech": 3, "FoodTech": 2, "Developer Tools": 5, "Agriculture": 4
            }.get(category, 0)
            
            cat_cpx_bias = {
                "HealthTech": 15, "Cybersecurity": 14, "AI": 13,
                "Developer Tools": 11, "FinTech": 10, "Agriculture": 8,
                "SaaS": 4, "FoodTech": 2, "EdTech": 1, "E-Commerce": 0
            }.get(category, 0)
            
            # Innovation score: 0 to 100
            inn_score = int(np.clip(quality * 75 + cat_inn_bias + np.random.normal(0, 8), 25, 99))
            
            # Market potential: 0 to 100
            mkt_score = int(np.clip(quality * 70 + cat_mkt_bias + np.random.normal(0, 9), 20, 98))
            
            # Complexity score: 0 to 100
            cpx_score = int(np.clip(45 + cat_cpx_bias + np.random.normal(0, 10), 20, 96))
            
            # Success probability: 0 to 100%
            # Higher market + innovation + reasonable complexity helps success
            succ_prob = int(np.clip(
                (mkt_score * 0.45) + (inn_score * 0.35) - (abs(cpx_score - 55) * 0.15) + np.random.normal(0, 6),
                15, 96
            ))
            
            # Investor readiness: 0 to 100
            # Weighted mix of innovation, market, execution balance
            inv_readiness = int(np.clip(
                (mkt_score * 0.35) + (inn_score * 0.30) + (succ_prob * 0.25) + ((100 - cpx_score * 0.3) * 0.10) + np.random.normal(0, 5),
                20, 98
            ))
            
            records.append({
                "startup_name": name,
                "description": description,
                "category": category,
                "problem_statement": problem,
                "target_audience": audience,
                "tech_stack": stack,
                "innovation_score": inn_score,
                "market_score": mkt_score,
                "complexity_score": cpx_score,
                "success_probability": succ_prob,
                "investor_readiness": inv_readiness
            })
            
    df = pd.DataFrame(records)
    # Shuffle dataset
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    return df

if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent
    out_file = out_dir / "startups.csv"
    print(f"Generating synthetic dataset with 1,200 startup records...")
    df = generate_startups(target_count=1200)
    df.to_csv(out_file, index=False)
    print(f"Successfully generated {len(df)} records to {out_file}")
    print("Class distribution:\n", df['category'].value_counts())
