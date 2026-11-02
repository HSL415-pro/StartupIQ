import React from 'react';
import { motion } from 'framer-motion';
import { ShieldCheck, AlertCircle, TrendingUp, AlertTriangle } from 'lucide-react';

export default function SwotMatrix({ swot }) {
  if (!swot) return null;

  const quadrants = [
    {
      key: 'strengths',
      title: 'Strengths',
      subtitle: 'Internal Advantages & Moats',
      icon: ShieldCheck,
      borderColor: 'border-emerald-500/30 hover:border-emerald-500/60',
      headerBg: 'bg-emerald-500/10 text-emerald-400',
      dotColor: 'bg-emerald-400',
      items: swot.strengths || []
    },
    {
      key: 'weaknesses',
      title: 'Weaknesses',
      subtitle: 'Internal Vulnerabilities & Friction',
      icon: AlertCircle,
      borderColor: 'border-rose-500/30 hover:border-rose-500/60',
      headerBg: 'bg-rose-500/10 text-rose-400',
      dotColor: 'bg-rose-400',
      items: swot.weaknesses || []
    },
    {
      key: 'opportunities',
      title: 'Opportunities',
      subtitle: 'Market Headwinds & Expansions',
      icon: TrendingUp,
      borderColor: 'border-blue-500/30 hover:border-blue-500/60',
      headerBg: 'bg-blue-500/10 text-blue-400',
      dotColor: 'bg-blue-400',
      items: swot.opportunities || []
    },
    {
      key: 'threats',
      title: 'Threats',
      subtitle: 'External Risks & Incumbents',
      icon: AlertTriangle,
      borderColor: 'border-purple-500/30 hover:border-purple-500/60',
      headerBg: 'bg-purple-500/10 text-purple-400',
      dotColor: 'bg-purple-400',
      items: swot.threats || []
    }
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
      {quadrants.map((quad, qIdx) => {
        const IconComponent = quad.icon;
        return (
          <motion.div
            key={quad.key}
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: qIdx * 0.1 }}
            className={`glass-panel rounded-2xl p-6 border ${quad.borderColor} transition-all duration-300 relative overflow-hidden`}
          >
            {/* Header */}
            <div className="flex items-center justify-between pb-4 border-b border-slate-800">
              <div className="flex items-center space-x-3">
                <div className={`p-2.5 rounded-xl ${quad.headerBg}`}>
                  <IconComponent className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-bold text-white tracking-wide">{quad.title}</h3>
                  <p className="text-xs text-slate-400">{quad.subtitle}</p>
                </div>
              </div>
              <span className="text-xs font-semibold px-2 py-0.5 rounded-md bg-slate-800 text-slate-300">
                {quad.items.length} Factors
              </span>
            </div>

            {/* Content List */}
            <ul className="mt-4 space-y-3.5">
              {quad.items.map((item, idx) => (
                <li key={idx} className="flex items-start space-x-3 text-sm group">
                  <span className={`w-2 h-2 rounded-full ${quad.dotColor} mt-2 flex-shrink-0 group-hover:scale-125 transition-transform`} />
                  <div>
                    <span className="font-semibold text-slate-200">
                      {typeof item === 'string' ? item : item.title}
                    </span>
                    {typeof item === 'object' && item.detail && (
                      <p className="text-xs text-slate-400 mt-0.5 leading-relaxed">
                        {item.detail}
                      </p>
                    )}
                  </div>
                </li>
              ))}
            </ul>
          </motion.div>
        );
      })}
    </div>
  );
}
