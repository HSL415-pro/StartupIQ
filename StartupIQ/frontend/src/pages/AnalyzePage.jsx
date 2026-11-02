import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  Sparkles,
  Rocket,
  AlertCircle,
  HelpCircle,
  Cpu,
  Layers,
  Target,
  FileText,
  RotateCcw
} from 'lucide-react';
import api from '../services/api';
import LoadingScreen from '../components/LoadingScreen';
import { SAMPLE_IDEAS } from '../utils/sampleIdeas';

const CATEGORIES = [
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

export default function AnalyzePage() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    startup_name: '',
    industry: 'AI',
    description: '',
    problem_statement: '',
    target_audience: '',
    technology_stack: ''
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [serverError, setServerError] = useState('');

  const validateForm = () => {
    const errs = {};
    if (!formData.startup_name.trim() || formData.startup_name.length < 2) {
      errs.startup_name = 'Startup name must be at least 2 characters.';
    }
    if (!formData.description.trim() || formData.description.length < 15) {
      errs.description = 'Please provide a descriptive explanation (minimum 15 characters).';
    }
    if (!formData.problem_statement.trim() || formData.problem_statement.length < 15) {
      errs.problem_statement = 'Please clearly articulate the problem being solved (minimum 15 characters).';
    }
    if (!formData.target_audience.trim() || formData.target_audience.length < 3) {
      errs.target_audience = 'Target audience is required (e.g. Enterprise Data Teams).';
    }
    if (!formData.technology_stack.trim() || formData.technology_stack.length < 3) {
      errs.technology_stack = 'Technology stack is required (e.g. Python, PyTorch, React, PostgreSQL).';
    }

    setErrors(errs);
    return Object.keys(errs).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: null }));
    }
    if (serverError) setServerError('');
  };

  const handleApplySample = (sample) => {
    setFormData(sample.data);
    setErrors({});
    setServerError('');
  };

  const handleReset = () => {
    setFormData({
      startup_name: '',
      industry: 'AI',
      description: '',
      problem_statement: '',
      target_audience: '',
      technology_stack: ''
    });
    setErrors({});
    setServerError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setLoading(true);
    setServerError('');

    try {
      const response = await api.analyzeIdea(formData);
      if (response && response.data) {
        // Cache result in sessionStorage for instant retrieval
        sessionStorage.setItem(`startupiq_analysis_${response.data.id}`, JSON.stringify(response.data));
        navigate(`/results/${response.data.id}`, { state: { analysis: response.data } });
      } else {
        throw new Error('Invalid response received from server.');
      }
    } catch (err) {
      console.error('Analysis error:', err);
      const detail = err.response?.data?.detail || err.message || 'Server error occurred during evaluation.';
      setServerError(detail);
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {loading && <LoadingScreen startupName={formData.startup_name || "Your Startup"} />}

      {/* Header */}
      <div className="text-center max-w-2xl mx-auto mb-10">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold mb-3">
          <Sparkles className="w-3.5 h-3.5" />
          <span>Venture Intelligence Engine</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
          Analyze Your Startup Idea
        </h1>
        <p className="text-sm text-slate-400 mt-2">
          Submit your product vision. StartupIQ’s 9 AI modules will evaluate innovation, market size, complexity, and investor readiness.
        </p>
      </div>

      {/* 1-Click Sample Pre-Fill Buttons */}
      <div className="glass-panel p-4 sm:p-5 rounded-2xl mb-8 border border-slate-800">
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center">
            <Rocket className="w-3.5 h-3.5 text-indigo-400 mr-1.5" />
            Quick Test: Pre-Fill With Sample Ideas
          </span>
          <button
            type="button"
            onClick={handleReset}
            className="text-xs text-slate-500 hover:text-slate-300 flex items-center space-x-1"
          >
            <RotateCcw className="w-3 h-3" />
            <span>Clear Form</span>
          </button>
        </div>

        <div className="flex flex-wrap gap-2.5">
          {SAMPLE_IDEAS.map((sample, idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => handleApplySample(sample)}
              className="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-900/80 hover:bg-indigo-600/20 border border-slate-800 hover:border-indigo-500/40 text-slate-200 hover:text-indigo-300 transition-all text-left flex items-center space-x-2"
            >
              <span className="w-2 h-2 rounded-full bg-indigo-400" />
              <span>{sample.title}</span>
              <span className="text-[10px] text-slate-500">({sample.badge})</span>
            </button>
          ))}
        </div>
      </div>

      {/* Main Submission Form */}
      <motion.form
        initial={{ opacity: 0, y: 15 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        onSubmit={handleSubmit}
        className="glass-panel p-6 sm:p-8 rounded-3xl border border-slate-800 space-y-6 relative"
      >
        {serverError && (
          <div className="p-4 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs flex items-start space-x-3">
            <AlertCircle className="w-5 h-5 text-rose-400 flex-shrink-0 mt-0.5" />
            <div>
              <strong className="block font-bold">Analysis Failed:</strong>
              <span>{serverError}</span>
            </div>
          </div>
        )}

        {/* Row 1: Startup Name & Industry */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
              Startup Name <span className="text-rose-400">*</span>
            </label>
            <input
              type="text"
              name="startup_name"
              value={formData.startup_name}
              onChange={handleChange}
              placeholder="e.g. AgenticFlow, VaultPay, AuraCare"
              className={`w-full px-4 py-3 rounded-xl text-sm glass-input ${
                errors.startup_name ? 'border-rose-500' : ''
              }`}
            />
            {errors.startup_name && (
              <p className="text-rose-400 text-xs mt-1.5">{errors.startup_name}</p>
            )}
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
              Primary Industry / Category <span className="text-rose-400">*</span>
            </label>
            <select
              name="industry"
              value={formData.industry}
              onChange={handleChange}
              className="w-full px-4 py-3 rounded-xl text-sm glass-input bg-slate-900 text-slate-100"
            >
              {CATEGORIES.map((cat) => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Startup Description */}
        <div>
          <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
            Startup Description & Solution <span className="text-rose-400">*</span>
          </label>
          <textarea
            rows={3}
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="Describe what your startup does, core features, and architectural wedge..."
            className={`w-full px-4 py-3 rounded-xl text-sm glass-input ${
              errors.description ? 'border-rose-500' : ''
            }`}
          />
          {errors.description && (
            <p className="text-rose-400 text-xs mt-1.5">{errors.description}</p>
          )}
        </div>

        {/* Problem Statement */}
        <div>
          <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
            Acute Problem Statement <span className="text-rose-400">*</span>
          </label>
          <textarea
            rows={2}
            name="problem_statement"
            value={formData.problem_statement}
            onChange={handleChange}
            placeholder="What specific acute pain point or friction does your target customer face today?"
            className={`w-full px-4 py-3 rounded-xl text-sm glass-input ${
              errors.problem_statement ? 'border-rose-500' : ''
            }`}
          />
          {errors.problem_statement && (
            <p className="text-rose-400 text-xs mt-1.5">{errors.problem_statement}</p>
          )}
        </div>

        {/* Row 2: Target Audience & Tech Stack */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div>
            <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
              Target Audience / Customer <span className="text-rose-400">*</span>
            </label>
            <input
              type="text"
              name="target_audience"
              value={formData.target_audience}
              onChange={handleChange}
              placeholder="e.g. Enterprise Data Engineering Teams, SMB Exporters"
              className={`w-full px-4 py-3 rounded-xl text-sm glass-input ${
                errors.target_audience ? 'border-rose-500' : ''
              }`}
            />
            {errors.target_audience && (
              <p className="text-rose-400 text-xs mt-1.5">{errors.target_audience}</p>
            )}
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">
              Technology Stack <span className="text-rose-400">*</span>
            </label>
            <input
              type="text"
              name="technology_stack"
              value={formData.technology_stack}
              onChange={handleChange}
              placeholder="e.g. Python, PyTorch, FastAPI, React, PostgreSQL"
              className={`w-full px-4 py-3 rounded-xl text-sm glass-input ${
                errors.technology_stack ? 'border-rose-500' : ''
              }`}
            />
            {errors.technology_stack && (
              <p className="text-rose-400 text-xs mt-1.5">{errors.technology_stack}</p>
            )}
          </div>
        </div>

        {/* Submit Button */}
        <div className="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
          <span className="text-xs text-slate-400">
            All 9 AI models execute synchronously. Results are persisted to your SQLite history.
          </span>

          <button
            type="submit"
            disabled={loading}
            className="w-full sm:w-auto px-8 py-3.5 rounded-2xl text-sm font-bold text-white bg-gradient-to-r from-indigo-600 via-indigo-500 to-purple-600 hover:from-indigo-500 hover:to-purple-500 shadow-xl shadow-indigo-500/30 transition-all hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center space-x-2 disabled:opacity-50"
          >
            <Sparkles className="w-4 h-4" />
            <span>Generate Full AI Analysis</span>
          </button>
        </div>
      </motion.form>
    </div>
  );
}
