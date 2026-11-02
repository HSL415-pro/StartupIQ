import React from 'react';
import { Link } from 'react-router-dom';
import { Rocket, ShieldCheck, Cpu, Database, Heart } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="border-t border-slate-800/80 bg-surface-950/60 mt-20 text-slate-400 text-xs no-print">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand Info */}
          <div className="space-y-3 md:col-span-1">
            <div className="flex items-center space-x-2.5">
              <div className="w-7 h-7 rounded-lg bg-indigo-600 flex items-center justify-center text-white">
                <Rocket className="w-4 h-4" />
              </div>
              <span className="font-extrabold text-white text-base tracking-tight">
                Startup<span className="text-indigo-400">IQ</span>
              </span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              Institutional-grade AI platform evaluating early-stage venture ideas across 9 multi-dimensional vectors.
            </p>
            <div className="flex items-center space-x-2 text-[11px] text-slate-500">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <span>Production Model v1.0 • Python 3.13</span>
            </div>
          </div>

          {/* AI Modules Links */}
          <div>
            <h4 className="font-semibold text-slate-200 uppercase tracking-wider text-[11px] mb-3">
              Core AI Modules
            </h4>
            <ul className="space-y-2">
              <li>Category Detection (TF-IDF + Logistic)</li>
              <li>Innovation Analyzer (0-100 Gauge)</li>
              <li>Market Potential Engine (TAM Model)</li>
              <li>Technical Complexity Analyzer</li>
              <li>Success Probability Predictor</li>
              <li>Similar Startup Finder (Cosine Vector)</li>
            </ul>
          </div>

          {/* Platform Navigation */}
          <div>
            <h4 className="font-semibold text-slate-200 uppercase tracking-wider text-[11px] mb-3">
              Platform
            </h4>
            <ul className="space-y-2">
              <li><Link to="/analyze" className="hover:text-indigo-400 transition-colors">Analyze Startup</Link></li>
              <li><Link to="/trends" className="hover:text-indigo-400 transition-colors">Startup Trends & Benchmarks</Link></li>
              <li><Link to="/history" className="hover:text-indigo-400 transition-colors">Analysis History</Link></li>
              <li><Link to="/about" className="hover:text-indigo-400 transition-colors">Methodology & Architecture</Link></li>
              <li><a href="http://127.0.0.1:8000/docs" target="_blank" rel="noreferrer" className="hover:text-indigo-400 transition-colors">FastAPI Interactive Docs</a></li>
            </ul>
          </div>

          {/* Tech Stack Specs */}
          <div>
            <h4 className="font-semibold text-slate-200 uppercase tracking-wider text-[11px] mb-3">
              Production Stack
            </h4>
            <ul className="space-y-2 text-slate-400">
              <li className="flex items-center space-x-1.5">
                <Cpu className="w-3.5 h-3.5 text-indigo-400" />
                <span>FastAPI + Python 3.13</span>
              </li>
              <li className="flex items-center space-x-1.5">
                <ShieldCheck className="w-3.5 h-3.5 text-purple-400" />
                <span>Scikit-Learn, Pandas, NumPy, Joblib</span>
              </li>
              <li className="flex items-center space-x-1.5">
                <Database className="w-3.5 h-3.5 text-blue-400" />
                <span>SQLite with WAL Engine</span>
              </li>
              <li className="flex items-center space-x-1.5">
                <Rocket className="w-3.5 h-3.5 text-pink-400" />
                <span>React 18 + Vite + Tailwind CSS</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-10 pt-6 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between text-[11px] text-slate-500 gap-3">
          <p>© {new Date().getFullYear()} StartupIQ Inc. AI-Powered Startup Idea Analyzer. All rights reserved.</p>
          <div className="flex items-center space-x-4">
            <span className="text-slate-500">Built for Founders, Angels, & Venture Accelerators</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
