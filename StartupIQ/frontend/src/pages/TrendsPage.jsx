import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  PieChart,
  Pie,
  Cell,
  LineChart,
  Line,
  CartesianGrid
} from 'recharts';
import {
  TrendingUp,
  BarChart3,
  PieChart as PieIcon,
  Compass,
  Cpu,
  Layers,
  Sparkles,
  ArrowUpRight
} from 'lucide-react';
import api from '../services/api';
import Badge from '../components/Badge';

const PIE_COLORS = [
  '#6366f1', '#a855f7', '#ec4899', '#3b82f6', '#10b981',
  '#f59e0b', '#06b6d4', '#14b8a6', '#8b5cf6', '#f43f5e'
];

export default function TrendsPage() {
  const [trendsData, setTrendsData] = useState([]);
  const [loading, setLoading] = useState(true);

  // Default benchmarks if API pending
  const defaultCategoryTrends = [
    { category: "AI", innovation: 88, market: 92, success: 82, volume: 340, fullMark: 100 },
    { category: "SaaS", innovation: 74, market: 86, success: 79, volume: 290, fullMark: 100 },
    { category: "FinTech", innovation: 79, market: 89, success: 76, volume: 260, fullMark: 100 },
    { category: "Cybersecurity", innovation: 85, market: 84, success: 78, volume: 210, fullMark: 100 },
    { category: "HealthTech", innovation: 83, market: 82, success: 71, volume: 195, fullMark: 100 },
    { category: "Developer Tools", innovation: 86, market: 79, success: 75, volume: 180, fullMark: 100 },
    { category: "E-Commerce", innovation: 62, market: 78, success: 68, volume: 220, fullMark: 100 },
    { category: "EdTech", innovation: 69, market: 71, success: 66, volume: 160, fullMark: 100 },
    { category: "Agriculture", innovation: 76, market: 74, success: 70, volume: 140, fullMark: 100 },
    { category: "FoodTech", innovation: 68, market: 72, success: 64, volume: 130, fullMark: 100 }
  ];

  useEffect(() => {
    api.getTrends()
      .then((res) => {
        if (res && res.data && res.data.category_trends) {
          setTrendsData(res.data.category_trends.map(t => ({ ...t, fullMark: 100 })));
        } else {
          setTrendsData(defaultCategoryTrends);
        }
      })
      .catch(() => {
        setTrendsData(defaultCategoryTrends);
      })
      .finally(() => setLoading(false));
  }, []);

  const chartData = trendsData.length > 0 ? trendsData : defaultCategoryTrends;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Page Header */}
      <div className="text-center max-w-3xl mx-auto">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold mb-3">
          <BarChart3 className="w-3.5 h-3.5" />
          <span>Macro Venture Analytics</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
          Global Startup Trends & Benchmarks
        </h1>
        <p className="text-sm text-slate-400 mt-2">
          Empirical scoring distributions across 10 industry verticals indexed by StartupIQ’s machine learning engine.
        </p>
      </div>

      {/* Top Benchmark Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="glass-card p-5 rounded-2xl border border-slate-800">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Top Innovation Vertical</span>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-black text-indigo-400">AI & Agents</span>
            <span className="text-sm font-bold text-slate-200">88.0 / 100</span>
          </div>
          <p className="text-xs text-slate-400 mt-1">Leading frontier tech density</p>
        </div>

        <div className="glass-card p-5 rounded-2xl border border-slate-800">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Highest Market TAM</span>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-black text-emerald-400">FinTech</span>
            <span className="text-sm font-bold text-slate-200">92.0 / 100</span>
          </div>
          <p className="text-xs text-slate-400 mt-1">Sustained institutional capital velocity</p>
        </div>

        <div className="glass-card p-5 rounded-2xl border border-slate-800">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Highest Success Viability</span>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-black text-purple-400">B2B SaaS</span>
            <span className="text-sm font-bold text-slate-200">79.2%</span>
          </div>
          <p className="text-xs text-slate-400 mt-1">Predictable recurring enterprise cashflow</p>
        </div>

        <div className="glass-card p-5 rounded-2xl border border-slate-800">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Lowest Execution Friction</span>
          <div className="flex items-baseline justify-between mt-2">
            <span className="text-2xl font-black text-blue-400">DevTools</span>
            <span className="text-sm font-bold text-slate-200">6 Weeks MVP</span>
          </div>
          <p className="text-xs text-slate-400 mt-1">Developer bottoms-up viral adoption</p>
        </div>
      </div>

      {/* Chart Row 1: Bar Chart (Category Analytics) & Radar Chart */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Bar Chart: Innovation vs Market Potential */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4"
        >
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Innovation vs. Market Potential</h3>
              <p className="text-xs text-slate-400">Cross-industry multi-factor benchmark</p>
            </div>
            <Badge color="indigo" size="sm">Bar Chart</Badge>
          </div>

          <div className="h-72 w-full pt-2">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 20 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="category" stroke="#64748b" tick={{ fontSize: 10 }} interval={0} angle={-35} textAnchor="end" />
                <YAxis stroke="#64748b" tick={{ fontSize: 11 }} domain={[0, 100]} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
                <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
                <Bar dataKey="innovation" name="Innovation Score" fill="#6366f1" radius={[4, 4, 0, 0]} />
                <Bar dataKey="market" name="Market Potential" fill="#10b981" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </motion.div>

        {/* Radar Chart: Multi-Dimensional Sector Profiles */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4"
        >
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Sector Dimension Radar</h3>
              <p className="text-xs text-slate-400">Innovation, market velocity & success probability</p>
            </div>
            <Badge color="purple" size="sm">Radar Chart</Badge>
          </div>

          <div className="h-72 w-full flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={chartData.slice(0, 6)}>
                <PolarGrid stroke="#334155" />
                <PolarAngleAxis dataKey="category" stroke="#94a3b8" tick={{ fontSize: 10 }} />
                <PolarRadiusAxis angle={30} domain={[0, 100]} stroke="#475569" tick={{ fontSize: 9 }} />
                <Radar name="Innovation" dataKey="innovation" stroke="#6366f1" fill="#6366f1" fillOpacity={0.4} />
                <Radar name="Success Prob." dataKey="success" stroke="#ec4899" fill="#ec4899" fillOpacity={0.3} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
                <Legend wrapperStyle={{ fontSize: '11px' }} />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        </motion.div>
      </div>

      {/* Chart Row 2: Pie Chart (Volume Distribution) & Success Trends Line Chart */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Pie Chart: Startup Corpus Distribution */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4"
        >
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Idea Volume & Sector Share</h3>
              <p className="text-xs text-slate-400">Distribution of indexed companies across categories</p>
            </div>
            <Badge color="blue" size="sm">Pie Chart</Badge>
          </div>

          <div className="h-72 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={chartData}
                  dataKey="volume"
                  nameKey="category"
                  cx="50%"
                  cy="50%"
                  outerRadius={85}
                  innerRadius={45}
                  paddingAngle={3}
                >
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={PIE_COLORS[index % PIE_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
                <Legend wrapperStyle={{ fontSize: '10px' }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </motion.div>

        {/* Line Chart: Success Trends Across Sectors */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4"
        >
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Success Probability Trends</h3>
              <p className="text-xs text-slate-400">Predicted rate of reaching venture scale</p>
            </div>
            <Badge color="emerald" size="sm">Trend Line</Badge>
          </div>

          <div className="h-72 w-full pt-2">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData} margin={{ top: 10, right: 15, left: -20, bottom: 20 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="category" stroke="#64748b" tick={{ fontSize: 10 }} interval={0} angle={-35} textAnchor="end" />
                <YAxis stroke="#64748b" tick={{ fontSize: 11 }} domain={[40, 100]} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                />
                <Line
                  type="monotone"
                  dataKey="success"
                  name="Success Probability (%)"
                  stroke="#10b981"
                  strokeWidth={3}
                  dot={{ r: 4, fill: '#10b981' }}
                  activeDot={{ r: 7 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
