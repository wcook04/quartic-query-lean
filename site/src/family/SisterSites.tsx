// The footer's list of Will Cook's websites, the same on every site of the
// family. Adapted from lean-exposition site/src/app/SisterSites.tsx at ed08df8,
// Copyright 2026 lean-exposition contributors, Apache-2.0.
import { FAMILY } from "./family";

export function SisterSites() {
  return (
    <nav className="fam-sites" aria-label={`${FAMILY.owner.name}'s websites`}>
      <p className="fam-sites__title">More from {FAMILY.owner.name}</p>
      <ul className="fam-sites__list">
        {FAMILY.sites.map((site) => <li key={site.id}><a href={site.url}>{site.short}</a></li>)}
        <li><a href={FAMILY.owner.home}>All websites and videos</a></li>
      </ul>
    </nav>
  );
}
