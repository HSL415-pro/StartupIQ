import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Lightbulb, CheckCircle2, Clock, Zap, ArrowRight, Filter } from 'lucide-react';
import Badge from './Badge';

export default function RecommendationsList({ recommendations = [] }) {
  const [filter, setFilter] = useState('All');

  if (!recommendations || recommendations.length === 0) return null;

  const categories = ['All', ...new Set(recommendations.map(r => r.category || 'General'))];

  const filtered = filter === 'All'
    ? recommendations
    : recommendations.filter(r => (r.category || 'General') === filter);

  const getPriorityColor = (p) => {
    if (p === 'High') return 'rose';
    if (p === 'Quick Win') return 'emerald';
    return 'blue';
  };

  return (
    <div className="space-y-4">
      {/* Category filter pills */}
      <div className="flex items-center space-x-2 overflow-x-auto pb-1 scrollbar-none">
        <Filter className="w-3.5 h-3.5 text-slate-500 mr-1 flex-shrink-0" />
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setFilter(cat)}
            className={`px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap transition-all ${
              filter === cat
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-500/20'
                : 'bg-slate-800/80 text-slate-400 hover:text-slate-200 hover:bg-slate-700/80'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 gap-3.5">
        {filtered.map((rec, idx) => (
          <motion.div
            key={rec.id || idx}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.35, delay: idx * 0.05 }}
            className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800/80 hover:border-indigo-500/30 transition-all group"
          >
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-start space-x-3">
                <div className="mt-0.5 p-2 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex-shrink-0">
                  <Lightbulb className="w-4 h-4" />
                </div>
                <div>
                  <h4 className="text-sm font-bold text-slate-100 group-hover:text-indigo-400 transition-colors">
                    {rec.title}
                  </h4>
                  <div className="flex items-center space-x-2 mt-1">
                    <Badge color={getPriorityColor(rec.priority)} size="sm">
                      {rec.priority || 'Medium'}
                    </Badge>
                    {rec.category && (
                      <span className="text-xs text-slate-400">
                        {rec.category}
                      </span>
                    )}
                    {rec.timeframe && (
                      <span className="flex items-center text-xs text-slate-500">
                        <Clock className="w-3 h-3 mr-1" />
                        {rec.timeframe}
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>

            <p className="mt-3 text-xs text-slate-300 leading-relaxed pl-11">
              {rec.description}
            </p>

            {rec.impact && (
              <div className="mt-2.5 ml-11 flex items-center text-xs text-emerald-400 font-medium">
                <Zap className="w-3.5 h-3.5 mr-1 text-emerald-400" />
                Estimated Impact: <span className="text-slate-200 ml-1">{rec.impact}</span>
              </div>
            )}
          </motion.div>
        ))}
      </div>
    </div>
  );
}
