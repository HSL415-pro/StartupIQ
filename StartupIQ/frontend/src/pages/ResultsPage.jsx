import React, { useEffect, useState } from 'react';
import { useParams, useLocation, Link, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  Sparkles,
  Printer,
  Download,
  Share2,
  ArrowLeft,
  TrendingUp,
  Cpu,
  Layers,
  ShieldCheck,
  DollarSign,
  Compass,
  FileCheck,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';
import api from '../services/api';
import CircularGauge from '../components/CircularGauge';
import ScoreCard from '../components/ScoreCard';
import SwotMatrix from '../components/SwotMatrix';
import SimilarStartupsCard from '../components/SimilarStartupsCard';
import RecommendationsList from '../components/RecommendationsList';
import ComplexityBreakdown from '../components/ComplexityBreakdown';
import InvestorReadinessCard from '../components/InvestorReadinessCard';
import Badge from '../components/Badge';

export default function ResultsPage() {
  const { id } = useParams();
  const location = useLocation();
  const navigate = useNavigate();

  const [analysis, setAnalysis] = useState(location.state?.analysis || null);
  const [loading, setLoading] = useState(!analysis);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    if (analysis) return;

    // Check sessionStorage first
    const cached = sessionStorage.getItem(`startupiq_analysis_${id}`);
    if (cached) {
      try {
        setAnalysis(JSON.parse(cached));
        setLoading(false);
        return;
      } catch (e) {}
    }

    // Fetch from backend API
    if (id) {
      setLoading(true);
      api.getHistoryDetail(id)
        .then((res) => {
          if (res && res.data) {
            setAnalysis(res.data);
          } else {
            setError('Analysis report not found.');
          }
        })
        .catch((err) => {
          console.error(err);
          setError('Failed to load analysis report.');
        })
        .finally(() => setLoading(false));
    }
  }, [id, analysis]);

  const handlePrint = () => {
    window.print();
  };

  const handleExportJSON = () => {
    if (!analysis) return;
    const blob = new Blob([JSON.stringify(analysis, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${(analysis.startup_name || 'startup').toLowerCase()}-startupiq-analysis.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleShare = () => {
    navigator.clipboard.writeText(window.location.href);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-24 text-center">
        <div className="w-12 h-12 rounded-2xl bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 mx-auto flex items-center justify-center animate-spin mb-4">
          <Cpu className="w-6 h-6" />
        </div>
        <h3 className="text-xl font-bold text-white">Loading Venture Report...</h3>
        <p className="text-xs text-slate-400 mt-1">Retrieving scorecard from SQLite database</p>
      </div>
    );
  }

  if (error || !analysis) {
    return (
      <div className="max-w-md mx-auto px-4 py-24 text-center">
        <div className="p-4 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-sm mb-4">
          <AlertCircle className="w-6 h-6 mx-auto mb-2 text-rose-400" />
          <p>{error || 'Report not found.'}</p>
        </div>
        <Link
          to="/analyze"
          className="px-6 py-2.5 rounded-xl text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-500 transition-colors inline-block"
        >
          Run New Analysis
        </Link>
      </div>
    );
  }

  const {
    startup_name,
    category,
    category_confidence = 0.9,
    overall_score = 75,
    innovation_score = 70,
    market_score = 70,
    market_tier = "Medium",
    complexity_score = 50,
    complexity_tier = "Moderate",
    complexity_factors = [],
    success_probability = 70,
    investor_readiness_score = 70,
    investor_readiness_data = {},
    swot_analysis = {},
    recommendations = [],
    similar_startups = [],
    description,
    problem_statement,
    target_audience,
    technology_stack
  } = analysis;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Top Action Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 no-print">
        <Link
          to="/analyze"
          className="inline-flex items-center space-x-1.5 text-xs font-semibold text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Analyze Another Startup</span>
        </Link>

        <div className="flex items-center space-x-2">
          <button
            onClick={handleShare}
            className="px-3.5 py-2 rounded-xl text-xs font-semibold glass-panel hover:bg-slate-800 text-slate-300 transition-colors flex items-center space-x-1.5"
          >
            <Share2 className="w-3.5 h-3.5 text-indigo-400" />
            <span>{copied ? 'Link Copied!' : 'Share Link'}</span>
          </button>

          <button
            onClick={handleExportJSON}
            className="px-3.5 py-2 rounded-xl text-xs font-semibold glass-panel hover:bg-slate-800 text-slate-300 transition-colors flex items-center space-x-1.5"
          >
            <Download className="w-3.5 h-3.5 text-purple-400" />
            <span>Export JSON</span>
          </button>

          <button
            onClick={handlePrint}
            className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white transition-colors flex items-center space-x-1.5 shadow-md shadow-indigo-500/20"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>Print Report (PDF)</span>
          </button>
        </div>
      </div>

      {/* Main Title Banner */}
      <motion.div
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-panel p-6 sm:p-8 rounded-3xl border border-slate-800 relative overflow-hidden"
      >
        <div className="ambient-glow -top-16 -right-16 w-48 h-48 bg-indigo-600/20" />

        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">
                Institutional Venture Scorecard
              </span>
              <Badge color="indigo" size="sm">
                Category: {category} ({Math.round(category_confidence * 100)}% Conf.)
              </Badge>
              {market_tier && (
                <Badge color={market_tier === 'High' ? 'emerald' : 'blue'} size="sm">
                  {market_tier} Market TAM
                </Badge>
              )}
            </div>

            <h1 className="text-3xl sm:text-5xl font-black text-white tracking-tight">
              {startup_name}
            </h1>

            <p className="text-sm text-slate-300 max-w-3xl leading-relaxed">
              {description}
            </p>

            <div className="pt-2 flex flex-wrap gap-4 text-xs text-slate-400">
              {target_audience && (
                <span><strong>Audience:</strong> {target_audience}</span>
              )}
              {technology_stack && (
                <span><strong>Stack:</strong> {technology_stack}</span>
              )}
            </div>
          </div>

          {/* Big Overall Composite Score */}
          <div className="flex flex-col items-center justify-center p-5 rounded-2xl bg-slate-900/90 border border-indigo-500/30 text-center min-w-[150px] flex-shrink-0">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">
              Overall Score
            </span>
            <span className="text-4xl sm:text-5xl font-black text-white gradient-text my-1">
              {overall_score}
            </span>
            <span className="text-[11px] font-semibold text-emerald-400">
              {overall_score >= 75 ? 'Top Decile Venture' : overall_score >= 60 ? 'Venture Viable' : 'Early Ideation'}
            </span>
          </div>
        </div>
      </motion.div>

      {/* Primary KPI Grid (Circular Gauge + Score Cards) */}
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 items-stretch">
        {/* Module 2: Innovation Analyzer (Circular Gauge) */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
          className="glass-card p-6 rounded-3xl border border-indigo-500/30 flex flex-col items-center justify-center text-center relative"
        >
          <div className="absolute top-4 left-4">
            <Badge color="indigo" size="sm">Module 2</Badge>
          </div>
          <CircularGauge
            score={innovation_score}
            size={180}
            strokeWidth={13}
            label="Innovation Score"
            subtext="Architectural & IP Defensibility"
          />
        </motion.div>

        {/* Module 3: Market Potential Engine */}
        <ScoreCard
          title="Market Potential"
          score={market_score}
          badgeText={`${market_tier} Growth Sector`}
          badgeColor={market_tier === 'High' ? 'emerald' : market_tier === 'Medium' ? 'blue' : 'amber'}
          description={`Projected sector expansion with strong customer budget tailwinds in ${category}.`}
          icon={TrendingUp}
          delay={0.1}
        />

        {/* Module 5: Success Predictor */}
        <ScoreCard
          title="Success Probability"
          score={success_probability}
          suffix="%"
          badgeText={success_probability >= 70 ? 'High Scale Probability' : 'Moderate Viability'}
          badgeColor={success_probability >= 70 ? 'emerald' : 'blue'}
          description="Synthesized probability of achieving venture-scale product-market fit."
          icon={FileCheck}
          delay={0.2}
        />

        {/* Module 8: Investor Readiness Preview */}
        <ScoreCard
          title="Investor Readiness"
          score={investor_readiness_score}
          badgeText={investor_readiness_data?.tier || "Seed Ready"}
          badgeColor={investor_readiness_score >= 75 ? 'emerald' : 'purple'}
          description="Composite institutional fundability index across 4 core venture pillars."
          icon={DollarSign}
          delay={0.3}
        />
      </div>

      {/* Technical Complexity Section (Module 4) */}
      <ComplexityBreakdown
        tier={complexity_tier}
        score={complexity_score}
        estimatedTimeline={analysis.complexity_details?.estimated_timeline || "2 - 4 Months"}
        factors={complexity_factors}
      />

      {/* Investor Readiness Detailed Breakdown (Module 8) */}
      <InvestorReadinessCard data={investor_readiness_data} />

      {/* SWOT Matrix Section (Module 7) */}
      <div className="space-y-4">
        <div className="flex items-center space-x-2">
          <ShieldCheck className="w-5 h-5 text-indigo-400" />
          <h2 className="text-xl font-bold text-white tracking-tight">
            Venture SWOT Matrix (Module 7)
          </h2>
        </div>
        <SwotMatrix swot={swot_analysis} />
      </div>

      {/* Recommendations Engine (Module 9) */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Sparkles className="w-5 h-5 text-amber-400" />
            <h2 className="text-xl font-bold text-white tracking-tight">
              Actionable Improvement Recommendations (Module 9)
            </h2>
          </div>
          <span className="text-xs text-slate-400">
            {recommendations.length} Prioritized Strategic Action Items
          </span>
        </div>
        <RecommendationsList recommendations={recommendations} />
      </div>

      {/* Similar Startups Discovery (Module 6) */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Compass className="w-5 h-5 text-purple-400" />
            <h2 className="text-xl font-bold text-white tracking-tight">
              Top 5 Similar Startup Ideas (Module 6)
            </h2>
          </div>
          <span className="text-xs text-slate-400">
            TF-IDF Cosine Vector Space Matching on 1,200+ Corpus
          </span>
        </div>
        <SimilarStartupsCard similarStartups={similar_startups} />
      </div>
    </div>
  );
}
