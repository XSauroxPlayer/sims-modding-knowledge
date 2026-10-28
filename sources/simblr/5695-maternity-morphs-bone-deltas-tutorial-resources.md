---
title: Maternity morphs & bone deltas tutorial + resources (VirtualHugs)
url: https://simblr.cc/ts3/tutorial/5695-maternity-morphs-bone-deltas-tutorial-resources.html
fetched: 2026-10-28
game: ts3
tags: cas, mesh, bgeo, bond, morphs
status: community-reported
author: VirtualHugs
---
# TS3 maternity morphs and bone deltas (BGEO, BOND)

## Key facts
- Tools: S3PE, CmarNYC Mesh Toolkit, Blender + GEOM Tools, BoneDeltaEditor, S3OC (CAS Part clone, uncheck Renumber).
- Morph: export GEOM LODs (skip `-fat` etc.), combine multi-group LODs (Mesh Toolkit "Combine Meshes"),
  "Auto-create Morph Mesh" from an EA reference (base simgeom + SPECIAL morph); LOD2/3 can reuse the LOD1 morph as
  reference; "Make Clothing/Hair BGEO" and replace the `_special` BGEO. Store items keep morphs as GEOMs
  ("Add Morphs to Clothing/Hair").
- CASP grid: `ClothingCategory > ValidForMaternity = True`.
- Bone deltas: replace the maternity BOND (ends `BOND4` / `special`) with an EA BOND from a similar-shaped garment.
  EA ships 90+ maternity BONDs, many unused. Maternity morphs also add overall weight, so BOND deltas are needed to
  stop clipping at belly, thighs, arms, hips.
- BoneDeltaEditor needs an updated `bones.xml` (Pets_updated_bones.zip) to show bone names.
- BOND also offsets Sim slots per body shape (see `topics/ik-and-slots.md`).
