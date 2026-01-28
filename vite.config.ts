import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";

export default defineConfig({
  // 🔑 VERY IMPORTANT: frontend root
  root: path.resolve(__dirname, "client"),

  plugins: [react()],

 server: {
  port: 8080,
  strictPort: true,

  hmr: false, // 🔑 FIX: disable WebSocket HMR

  fs: {
    allow: [
      path.resolve(__dirname, "client"),
      path.resolve(__dirname, "shared"),
    ],
  },
},

  resolve: {
    alias: {
      "@": path.resolve(__dirname, "client"),
      "@shared": path.resolve(__dirname, "shared"),
    },
  },

  build: {
    outDir: path.resolve(__dirname, "dist"),
    emptyOutDir: true,
  },
});
