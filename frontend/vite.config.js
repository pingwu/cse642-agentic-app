import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// API_TARGET is set by docker-compose.yml; on your own machine it falls back to the local backend.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    watch: process.env.CHOKIDAR_USEPOLLING ? { usePolling: true } : undefined,
    proxy: { "/api": process.env.API_TARGET || "http://127.0.0.1:8000" },
  },
});
