// Copied from proof-reader web/src at e2df888, Copyright 2026 proof-reader
// contributors, Apache-2.0 (adapted from Lean Exposition's map).
// A remembered view of the map: what is unfolded, the camera and the mode.
// The page stores one per history entry and hands it back on Back.

import type { MapMode } from "./representation";

export interface MapScene {
  camera: { x: number; y: number; k: number };
  expanded: string[];
  mode: MapMode;
  /**
   * Optional: one drawn card and where it sat on screen. A layout rebuilt from
   * scratch may place cards a little differently from one grown step by step,
   * so restoring keeps this card exactly where it was rather than trusting
   * world coordinates alone.
   */
  anchor?: { id: string; x: number; y: number };
}
