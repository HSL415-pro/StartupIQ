import React from 'react';

const colorStyles = {
  emerald: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/25',
  blue: 'bg-blue-500/10 text-blue-400 border-blue-500/25',
  indigo: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/25',
  purple: 'bg-purple-500/10 text-purple-400 border-purple-500/25',
  amber: 'bg-amber-500/10 text-amber-400 border-amber-500/25',
  rose: 'bg-rose-500/10 text-rose-400 border-rose-500/25',
  slate: 'bg-slate-500/10 text-slate-400 border-slate-500/25',
};

export default function Badge({ children, color = 'indigo', className = '', size = 'md' }) {
  const sizeClasses = size === 'sm' ? 'px-2 py-0.5 text-xs' : 'px-2.5 py-1 text-xs';
  const colorClass = colorStyles[color] || colorStyles.indigo;

  return (
    <span className={`inline-flex items-center font-medium rounded-full border ${sizeClasses} ${colorClass} ${className}`}>
      {children}
    </span>
  );
}
