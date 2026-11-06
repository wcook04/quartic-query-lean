// Open one immutable reading edition with the client bundled into this site.
// Only an edition filename can come from a shared link; the client validates
// it, refuses redirects and checks every byte against the manifest.
import { openEdition as openWith } from "../../../tools/reader.mjs";

export type Reader = Awaited<ReturnType<typeof openWith>>;

export interface Edition {
  reader: Reader;
  /** e.g. edition-af18….json */
  permalink: string;
  /** A shared link named an older edition and we opened it. */
  pinnedOlder: boolean;
  /** A shared link named an edition this host does not hold. */
  missingRequested: string | null;
}

const API_ROOT = new URL(`${import.meta.env.BASE_URL}reading-api/v1/`, location.href).href;
const EDITION = /^edition-[a-f0-9]{64}\.json$/;

export async function openEdition(requested: string | null): Promise<Edition> {
  const latest = await openWith(API_ROOT);
  if (!requested || requested === latest.permalink) return { reader: latest, permalink: latest.permalink, pinnedOlder: false, missingRequested: null };
  if (!EDITION.test(requested)) return { reader: latest, permalink: latest.permalink, pinnedOlder: false, missingRequested: requested.slice(0, 80) };
  try {
    const older = await openWith(API_ROOT, { edition: requested });
    return { reader: older, permalink: older.permalink, pinnedOlder: true, missingRequested: null };
  } catch {
    return { reader: latest, permalink: latest.permalink, pinnedOlder: false, missingRequested: requested };
  }
}
