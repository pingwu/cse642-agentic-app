import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// In Docker the backend is reachable as http://backend:8000; on the host it is 127.0.0.1:8000.
const apiTarget = process.env.API_URL || "http://127.0.0.1:8000";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: { "/api": apiTarget },
    // Polling makes edits show up inside Docker on Windows.
    watch: { usePolling: process.env.CHOKIDAR_USEPOLLING === "true" },
  },
});
