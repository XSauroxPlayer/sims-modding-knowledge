---
title: TSM to TS3 Conversion (Danjaley)
url: https://danjaleyreblogs.tumblr.com/post/157311846982/tsm-to-ts3-conversion-this-tutorial-only-covers
fetched: 2026-10-28
game: tsm, ts3
tags: conversion, object-creation, cas, mlod, geom
status: community-reported
author: Danjaley
---
# TSM (The Sims Medieval) to TS3 conversion - Danjaley, 2017

Read in a web browser (tumblr answers 403 to plain fetch). Only the TSM-specific steps.

## Where the TSM data is
- `...\Electronic Arts\The Sims Medieval\Game Data\Shared\Packages`: **SASFullBuild1** = base game objects,
  **SASFullBuild2** = base game CAS; Pirates and Nobles: **SASFullBuild_EP1** (all its content). Work on copies.
- In s3pe sort by Tag then Name; many TS3 resources are mixed in. Use `_IMG` resources to identify items, or the
  MLOD with group 0x00000000 ("MLOD Preview" plugin). CAS parts sort by age/gender/type prefix (`amBody`, `afBody`,
  `cuBody`...).

## Objects
- Export the `_IMG` textures (keep `.dds`) and the **MLOD with group 0** (Export to s3asc for Milkshape / s3m2b for
  Blender), then build a normal TS3 object. Overlay-only objects: derive multiplier/specular by desaturating.

## Clothing
- Take the GEOM named with `lod_1` / `lod1_1` (lowercase, no elder/teen/fit/fat/thin/special suffix); if both exist
  you need both (the second often holds a stray piece such as a finger).
- TSM and TS3 bodies are similar; align neck and legs, or import a TS3 nude mesh and delete the TSM body.
- Pitfall: TSM has no separate shoes, so outfits ignore the TS3 UV convention (shoe area holds trouser legs); most TSM
  conversions therefore have shoes baked in (worn barefoot or with a no-feet mod). Skin areas use roughly the right
  UV map.
