---
title: Tutorials:Modifying a TS3 Mesh
url: https://simswiki.info/index.php?title=Tutorials:Modifying_a_TS3_Mesh
fetched: 2026-10-28
game: ts3
tags: mesh, geom, cas, milkshape, history
status: community-reported
author: WesHowe
---
# Modifying a TS3 Mesh (WesHowe, early 2009, historical)

Old Postal + MilkShape Q-Mesh workflow on the adult Aviator sunglasses. Superseded by s3pe/TSRW/Blender tools, but
the identifiers are useful.

- CAS mesh = GEOM, type **0x015A1849**; the example group 0x005DC5FC, instance 0x00000000D826640E
  (`afAccessoryGlassesAviator`). "Export to Wes" in Postal gathers the GEOM, two DDS images and the Skin
  Controller (bone data) into a package.
- Override = same TGI in a Mods package. The importer needs the skin controller next to the `.simgeom` file
  (extension `.skcon`) or it falls back to default bone values.
- MilkShape pitfall: turn **Autosmooth off** before importing TS3 meshes.
