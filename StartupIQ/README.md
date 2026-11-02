# StartupIQ 🚀
### AI-Powered Startup Idea Analyzer

[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React 18](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **StartupIQ** is an institutional-grade AI/ML SaaS web application that evaluates early-stage startup ideas using specialized machine learning models and vector space analysis.

---

## 🎯 Executive Summary & Objectives

StartupIQ bridges the gap between subjective founder intuition and data-driven venture analysis. A user provides:
- **Startup Name**
- **Startup Description**
- **Problem Statement**
- **Industry**
- **Target Audience**
- **Technology Stack**

The platform executes 9 specialized AI/ML modules in parallel to generate:
1. **Startup Category Detection** (TF-IDF + Logistic Regression across 10 verticals with confidence score)
2. **Innovation Score** (0–100 score displayed on an animated circular gauge)
3. **Market Potential Score** (0–100 TAM projection categorized into Low, Medium, High)
4. **Technical Complexity Analysis** (Simple, Moderate, Complex with contributing architectural factors)
5. **Success Probability** (0–100% venture viability prediction)
6. **Similar Startup Discovery** (Cosine Similarity on 1,200+ startup vectors returning Top 5 peers)
7. **SWOT Analysis** (Context-aware 4-quadrant strategic matrix)
8. **Investor Readiness Score** (Composite 0–100 score across 4 institutional pillars)
9. **Startup Improvement Recommendations** (5–10 prioritized actionable initiatives)

---

## 🏗️ Repository Architecture

```
StartupIQ/
├── assets/
│   └── logo.svg                      # Vector branding assets
├── backend/
│   ├── services/
│   │   ├── ai_pipeline.py            # Unified 9-module orchestrator
│   │   ├── category_service.py       # Module 1: TF-IDF + Logistic Regression
│   │   ├── innovation_service.py     # Module 2: Novelty & Defensibility
│   │   ├── market_service.py         # Module 3: Market Potential Engine
│   │   ├── complexity_service.py     # Module 4: Technical Complexity Analyzer
│   │   ├── success_service.py        # Module 5: Success Predictor Regressor
│   │   ├── similarity_service.py     # Module 6: Vector Cosine Similar Startups
│   │   ├── swot_service.py           # Module 7: Dynamic SWOT Matrix Generator
│   │   ├── investor_service.py       # Module 8: Four-Pillar Investor Readiness
│   │   └── recommendation_service.py # Module 9: Strategic Actionable Engine
│   ├── config.py                     # App settings, CORS, and environment
│   ├── main.py                       # FastAPI application & REST endpoints
│   └── schemas.py                    # Pydantic request/response schemas
├── database/
│   ├── connection.py                 # SQLite thread-safe connection manager
│   ├── db_manager.py                 # CRUD and analytical metric aggregations
│   ├── init_db.py                    # Database schema creator & seed script
│   └── startupiq.db                  # Local SQLite database file (auto-generated)
├── datasets/
│   ├── startups.csv                  # 1,200 synthetic startup records across 10 categories
│   └── generate_dataset.py           # Synthetic dataset generator script
├── models/
│   ├── category_model.joblib         # Trained Logistic Regression classifier
│   ├── category_vectorizer.joblib    # Fitted TF-IDF category vectorizer
│   ├── market_model.joblib           # Trained Ridge market regressor
│   ├── market_vectorizer.joblib      # Fitted TF-IDF market vectorizer
│   ├── success_model.joblib          # Multi-factor success regressor
│   ├── similarity_matrix.joblib      # Precomputed TF-IDF corpus vector matrix
│   ├── similarity_vectorizer.joblib  # Fitted similarity TF-IDF vectorizer
│   ├── startups_corpus.joblib        # Indexed startup metadata records
│   └── metadata.json                 # Serialized model metrics & evaluation report
├── training/
│   ├── train_category.py             # Trains category detection model
│   ├── train_market.py               # Trains market potential model
│   ├── train_success.py              # Trains success probability regressor
│   ├── train_similarity.py           # Builds similarity corpus index
│   └── save_models.py                # Master training script executing all steps
├── utils/
│   ├── constants.py                  # Industry categories, TAM benchmarks, signals
│   ├── scoring.py                    # Tier classifications & investor formulas
│   └── text_cleaner.py               # Text normalization and feature composers
├── frontend/
│   ├── public/
│   │   └── logo.svg                  # Brand favicon & SVGs
│   ├── src/
│   │   ├── components/
│   │   │   ├── Badge.jsx             # Color-coded tier badges
│   │   │   ├── CircularGauge.jsx     # Animated SVG circular innovation gauge
│   │   │   ├── ComplexityBreakdown.jsx# Engineering timeline & factor breakdown
│   │   │   ├── Footer.jsx            # SaaS dark mode footer
│   │   │   ├── InvestorReadinessCard.jsx# VC round fit & 4-factor progress bars
│   │   │   ├── LoadingScreen.jsx     # Step-by-step radar progress simulator
│   │   │   ├── Navbar.jsx            # Responsive navigation & active model pill
│   │   │   ├── RecommendationsList.jsx# Filterable strategic roadmap list
│   │   │   ├── ScoreCard.jsx         # Metric card with gradient progress bars
│   │   │   ├── SimilarStartupsCard.jsx# Top 5 similar startups with % match
│   │   │   └── SwotMatrix.jsx        # 4-quadrant interactive SWOT matrix
│   │   ├── pages/
│   │   │   ├── AboutPage.jsx         # Architecture deep-dive & methodology
│   │   │   ├── AnalyzePage.jsx       # Submission form with 1-click sample presets
│   │   │   ├── HistoryPage.jsx       # Historical records, search, filter & sort
│   │   │   ├── HomePage.jsx          # Hero, stats, feature grid & workflows
│   │   │   ├── ResultsPage.jsx       # Comprehensive report with PDF/JSON export
│   │   │   └── TrendsPage.jsx        # Recharts Bar, Radar, Pie & Line charts
│   │   ├── services/
│   │   │   └── api.js                # Axios client with fallback routing
│   │   ├── utils/
│   │   │   └── sampleIdeas.js        # One-click test startup presets
│   │   ├── App.jsx                   # React Router routing configuration
│   │   ├── index.css                 # Glassmorphism, animations & Tailwind styles
│   │   └── main.jsx                  # React 18 DOM entry point
│   ├── index.html                    # HTML5 shell with fonts and metadata
│   ├── package.json                  # Frontend dependencies & scripts
│   ├── postcss.config.js             # PostCSS plugins
│   ├── tailwind.config.js            # Tailwind CSS configuration
│   └── vite.config.js                # Vite dev server & proxy settings
├── Dockerfile                        # Multi-stage production container build
├── docker-compose.yml                # Single command container orchestrator
├── render.yaml                       # Render.com backend blueprint
├── vercel.json                       # Vercel.com frontend deployment config
├── package.json                      # Root workspace scripts
├── tailwind.config.js                # Root Tailwind config
├── vite.config.js                    # Root Vite config
├── requirements.txt                  # Python 3.13 verified dependencies
├── .env.example                      # Sample environment variables
└── README.md                         # Complete project documentation
```

---

## ⚡ Tech Stack Specifications

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, Vite, Tailwind CSS, React Router v6, Axios, Recharts, Framer Motion, Lucide Icons |
| **Backend** | Python 3.13, FastAPI, Uvicorn, Pydantic v2 |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy, Joblib, SciPy |
| **Database** | SQLite (WAL mode, thread-safe connections, foreign key constraints) |
| **Containerization** | Docker (Multi-stage build), Docker Compose |
| **Deployment** | Vercel (Frontend SPA) + Render (Backend FastAPI Service) |

---

## 🧠 The 9 AI & ML Modules

### Module 1: Category Detection
- **Algorithm**: Sublinear TF-IDF Vectorizer + Multinomial Logistic Regression ($C=2.0$).
- **Categories (10)**: AI, SaaS, FoodTech, HealthTech, FinTech, EdTech, Agriculture, Cybersecurity, E-Commerce, Developer Tools.
- **Output**: Predicted Category and normalized Confidence Probability.

### Module 2: Innovation Analyzer
- **Algorithm**: High-dimensional semantic token novelty detection and frontier technology keyword scoring.
- **Output**: 0–100 Innovation Score rendered on an animated circular SVG gauge.

### Module 3: Market Potential Engine
- **Algorithm**: TF-IDF feature extraction + Ridge Regularized Regressor ($ \alpha=5.0 $) combined with sector Total Addressable Market (TAM) expansion factors.
- **Output**: Continuous Market Potential Score (0–100) and classification into `Low`, `Medium`, or `High` tiers.

### Module 4: Technical Complexity Analyzer
- **Algorithm**: Structural architecture parser analyzing deep inference, real-time telemetry, regulatory compliance (HIPAA, FHIR, PCI-DSS, SOC 2), and microservice topology.
- **Output**: `Simple`, `Moderate`, or `Complex` classification, sprint delivery timeline, and contributing factor breakdown.

### Module 5: Success Predictor
- **Algorithm**: Interaction Ridge Regressor trained on non-linear interaction terms between Market TAM, Defensibility, and Complexity risk penalties.
- **Output**: Success Probability (0–100%) and percentile ranking.

### Module 6: Similar Startup Finder
- **Algorithm**: TF-IDF Vector Space Model + Pairwise Cosine Similarity computed against 1,200 indexed startup vectors.
- **Output**: Top 5 most semantically and architecturally similar startups with exact Match Percentages.

### Module 7: SWOT Generator
- **Algorithm**: Dynamic context-aware synthesis evaluating domain friction, team scope, and competitive wedges.
- **Output**: Institutional 4-quadrant SWOT matrix (Strengths, Weaknesses, Opportunities, Threats).

### Module 8: Investor Readiness Engine
- **Algorithm**: Four-Pillar Venture Index:
  $$\text{Investor Score} = 0.25 \times \text{Innovation} + 0.30 \times \text{Scalability} + 0.25 \times \text{Market} + 0.20 \times \text{Feasibility}$$
- **Output**: Fundability Score (0–100), Target Round (Pre-Seed to Series A), estimated check size, and VC narrative guidance.

### Module 9: Recommendation Engine
- **Algorithm**: Prioritized strategic heuristics addressing specific structural vulnerabilities identified in Modules 1–8.
- **Output**: 5–10 actionable recommendations categorized by GTM, Product, Engineering, Compliance, and Defensibility with estimated timelines.

---

## 🚀 Quickstart Guide (Local Execution)

### Prerequisites
- **Python 3.13** installed
- **Node.js (v18+)** and **npm** installed

---

### Step 1: Clone or Extract Repository
```bash
cd StartupIQ
```

---

### Step 2: Backend Setup & Execution
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Initialize database schemas:
   ```bash
   python database/init_db.py
   ```
3. (Optional) Re-train all machine learning models:
   ```bash
   python training/save_models.py
   ```
   *(Pre-trained models are already included inside `models/` ready to run out of the box!)*

4. Launch the FastAPI backend server:
   ```bash
   python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
   Backend will be live at: **http://127.0.0.1:8000**  
   Interactive Swagger API Documentation: **http://127.0.0.1:8000/docs**

---

### Step 3: Frontend Setup & Execution
1. Open a new terminal window and navigate to `frontend/`:
   ```bash
   cd frontend
   npm install
   ```
2. Start the Vite development server:
   ```bash
   npm run dev
   ```
   Frontend will be live at: **http://localhost:5173**

---

## 🐳 Docker Deployment

Run the complete fullstack application using Docker:

```bash
# Build and run containers
docker-compose up --build -d

# Inspect running application
docker-compose ps
```
The application will be accessible at: **http://localhost:8000**

---

## 🌐 Cloud Deployment Guide

### Frontend Deployment on Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run from the project root:
   ```bash
   vercel --prod
   ```
3. Set Environment Variable in Vercel Dashboard:
   - `VITE_API_URL`: Your deployed backend URL (e.g., `https://startupiq-backend.onrender.com`)

### Backend Deployment on Render
1. Connect your GitHub repository to [Render](https://render.com).
2. Create a new **Web Service** selecting `render.yaml` or manual configuration:
   - **Environment**: Python 3.13
   - **Build Command**: `pip install -r requirements.txt && python database/init_db.py`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - `PYTHON_VERSION`: `3.13.1`
     - `HOST`: `0.0.0.0`
     - `DEBUG`: `false`

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/analyze` | Comprehensive pipeline executing all 9 modules and saving to DB |
| `POST` | `/predict-category` | Module 1: Category Detection & Confidence |
| `POST` | `/predict-market` | Module 3: Market Potential & TAM Tier |
| `POST` | `/predict-complexity` | Module 4: Technical Complexity & Factors |
| `POST` | `/predict-success` | Module 5: Success Probability |
| `POST` | `/similar-startups` | Module 6: Vector Cosine Similar Startups (Top 5) |
| `POST` | `/generate-swot` | Module 7: Dynamic 4-Quadrant SWOT Matrix |
| `POST` | `/investor-readiness` | Module 8: Four-Pillar Investor Readiness Score |
| `POST` | `/recommendations` | Module 9: 5–10 Actionable Improvement Steps |
| `GET` | `/dashboard-stats` | Platform aggregates and average scores |
| `GET` | `/trends` | Cross-category benchmarks for charts |
| `GET` | `/history` | Search, filter, and paginate analysis records |
| `GET` | `/history/{id}` | Full analysis details by ID |
| `DELETE` | `/history/{id}` | Delete history record |
| `GET` | `/health` | Health check endpoint |

---

## 🧪 Verification & Testing Checklist

- [x] Python 3.13 compatibility verified
- [x] All 9 AI modules functioning end-to-end
- [x] Pre-trained models stored in `models/`
- [x] 1,200 synthetic startup dataset generated in `datasets/startups.csv`
- [x] SQLite database tables (`users`, `startup_ideas`, `analysis_results`, `analysis_history`) active
- [x] Frontend React 18 SPA with dark mode, glassmorphism, Recharts, and Framer Motion
- [x] Complete `StartupIQ.zip` distributable archive created
