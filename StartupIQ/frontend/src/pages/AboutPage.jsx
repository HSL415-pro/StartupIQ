import React from 'react';
import { motion } from 'framer-motion';
import {
  Brain,
  Cpu,
  Layers,
  Database,
  ShieldCheck,
  Sparkles,
  Rocket,
  Code,
  FileText,
  TrendingUp,
  CheckCircle2
} from 'lucide-react';
import Badge from '../components/Badge';

export default function AboutPage() {
  const models = [
    {
      num: "01",
      title: "Category Detection",
      tech: "TF-IDF + Multinomial Logistic Regression",
      desc: "Converts startup problem and tech stack tokens into sublinear TF-IDF vectors, trained across 10 distinct industry verticals with stratified cross-validation."
    },
    {
      num: "02",
      title: "Innovation Analyzer",
      tech: "Novelty & Frontier Tech Heuristic Engine",
      desc: "Measures distance from standard CRUD archetypes, penalizing commodity portal patterns while rewarding agentic, deep learning, or low-latency primitives."
    },
    {
      num: "03",
      title: "Market Potential Engine",
      tech: "Ridge Regularized Regressor + TAM Coefficients",
      desc: "Combines domain addressable market (TAM) multipliers with customer willingness-to-pay signals to classify venture potential into Low, Medium, and High tiers."
    },
    {
      num: "04",
      title: "Technical Complexity Analyzer",
      tech: "Architectural & Compliance Factor Parser",
      desc: "Detects GPU orchestration, event streaming, biometric/healthcare compliance (HIPAA/FHIR), and eBPF kernel tracing to output realistic sprint timelines."
    },
    {
      num: "05",
      title: "Success Predictor",
      tech: "Interaction Ridge Regressor",
      desc: "Models non-linear risk interactions between market demand, innovation defensibility, and execution complexity penalty curves."
    },
    {
      num: "06",
      title: "Similar Startup Finder",
      tech: "Vector Space Cosine Similarity on 1,200+ Corpus",
      desc: "Vectorizes problem, audience, and solution parameters across 1,200 indexed startup vectors to retrieve the Top 5 closest semantic peers."
    },
    {
      num: "07",
      title: "SWOT Matrix Generator",
      tech: "Context-Aware Dynamic Synthesis",
      desc: "Generates an institutional 4-quadrant SWOT matrix (Strengths, Weaknesses, Opportunities, Threats) tailored to the exact audience and tech stack."
    },
    {
      num: "08",
      title: "Investor Readiness Engine",
      tech: "Four-Pillar Institutional Scorecard",
      desc: "Evaluates fundability across Innovation (25%), Scalability (30%), Market Size (25%), and Feasibility (20%) to determine optimal check size and stage."
    },
    {
      num: "09",
      title: "Recommendation Engine",
      tech: "Strategic Action Item Generator",
      desc: "Synthesizes 5-10 prioritized tactical initiatives spanning initial customer wedge, feedback flywheels, and pricing value metrics."
    }
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-14">
      {/* Page Header */}
      <div className="text-center max-w-3xl mx-auto">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold mb-3">
          <Brain className="w-3.5 h-3.5" />
          <span>Scientific Venture Intelligence</span>
        </div>
        <h1 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight">
          About Startup<span className="text-indigo-400">IQ</span>
        </h1>
        <p className="text-sm sm:text-base text-slate-300 mt-3 leading-relaxed">
          StartupIQ transforms startup idea evaluation from subjective intuition into systematic, multi-dimensional Machine Learning analysis.
        </p>
      </div>

      {/* Mission Section */}
      <motion.div
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-panel p-8 sm:p-10 rounded-3xl border border-slate-800 space-y-4"
      >
        <h2 className="text-xl font-bold text-white flex items-center space-x-2">
          <Rocket className="w-5 h-5 text-indigo-400" />
          <span>The StartupIQ Philosophy</span>
        </h2>
        <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
          Over 90% of early-stage startups fail not because they cannot build software, but because they build something with negligible market demand, zero technological moat, or insurmountable regulatory overhead.
        </p>
        <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
          StartupIQ was built to give founders, venture capitalists, and startup accelerators a fast, repeatable, institutional-grade evaluation framework that pressure-tests venture viability in seconds.
        </p>
      </motion.div>

      {/* AI Architecture Deep Dive */}
      <div className="space-y-6">
        <div className="text-center max-w-xl mx-auto">
          <span className="text-xs font-bold uppercase tracking-widest text-indigo-400">
            Machine Learning Pipeline
          </span>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white mt-1">
            The 9 Specialized AI Modules
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Trained and serialized with Scikit-Learn and Joblib for instant inferencing.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {models.map((m, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 15 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.35, delay: idx * 0.05 }}
              className="glass-card p-6 rounded-2xl border border-slate-800 space-y-2.5"
            >
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono font-bold text-indigo-400">
                  MODULE {m.num}
                </span>
                <Badge color="slate" size="sm">
                  Scikit-Learn
                </Badge>
              </div>
              <h3 className="text-base font-bold text-white">
                {m.title}
              </h3>
              <span className="inline-block text-[11px] font-semibold text-slate-400 bg-slate-900 px-2 py-0.5 rounded-md border border-slate-800">
                {m.tech}
              </span>
              <p className="text-xs text-slate-400 leading-relaxed pt-1">
                {m.desc}
              </p>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Tech Stack Specs */}
      <div className="glass-panel p-8 rounded-3xl border border-slate-800 space-y-6">
        <h2 className="text-xl font-bold text-white flex items-center space-x-2">
          <Cpu className="w-5 h-5 text-purple-400" />
          <span>Production Technical Specifications</span>
        </h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 text-xs">
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <span className="text-indigo-400 font-bold block mb-1">Backend Runtime</span>
            <p className="font-semibold text-slate-200">Python 3.13</p>
            <p className="text-slate-500 mt-0.5">FastAPI, Uvicorn, Pydantic</p>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <span className="text-purple-400 font-bold block mb-1">Machine Learning</span>
            <p className="font-semibold text-slate-200">Scikit-Learn 1.8+</p>
            <p className="text-slate-500 mt-0.5">TF-IDF, Logistic, Ridge, Joblib</p>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <span className="text-blue-400 font-bold block mb-1">Database Engine</span>
            <p className="font-semibold text-slate-200">SQLite (WAL Mode)</p>
            <p className="text-slate-500 mt-0.5">Thread-safe row factories & JSON</p>
          </div>

          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800">
            <span className="text-pink-400 font-bold block mb-1">Frontend UI</span>
            <p className="font-semibold text-slate-200">React 18 + Vite</p>
            <p className="text-slate-500 mt-0.5">Tailwind CSS, Framer Motion, Recharts</p>
          </div>
        </div>
      </div>
    </div>
  );
}
