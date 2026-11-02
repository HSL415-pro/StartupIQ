import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles, ArrowUpRight, Cpu } from 'lucide-react';
import Badge from './Badge';

export default function SimilarStartupsCard({ similarStartups = [] }) {
  if (!similarStartups || similarStartups.length === 0) {
    return (
      <div className="glass-panel rounded-2xl p-6 text-center text-slate-400">
        No similar startups indexed yet.
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {similarStartups.map((startup, idx) => {
        const similarity = startup.similarity_percentage || Math.round((startup.similarity_score || 0.5) * 100);
        const simColor = similarity >= 80 ? 'emerald' : similarity >= 65 ? 'blue' : 'amber';

        return (
          <motion.div
            key={idx}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.4, delay: idx * 0.08 }}
            className="glass-card p-5 rounded-2xl border border-slate-800/80 hover:border-indigo-500/40 transition-all duration-300 relative group"
          >
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-center space-x-3">
                <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500/20 to-purple-500/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 font-bold text-sm">
                  #{idx + 1}
                </div>
                <div>
                  <div className="flex items-center space-x-2">
                    <h4 className="text-base font-bold text-white group-hover:text-indigo-400 transition-colors">
                      {startup.startup_name}
                    </h4>
                    <Badge color="slate" size="sm">
                      {startup.category}
                    </Badge>
                  </div>
                  {startup.target_audience && (
                    <span className="text-xs text-slate-400">
                      Target: {startup.target_audience}
                    </span>
                  )}
                </div>
              </div>

              {/* Similarity Badge */}
              <div className="flex items-center space-x-2">
                <Badge color={simColor} size="md" className="font-semibold text-xs tracking-wide">
                  <Sparkles className="w-3.5 h-3.5 mr-1" />
                  {similarity}% Match
                </Badge>
              </div>
            </div>

            {/* Description & Problem */}
            <p className="mt-3 text-xs text-slate-300 leading-relaxed line-clamp-2">
              {startup.description}
            </p>

            {startup.tech_stack && (
              <div className="mt-3 pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs text-slate-400">
                <div className="flex items-center space-x-1.5 truncate">
                  <Cpu className="w-3.5 h-3.5 text-slate-500 flex-shrink-0" />
                  <span className="truncate">{startup.tech_stack}</span>
                </div>
                <div className="flex items-center space-x-3 flex-shrink-0 ml-2">
                  <span className="text-slate-400">
                    Readiness: <strong className="text-slate-200">{startup.investor_readiness || 70}/100</strong>
                  </span>
                </div>
              </div>
            )}
          </motion.div>
        );
      })}
    </div>
  );
}
