import React from 'react';
import { motion } from 'framer-motion';

export default function CircularGauge({
  score = 0,
  size = 200,
  strokeWidth = 14,
  label = "Innovation Score",
  subtext = "Novelty & Defensibility",
  color = "indigo"
}) {
  const radius = (size - strokeWidth * 2) / 2;
  const circumference = radius * 2 * Math.PI;
  const progress = Math.min(Math.max(score, 0), 100);
  const strokeDashoffset = circumference - (progress / 100) * circumference;

  // Determine gradient color scheme based on score
  const getGradientColors = (s) => {
    if (s >= 80) return { start: '#10b981', mid: '#06b6d4', end: '#6366f1' };
    if (s >= 60) return { start: '#6366f1', mid: '#8b5cf6', end: '#ec4899' };
    if (s >= 40) return { start: '#f59e0b', mid: '#ea580c', end: '#ec4899' };
    return { start: '#f43f5e', mid: '#fb7185', end: '#f59e0b' };
  };

  const colors = getGradientColors(score);
  const gradientId = `gaugeGrad-${label.replace(/\s+/g, '')}`;

  return (
    <div className="flex flex-col items-center justify-center relative select-none">
      <div className="relative" style={{ width: size, height: size }}>
        <svg width={size} height={size} className="transform -rotate-90">
          <defs>
            <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor={colors.start} />
              <stop offset="50%" stopColor={colors.mid} />
              <stop offset="100%" stopColor={colors.end} />
            </linearGradient>
            <filter id={`glow-${gradientId}`} x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="4" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Background Track */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="rgba(255, 255, 255, 0.08)"
            strokeWidth={strokeWidth}
            fill="transparent"
          />

          {/* Animated Foreground Progress Circle */}
          <motion.circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke={`url(#${gradientId})`}
            strokeWidth={strokeWidth}
            strokeLinecap="round"
            fill="transparent"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset }}
            transition={{ duration: 1.5, ease: "easeOut" }}
            filter={`url(#glow-${gradientId})`}
          />
        </svg>

        {/* Center Score Display */}
        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="flex items-baseline font-black tracking-tight"
          >
            <span className="text-4xl md:text-5xl font-extrabold text-white">
              {Math.round(score)}
            </span>
            <span className="text-sm font-semibold text-slate-400 ml-0.5">/100</span>
          </motion.div>
          <span className="text-xs font-medium text-slate-400 mt-1 uppercase tracking-wider">
            {score >= 80 ? 'Frontier Moat' : score >= 60 ? 'Competitive' : 'Iterative'}
          </span>
        </div>
      </div>

      {label && (
        <div className="text-center mt-3">
          <h4 className="text-sm font-semibold text-slate-200">{label}</h4>
          {subtext && <p className="text-xs text-slate-400 mt-0.5">{subtext}</p>}
        </div>
      )}
    </div>
  );
}
