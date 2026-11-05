import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "@fontsource/stix-two-text/400.css";
import "@fontsource/stix-two-text/400-italic.css";
import "@fontsource/stix-two-text/600.css";
import "@fontsource-variable/source-sans-3";
import "@fontsource/jetbrains-mono/400.css";
import "katex/dist/katex.min.css";
import "./styles.css";
import { App } from "./app/App";

createRoot(document.getElementById("root")!).render(<StrictMode><App /></StrictMode>);
