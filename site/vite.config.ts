import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

// VITE_BASE_PATH is the folder the site is served from, such as /quartic/.
export default defineConfig(({ mode }) => {
  const base = loadEnv(mode, process.cwd(), "VITE_").VITE_BASE_PATH ?? process.env.VITE_BASE_PATH ?? "/";
  return {
    base,
    build: { assetsInlineLimit: 0, copyPublicDir: false },
    // The reading client lives in the repository's tools/ and is bundled from there.
    server: { fs: { allow: [".."] } },
    plugins: [react()],
  };
});
