import React from 'react';
import { motion } from 'framer-motion';
import Badge from './Badge';

export default function ScoreCard({
  title,
  score,
  maxScore = 100,
  badgeText,
  badgeColor = 'indigo',
  description,
  icon: Icon,
  delay = 0,
  suffix = ""
}) {
  const percentage = Math.min(Math.max((score / maxScore) * 100, 0), 100);

  const getBarColor = (val) => {
    if (val >= 75) return 'from-emerald-500 to-teal-400';
    if (val >= 50) return 'from-indigo-500 to-blue-400';
    if (val >= 35) return 'from-amber-500 to-orange-400';
    return 'from-rose-500 to-red-400';
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay }}
      className="glass-card p-5 rounded-2xl relative overflow-hidden"
    >
      <div className="flex items-start justify-between">
        <div className="flex items-center space-x-3">
          {Icon && (
            <div className="p-2.5 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
              <Icon className="w-5 h-5" />
            </div>
          )}
          <div>
            <h3 className="text-sm font-semibold text-slate-300">{title}</h3>
            {badgeText && (
              <Badge color={badgeColor} size="sm" className="mt-1">
                {badgeText}
              </Badge>
            )}
          </div>
        </div>

        <div className="text-right">
          <span className="text-3xl font-extrabold text-white tracking-tight">
            {typeof score === 'number' ? Math.round(score) : score}{suffix}
          </span>
          {maxScore === 100 && typeof score === 'number' && (
            <span className="text-xs text-slate-400 font-medium ml-1">/100</span>
          )}
        </div>
      </div>

      {/* Progress Bar */}
      {typeof score === 'number' && (
        <div className="mt-4">
          <div className="h-2 w-full bg-slate-800/80 rounded-full overflow-hidden p-0.5 border border-slate-700/40">
            <motion.div
              initial={{ width: 0 }}
              animate={{ width: `${percentage}%` }}
              transition={{ duration: 1.2, delay: delay + 0.2, ease: "easeOut" }}
              className={`h-full rounded-full bg-gradient-to-r ${getBarColor(percentage)}`}
            />
          </div>
        </div>
      )}

      {description && (
        <p className="mt-3 text-xs text-slate-400 leading-relaxed">
          {description}
        </p>
      )}
    </motion.div>
  );
}
