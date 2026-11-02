import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/analyze': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/dashboard-stats': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/predict-category': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/predict-market': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/predict-success': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/predict-complexity': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/investor-readiness': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/generate-swot': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/recommendations': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/similar-startups': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/history': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/trends': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
});
