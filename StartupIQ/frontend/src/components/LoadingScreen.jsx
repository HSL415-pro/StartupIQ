import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Brain, Cpu, Search, CheckCircle2 } from 'lucide-react';

const STEPS = [
  "Tokenizing startup problem & technical architecture...",
  "Executing TF-IDF & Logistic Regression Category Classifier...",
  "Benchmarking innovation signals & architectural novelty...",
  "Computing Sector Addressable Market (TAM) & growth headwinds...",
  "Evaluating multi-tenant complexity & infrastructure overhead...",
  "Calculating multi-factor interaction Success Probability...",
  "Searching 1,200+ startup vectors with Cosine Similarity...",
  "Synthesizing 4-quadrant SWOT Matrix & Investor Readiness...",
  "Finalizing actionable strategic roadmap recommendations..."
];

export default function LoadingScreen({ startupName = "Your Startup Idea" }) {
  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStep((prev) => (prev < STEPS.length - 1 ? prev + 1 : prev));
    }, 450);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-surface-950/90 backdrop-blur-xl p-4">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="glass-panel max-w-lg w-full p-8 rounded-3xl border border-indigo-500/30 shadow-2xl shadow-indigo-500/10 text-center relative overflow-hidden"
      >
        {/* Ambient background glow */}
        <div className="ambient-glow -top-20 -left-20 w-48 h-48 bg-indigo-500/30" />
        <div className="ambient-glow -bottom-20 -right-20 w-48 h-48 bg-purple-500/30" />

        {/* Central Pulsing Radar Icon */}
        <div className="relative w-24 h-24 mx-auto mb-6 flex items-center justify-center">
          <motion.div
            animate={{ scale: [1, 1.4, 1], opacity: [0.3, 0.8, 0.3] }}
            transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
            className="absolute inset-0 rounded-full bg-indigo-500/20 border border-indigo-500/40"
          />
          <motion.div
            animate={{ scale: [1, 1.2, 1], opacity: [0.5, 1, 0.5] }}
            transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
            className="absolute inset-2 rounded-full bg-purple-500/30"
          />
          <div className="relative z-10 w-14 h-14 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-lg shadow-indigo-500/50">
            <Brain className="w-8 h-8 text-white animate-pulse" />
          </div>
        </div>

        <h3 className="text-xl font-extrabold text-white">
          Analyzing <span className="gradient-brand">{startupName}</span>
        </h3>
        <p className="text-xs text-slate-400 mt-1">
          StartupIQ Neural Engine running 9 multi-dimensional AI modules
        </p>

        {/* Dynamic Step Display */}
        <div className="mt-8 p-4 rounded-2xl bg-slate-900/80 border border-slate-800 text-left">
          <div className="flex items-center space-x-3">
            <Cpu className="w-5 h-5 text-indigo-400 animate-spin" />
            <span className="text-xs font-semibold text-slate-200">
              {STEPS[currentStep]}
            </span>
          </div>

          {/* Progress bar */}
          <div className="mt-4 h-1.5 w-full bg-slate-800 rounded-full overflow-hidden">
            <motion.div
              className="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"
              animate={{ width: `${((currentStep + 1) / STEPS.length) * 100}%` }}
              transition={{ duration: 0.3 }}
            />
          </div>
        </div>

        <div className="mt-6 flex items-center justify-center space-x-2 text-[11px] text-slate-500">
          <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
          <span>Generating institutional-grade venture scorecard</span>
        </div>
      </motion.div>
    </div>
  );
}
