---
title: Tutorials:Understanding the Scenegraph
url: https://simswiki.info/index.php?title=Tutorials:Understanding_the_Scenegraph
fetched: 2026-10-28
game: ts2
tags: ts2, scenegraph, cres, shpe, gmnd, gmdc, txmt, txtr, mmat, recolour
status: community-reported
author: Echo
---
# Understanding the Scenegraph (simswiki, Echo, TS2)

Synthesis: `topics/ts2-formats.md`.

- Object scenegraph chain: **CRES -> SHPE -> (GMND -> GMDC) and (TXMT -> TXTR)**; MMAT links a CRES straight to a
  TXMT for recolours; LGHT hangs off the CRES. The CRES holds the skeleton and the placement of meshes, lights and
  slots relative to the object origin.
- SHPE maps each mesh subset to its default material (one line per subset/TXMT in the Parts tab); renaming or adding a
  subset requires editing the SHPE. GMND flags which subsets are shadows, recolourable, or state-changing.
- How links are stored:
  - CRES -> SHPE and GMND -> GMDC: by **TGI** (Reference tab).
  - SHPE -> GMND: by **name** (Items tab). SHPE -> TXMT: by name per subset (Parts tab).
  - TXMT -> TXTR: **twice**, `stdMatBaseTextureName` property and the File List tab; both must match.
  - MMAT -> TXMT: MMAT `name`; MMAT -> CRES: MMAT `modelName` = CRES name.
- A recolour package is TXTR + TXMT + MMAT; the MMAT finds the object by CRES name in any loaded package
  ("extern" in SimPE's Scenegrapher).
- Diagnosis: blue flashing textures, untextured subsets or missing parts usually mean one broken link; after renaming
  resources run SimPE **Fix Integrity**.

## Against verified findings
- Matches the traversal used by XSauroxPlayer's TS2 extractor (CRES/SHPE/GMND/GMDC and TXMT texture names); no
  conflict.
