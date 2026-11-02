import axios from 'axios';

// Support both standard proxy and explicit backend URL from env
const API_BASE = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

const client = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000,
});

export const api = {
  // Comprehensive analysis
  analyzeIdea: async (payload) => {
    const res = await client.post('/analyze', payload);
    return res.data;
  },

  // Platform Dashboard & Metrics
  getDashboardStats: async () => {
    const res = await client.get('/dashboard-stats');
    return res.data;
  },

  // Sector Trends & Analytics
  getTrends: async () => {
    const res = await client.get('/trends');
    return res.data;
  },

  // Historical Analyses
  getHistory: async (params = {}) => {
    const res = await client.get('/history', { params });
    return res.data;
  },

  getHistoryDetail: async (analysisId) => {
    const res = await client.get(`/history/${analysisId}`);
    return res.data;
  },

  deleteHistory: async (historyId) => {
    const res = await client.delete(`/history/${historyId}`);
    return res.data;
  },

  // Specific AI Modules
  predictCategory: async (payload) => {
    const res = await client.post('/predict-category', payload);
    return res.data;
  },

  predictMarket: async (payload) => {
    const res = await client.post('/predict-market', payload);
    return res.data;
  },

  predictComplexity: async (payload) => {
    const res = await client.post('/predict-complexity', payload);
    return res.data;
  },

  predictSuccess: async (payload) => {
    const res = await client.post('/predict-success', payload);
    return res.data;
  },

  getInvestorReadiness: async (payload) => {
    const res = await client.post('/investor-readiness', payload);
    return res.data;
  },

  generateSwot: async (payload) => {
    const res = await client.post('/generate-swot', payload);
    return res.data;
  },

  getRecommendations: async (payload) => {
    const res = await client.post('/recommendations', payload);
    return res.data;
  },

  getSimilarStartups: async (payload) => {
    const res = await client.post('/similar-startups', payload);
    return res.data;
  },
};

export default api;
