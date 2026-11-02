import React from 'react';
import { motion } from 'framer-motion';
import { Layers, Clock, Cpu, CheckCircle } from 'lucide-react';
import Badge from './Badge';

export default function ComplexityBreakdown({
  tier = "Moderate",
  score = 55,
  estimatedTimeline = "2 - 4 Months",
  factors = []
}) {
  const tierColor = tier === 'Complex' ? 'rose' : tier === 'Moderate' ? 'blue' : 'emerald';

  return (
    <div className="glass-panel p-6 rounded-2xl border border-slate-800">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-800 gap-3">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-purple-500/10 border border-purple-500/20 text-purple-400">
            <Layers className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <h3 className="text-base font-bold text-white">Technical Complexity Profile</h3>
              <Badge color={tierColor} size="md">
                {tier}
              </Badge>
            </div>
            <p className="text-xs text-slate-400">Architecture, infrastructure overhead & compliance burden</p>
          </div>
        </div>

        <div className="flex items-center space-x-2 text-xs text-slate-300 bg-slate-900/80 px-3 py-1.5 rounded-xl border border-slate-800">
          <Clock className="w-3.5 h-3.5 text-indigo-400" />
          <span>Timeline: <strong>{estimatedTimeline}</strong></span>
        </div>
      </div>

      {/* Contributing Factors List */}
      <div className="mt-5 space-y-3">
        <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
          Identified Contributing Engineering Factors ({factors.length})
        </h4>

        <div className="grid grid-cols-1 gap-3">
          {factors.map((item, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, x: -5 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.3, delay: idx * 0.08 }}
              className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800/80 flex items-start justify-between gap-3 hover:border-slate-700 transition-colors"
            >
              <div className="flex items-start space-x-2.5">
                <div className="mt-0.5 w-2 h-2 rounded-full bg-indigo-400 flex-shrink-0" />
                <div>
                  <h5 className="text-xs font-bold text-slate-200">{item.factor}</h5>
                  <p className="text-xs text-slate-400 mt-0.5 leading-relaxed">
                    {item.details}
                  </p>
                </div>
              </div>

              <Badge color={item.color || 'blue'} size="sm" className="flex-shrink-0">
                {item.impact} Impact
              </Badge>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}
