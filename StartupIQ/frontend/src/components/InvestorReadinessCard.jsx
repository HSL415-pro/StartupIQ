import React from 'react';
import { motion } from 'framer-motion';
import { Briefcase, DollarSign, Award, Target } from 'lucide-react';
import Badge from './Badge';

export default function InvestorReadinessCard({ data }) {
  if (!data) return null;

  const {
    score = 75,
    tier = "Seed / Angel Ready",
    target_round = "Seed Round",
    estimated_check_size = "$1.0M - $2.5M",
    pitch_advice = "Focus on acute customer pain and early organic retention.",
    badge_color = "emerald",
    factors = []
  } = data;

  return (
    <div className="glass-panel p-6 rounded-2xl border border-slate-800">
      {/* Top Banner */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-slate-800 gap-4">
        <div className="flex items-center space-x-3.5">
          <div className="p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400">
            <Briefcase className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center space-x-2.5">
              <h3 className="text-lg font-bold text-white">Investor Readiness Engine</h3>
              <Badge color={badge_color} size="md">
                {tier}
              </Badge>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">Venture Capital round fit, fundability index & syndicate assessment</p>
          </div>
        </div>

        {/* Big Score Display */}
        <div className="flex items-baseline space-x-1 sm:text-right">
          <span className="text-4xl font-extrabold text-white">{Math.round(score)}</span>
          <span className="text-sm font-semibold text-slate-400">/100</span>
        </div>
      </div>

      {/* Target Round and Check Size */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 my-5">
        <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center space-x-3">
          <div className="p-2 rounded-lg bg-indigo-500/10 text-indigo-400">
            <Target className="w-4 h-4" />
          </div>
          <div>
            <span className="text-xs text-slate-400">Target Financing Stage</span>
            <p className="text-sm font-bold text-slate-100">{target_round}</p>
          </div>
        </div>

        <div className="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center space-x-3">
          <div className="p-2 rounded-lg bg-emerald-500/10 text-emerald-400">
            <DollarSign className="w-4 h-4" />
          </div>
          <div>
            <span className="text-xs text-slate-400">Optimal Round Target</span>
            <p className="text-sm font-bold text-slate-100">{estimated_check_size}</p>
          </div>
        </div>
      </div>

      {/* 4 Core Factors Progress Bars */}
      <div className="space-y-3.5">
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
          Four-Pillar Institutional Evaluation Breakdown
        </h4>

        {factors.map((factor, idx) => {
          const val = typeof factor.score === 'number' ? factor.score : 70;
          return (
            <div key={idx} className="space-y-1.5">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-slate-200">
                  {factor.name} <span className="text-slate-500 font-normal">({factor.weight})</span>
                </span>
                <span className="font-bold text-slate-300">{Math.round(val)}%</span>
              </div>
              <div className="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${val}%` }}
                  transition={{ duration: 1, delay: idx * 0.1 }}
                  className="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full"
                />
              </div>
              {factor.description && (
                <p className="text-[11px] text-slate-400 leading-tight">
                  {factor.description}
                </p>
              )}
            </div>
          );
        })}
      </div>

      {/* Pitch Advice */}
      {pitch_advice && (
        <div className="mt-5 p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/20 text-xs text-indigo-300 flex items-start space-x-2.5">
          <Award className="w-4 h-4 text-indigo-400 flex-shrink-0 mt-0.5" />
          <div>
            <strong className="text-white">VC Narrative Recommendation: </strong>
            <span>{pitch_advice}</span>
          </div>
        </div>
      )}
    </div>
  );
}
