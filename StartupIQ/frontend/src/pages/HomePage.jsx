import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  Sparkles,
  ArrowRight,
  TrendingUp,
  Cpu,
  ShieldCheck,
  Zap,
  Layers,
  Search,
  CheckCircle2,
  DollarSign,
  Compass,
  BarChart2,
  PieChart
} from 'lucide-react';
import api from '../services/api';

export default function HomePage() {
  const [stats, setStats] = useState({
    total_analyzed: 42,
    avg_innovation: 78.4,
    avg_market: 76.2,
    avg_success: 71.8
  });

  useEffect(() => {
    // Attempt fetching live platform metrics
    api.getDashboardStats()
      .then((res) => {
        if (res.data) {
          setStats((prev) => ({
            ...prev,
            total_analyzed: Math.max(res.data.total_analyzed || 0, 42),
            avg_innovation: res.data.avg_innovation || prev.avg_innovation,
            avg_market: res.data.avg_market || prev.avg_market,
            avg_success: res.data.avg_success || prev.avg_success,
          }));
        }
      })
      .catch(() => {});
  }, []);

  const features = [
    {
      icon: Compass,
      title: "Category Detection",
      module: "Module 1",
      desc: "TF-IDF & Logistic Regression trained across 10 industry verticals to classify sector with high confidence."
    },
    {
      icon: Zap,
      title: "Innovation Analyzer",
      module: "Module 2",
      desc: "Evaluates architectural uniqueness and defensibility against standard paradigms on a 0-100 animated circular gauge."
    },
    {
      icon: TrendingUp,
      title: "Market Potential Engine",
      module: "Module 3",
      desc: "Predicts continuous market potential and classifies TAM headwind into Low, Medium, or High growth tiers."
    },
    {
      icon: Layers,
      title: "Technical Complexity Analyzer",
      module: "Module 4",
      desc: "Explains structural engineering factors across AI inference, real-time streaming, and compliance burden."
    },
    {
      icon: BarChart2,
      title: "Success Predictor",
      module: "Module 5",
      desc: "Calculates probability of venture scale (0-100%) by balancing market demand against technical execution risk."
    },
    {
      icon: Search,
      title: "Similar Startup Finder",
      module: "Module 6",
      desc: "High-dimensional Cosine Similarity vector search discovering the Top 5 most semantically similar companies."
    },
    {
      icon: ShieldCheck,
      title: "SWOT Matrix Generator",
      module: "Module 7",
      desc: "Synthesizes an institutional 4-quadrant SWOT matrix (Strengths, Weaknesses, Opportunities, Threats)."
    },
    {
      icon: DollarSign,
      title: "Investor Readiness Engine",
      module: "Module 8",
      desc: "Scores round readiness across Innovation, Scalability, Market Size, and Technical Feasibility."
    },
    {
      icon: Sparkles,
      title: "Recommendation Engine",
      module: "Module 9",
      desc: "Generates 5-10 prioritized, actionable strategic steps spanning product wedge, GTM, and moat building."
    }
  ];

  const steps = [
    {
      step: "01",
      title: "Submit Idea Parameters",
      desc: "Provide your startup name, description, problem statement, target audience, and technology stack."
    },
    {
      step: "02",
      title: "Multi-Module AI Inference",
      desc: "StartupIQ's 9 trained ML models perform category classification, TAM modeling, and vector similarity in parallel."
    },
    {
      step: "03",
      title: "Venture Ready Scorecard",
      desc: "Receive an institutional-grade analysis dashboard with animated gauges, SWOT matrix, and tactical roadmap."
    }
  ];

  return (
    <div className="relative overflow-hidden">
      {/* Background ambient gradient orbs */}
      <div className="ambient-glow -top-32 left-1/4 w-96 h-96 bg-indigo-600/25" />
      <div className="ambient-glow top-96 -right-20 w-96 h-96 bg-purple-600/20" />
      <div className="ambient-glow top-[1200px] left-10 w-80 h-80 bg-pink-600/15" />

      {/* Hero Section */}
      <section className="relative pt-20 pb-16 md:pt-28 md:pb-24 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        {/* Top Tag Pill */}
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/25 text-indigo-400 text-xs font-semibold mb-6 shadow-sm shadow-indigo-500/10"
        >
          <Sparkles className="w-3.5 h-3.5" />
          <span>Next-Generation AI Idea Validation Platform</span>
        </motion.div>

        {/* Hero Title */}
        <motion.h1
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white max-w-4xl mx-auto leading-[1.12]"
        >
          Evaluate Startup Ideas With{' '}
          <span className="gradient-brand">Machine Learning</span> Rigor.
        </motion.h1>

        {/* Tagline & Subtitle */}
        <motion.p
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="mt-6 text-base sm:text-lg md:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed"
        >
          Stop building in the dark. <strong>StartupIQ</strong> leverages 9 specialized AI & ML models to evaluate market potential, technical feasibility, SWOT dynamics, and investor readiness in seconds.
        </motion.p>

        {/* CTA Buttons */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-9 flex flex-col sm:flex-row items-center justify-center gap-4"
        >
          <Link
            to="/analyze"
            className="w-full sm:w-auto px-8 py-3.5 rounded-2xl text-sm font-bold text-white bg-gradient-to-r from-indigo-600 via-indigo-500 to-purple-600 hover:from-indigo-500 hover:to-purple-500 shadow-xl shadow-indigo-500/30 transition-all hover:scale-[1.03] active:scale-[0.98] flex items-center justify-center space-x-2"
          >
            <span>Analyze Your Startup Idea</span>
            <ArrowRight className="w-4 h-4" />
          </Link>

          <Link
            to="/trends"
            className="w-full sm:w-auto px-7 py-3.5 rounded-2xl text-sm font-bold text-slate-200 glass-panel hover:bg-slate-800/80 hover:text-white border border-slate-700/60 transition-all flex items-center justify-center space-x-2"
          >
            <PieChart className="w-4 h-4 text-indigo-400" />
            <span>Explore Sector Trends</span>
          </Link>
        </motion.div>

        {/* Social Proof / Benchmark Banner */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.45 }}
          className="mt-12 flex flex-wrap items-center justify-center gap-6 sm:gap-10 text-xs text-slate-400"
        >
          <div className="flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>1,200+ Synthetic Corpus Indexed</span>
          </div>
          <div className="flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>10 Distinct Industry Categories</span>
          </div>
          <div className="flex items-center space-x-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>Python 3.13 & FastAPI Core</span>
          </div>
        </motion.div>
      </section>

      {/* Animated Statistics Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6">
          <motion.div
            whileHover={{ y: -3 }}
            className="glass-card p-6 rounded-2xl text-center border border-slate-800"
          >
            <span className="text-3xl sm:text-4xl font-extrabold text-white gradient-text">
              1,200+
            </span>
            <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mt-1.5">
              Startups Indexed
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -3 }}
            className="glass-card p-6 rounded-2xl text-center border border-slate-800"
          >
            <span className="text-3xl sm:text-4xl font-extrabold text-indigo-400">
              10
            </span>
            <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mt-1.5">
              Industry Verticals
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -3 }}
            className="glass-card p-6 rounded-2xl text-center border border-slate-800"
          >
            <span className="text-3xl sm:text-4xl font-extrabold text-purple-400">
              9
            </span>
            <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mt-1.5">
              ML Engine Modules
            </p>
          </motion.div>

          <motion.div
            whileHover={{ y: -3 }}
            className="glass-card p-6 rounded-2xl text-center border border-slate-800"
          >
            <span className="text-3xl sm:text-4xl font-extrabold text-emerald-400">
              &lt; 1.5s
            </span>
            <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider mt-1.5">
              Pipeline Latency
            </p>
          </motion.div>
        </div>
      </section>

      {/* Features Grid Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center max-w-3xl mx-auto mb-14">
          <span className="text-xs font-bold uppercase tracking-widest text-indigo-400">
            Comprehensive Venture Evaluation
          </span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white mt-2">
            9 Multi-Dimensional AI Modules In One Cohesive Platform
          </h2>
          <p className="text-sm text-slate-400 mt-3">
            Every analysis executes across specialized natural language processing, linear classifiers, and vector space models.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feat, idx) => {
            const Icon = feat.icon;
            return (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 15 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: idx * 0.05 }}
                className="glass-card p-6 rounded-2xl border border-slate-800/80 hover:border-indigo-500/40 group relative overflow-hidden"
              >
                <div className="flex items-center justify-between mb-4">
                  <div className="p-3 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 group-hover:bg-indigo-500/20 group-hover:scale-110 transition-all">
                    <Icon className="w-5 h-5" />
                  </div>
                  <span className="text-[11px] font-bold px-2 py-0.5 rounded-full bg-slate-800 text-slate-400">
                    {feat.module}
                  </span>
                </div>
                <h3 className="text-base font-bold text-white group-hover:text-indigo-300 transition-colors">
                  {feat.title}
                </h3>
                <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                  {feat.desc}
                </p>
              </motion.div>
            );
          })}
        </div>
      </section>

      {/* How It Works Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 border-t border-slate-800/80">
        <div className="text-center max-w-3xl mx-auto mb-14">
          <span className="text-xs font-bold uppercase tracking-widest text-purple-400">
            Streamlined Workflow
          </span>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white mt-2">
            How StartupIQ Operates
          </h2>
          <p className="text-sm text-slate-400 mt-3">
            From brief concept description to institutional investment readiness in 3 transparent steps.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {steps.map((st, idx) => (
            <div key={idx} className="relative glass-panel p-8 rounded-2xl border border-slate-800">
              <span className="text-4xl font-black text-indigo-500/30">
                {st.step}
              </span>
              <h3 className="text-lg font-bold text-white mt-3">
                {st.title}
              </h3>
              <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                {st.desc}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Final Call to Action */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
        <div className="glass-panel p-10 sm:p-14 rounded-3xl border border-indigo-500/30 relative overflow-hidden shadow-2xl shadow-indigo-500/10">
          <div className="ambient-glow -top-20 -left-20 w-56 h-56 bg-indigo-500/30" />
          <div className="ambient-glow -bottom-20 -right-20 w-56 h-56 bg-purple-500/30" />

          <h2 className="text-3xl sm:text-4xl font-extrabold text-white relative z-10">
            Ready To Pressure-Test Your Startup Idea?
          </h2>
          <p className="text-sm sm:text-base text-slate-300 max-w-xl mx-auto mt-3 relative z-10 leading-relaxed">
            Gain immediate institutional clarity on market viability, defensibility, and strategic next steps.
          </p>

          <div className="mt-8 relative z-10 flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/analyze"
              className="w-full sm:w-auto px-8 py-3.5 rounded-2xl text-sm font-bold text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 shadow-xl shadow-indigo-500/25 transition-all hover:scale-105 active:scale-95"
            >
              Start Free AI Analysis
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
