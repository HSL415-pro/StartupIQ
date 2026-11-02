import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  History as HistoryIcon,
  Search,
  Filter,
  ArrowUpDown,
  Trash2,
  ExternalLink,
  Sparkles,
  Calendar,
  AlertCircle
} from 'lucide-react';
import api from '../services/api';
import Badge from '../components/Badge';

const CATEGORIES = [
  "All",
  "AI",
  "SaaS",
  "FoodTech",
  "HealthTech",
  "FinTech",
  "EdTech",
  "Agriculture",
  "Cybersecurity",
  "E-Commerce",
  "Developer Tools"
];

export default function HistoryPage() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [sortBy, setSortBy] = useState('created_at');
  const [order, setOrder] = useState('desc');
  const [deleteId, setDeleteId] = useState(null);

  const fetchHistory = () => {
    setLoading(true);
    api.getHistory({
      search: search || undefined,
      category: selectedCategory !== 'All' ? selectedCategory : undefined,
      sort_by: sortBy,
      order: order
    })
      .then((res) => {
        if (res && res.data) {
          setHistory(res.data);
        }
      })
      .catch((err) => {
        console.error('History fetch error:', err);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    const debounce = setTimeout(() => {
      fetchHistory();
    }, 250);
    return () => clearTimeout(debounce);
  }, [search, selectedCategory, sortBy, order]);

  const handleDelete = async (id, e) => {
    e.stopPropagation();
    if (!window.confirm(`Are you sure you want to delete analysis record #${id}?`)) return;

    try {
      await api.deleteHistory(id);
      setHistory(prev => prev.filter(item => item.id !== id && item.analysis_id !== id));
    } catch (err) {
      console.error('Failed to delete history item:', err);
      alert('Could not delete record.');
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold mb-2">
            <HistoryIcon className="w-3.5 h-3.5" />
            <span>SQLite Persistence Vault</span>
          </div>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Analysis History
          </h1>
          <p className="text-xs text-slate-400 mt-1">
            Search, filter, and inspect past evaluations executed by StartupIQ.
          </p>
        </div>

        <Link
          to="/analyze"
          className="px-5 py-2.5 rounded-xl text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-500 transition-colors inline-flex items-center space-x-1.5 self-start md:self-auto shadow-md shadow-indigo-500/20"
        >
          <Sparkles className="w-3.5 h-3.5" />
          <span>New Analysis</span>
        </Link>
      </div>

      {/* Filter & Search Bar */}
      <div className="glass-panel p-4 rounded-2xl border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-4">
        {/* Search */}
        <div className="relative w-full md:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search startup name or summary..."
            className="w-full pl-10 pr-4 py-2 rounded-xl text-xs glass-input"
          />
        </div>

        {/* Filter by Category & Sort */}
        <div className="flex flex-wrap items-center gap-3 w-full md:w-auto">
          {/* Category */}
          <div className="flex items-center space-x-2">
            <Filter className="w-3.5 h-3.5 text-slate-400" />
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="px-3 py-1.5 rounded-xl text-xs glass-input bg-slate-900 text-slate-200"
            >
              {CATEGORIES.map(cat => (
                <option key={cat} value={cat}>Category: {cat}</option>
              ))}
            </select>
          </div>

          {/* Sort By */}
          <div className="flex items-center space-x-2">
            <ArrowUpDown className="w-3.5 h-3.5 text-slate-400" />
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="px-3 py-1.5 rounded-xl text-xs glass-input bg-slate-900 text-slate-200"
            >
              <option value="created_at">Date Created</option>
              <option value="overall_score">Overall Score</option>
              <option value="success_probability">Success Probability</option>
              <option value="investor_readiness_score">Investor Readiness</option>
              <option value="startup_name">Startup Name</option>
            </select>
          </div>

          {/* Order */}
          <button
            onClick={() => setOrder(order === 'desc' ? 'asc' : 'desc')}
            className="px-3 py-1.5 rounded-xl text-xs glass-panel text-slate-300 hover:text-white"
          >
            {order.toUpperCase()}
          </button>
        </div>
      </div>

      {/* History List */}
      {loading ? (
        <div className="py-16 text-center text-slate-400 text-xs">
          Loading historical records...
        </div>
      ) : history.length === 0 ? (
        <div className="glass-panel p-12 rounded-3xl text-center border border-slate-800">
          <AlertCircle className="w-8 h-8 text-slate-500 mx-auto mb-3" />
          <h3 className="text-base font-bold text-white">No Analyses Found</h3>
          <p className="text-xs text-slate-400 mt-1 max-w-sm mx-auto">
            {search || selectedCategory !== 'All'
              ? 'No evaluations match your search filter.'
              : 'You have not evaluated any startup ideas yet.'}
          </p>
          <Link
            to="/analyze"
            className="mt-4 inline-block px-5 py-2 rounded-xl text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-500 transition-colors"
          >
            Run First Analysis
          </Link>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-3.5">
          {history.map((item, idx) => (
            <motion.div
              key={item.id}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3, delay: idx * 0.04 }}
              className="glass-card p-5 rounded-2xl border border-slate-800/80 hover:border-indigo-500/40 transition-all flex flex-col sm:flex-row sm:items-center justify-between gap-4"
            >
              <div className="space-y-1.5 max-w-xl">
                <div className="flex items-center space-x-2">
                  <h3 className="text-base font-bold text-white">
                    {item.startup_name}
                  </h3>
                  <Badge color="slate" size="sm">
                    {item.category}
                  </Badge>
                  <span className="text-[11px] text-slate-500 flex items-center">
                    <Calendar className="w-3 h-3 mr-1" />
                    {new Date(item.created_at).toLocaleDateString()}
                  </span>
                </div>
                {item.summary && (
                  <p className="text-xs text-slate-300 leading-relaxed line-clamp-1">
                    {item.summary}
                  </p>
                )}
              </div>

              {/* Metrics Pills & Actions */}
              <div className="flex items-center space-x-4 self-end sm:self-center flex-shrink-0">
                <div className="text-right">
                  <span className="block text-[10px] text-slate-400 uppercase tracking-wider font-semibold">
                    Overall
                  </span>
                  <span className="text-base font-extrabold text-white">
                    {Math.round(item.overall_score || 75)}
                  </span>
                </div>

                <div className="text-right">
                  <span className="block text-[10px] text-slate-400 uppercase tracking-wider font-semibold">
                    Success
                  </span>
                  <span className="text-base font-extrabold text-emerald-400">
                    {Math.round(item.success_probability || 70)}%
                  </span>
                </div>

                <div className="text-right">
                  <span className="block text-[10px] text-slate-400 uppercase tracking-wider font-semibold">
                    Investor
                  </span>
                  <span className="text-base font-extrabold text-purple-400">
                    {Math.round(item.investor_readiness_score || 70)}
                  </span>
                </div>

                <div className="flex items-center space-x-1.5 pl-2 border-l border-slate-800">
                  <Link
                    to={`/results/${item.analysis_id || item.id}`}
                    className="p-2 rounded-xl bg-indigo-600/20 text-indigo-400 hover:bg-indigo-600 hover:text-white transition-colors"
                    title="View Full Report"
                  >
                    <ExternalLink className="w-4 h-4" />
                  </Link>
                  <button
                    onClick={(e) => handleDelete(item.id, e)}
                    className="p-2 rounded-xl bg-rose-500/10 text-rose-400 hover:bg-rose-500 hover:text-white transition-colors"
                    title="Delete Record"
                  >
                    <Trash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      )}
    </div>
  );
}
