---
title: Converting animations from The Sims Medieval / The Sims 3 to The Sims 2 (Morita, reposted by honowo)
url: https://simblr.cc/ts2/tutorial/7096-converting-animations-from-the-sims-medieval-the-sims-3-to-the-sims-2.html
fetched: 2026-10-28
game: ts2, ts3, tsm
tags: animation, clip, ts2-anim, conversion, rig, tools
status: contradicted
author: Morita (reposted by honowo)
---
# TSM/TS3 CLIP -> TS2 ANIM conversion (Morita, reposted 2026-01-15)

Reverse direction of TS2 -> TS3 conversion, but the tool chain and rig facts transfer.

## Key facts
- Chain: s3pe export CLIP (TSM: `GameData/Shared/Packages/SASFullBuild1.package`) -> Blender <= 2.79 with
  "Sims 3 MLOD/MODL Tools" + "Sims 3 Clip Tool" (S3PY Animation Tools panel; "Load CLIP" with a rig bone
  selected) on omglo's "TS3 to TS2 conversion rig" (adult/child) -> export the bound Dr. Pixel TS2 base mesh to
  Milkshape -> Raw ANIM Frame exporter/importer -> "Sims2 AniMesh ANIM Exporter v10.1" -> SimPE.
- TSM has only adult, child and object clips; pick clips ending `_x` / `_y` (actor suffix) when several exist.
- After Load CLIP, set the Blender timeline end to the clip length by hand.
- Not every clip converts cleanly; MTS threads cover "leg does a 360 in the air" and "incorrect joint rotations in game".

## Contradiction to flag
- The tutorial sets AniMesh "Length (ms)" to **frames x 50 ms** ("one Frame=50 Milliseconds", i.e. 20 fps).
  Verified in game by XSauroxPlayer: EA TS2 ANIMs are baked at
  **24 fps (33.3 ticks of 1/800 s per key)**, key i at i/(n-1) of the duration. The 50 ms figure is the author's
  exporter setting, not EA data. Do not use it for EA ANIM timing.
