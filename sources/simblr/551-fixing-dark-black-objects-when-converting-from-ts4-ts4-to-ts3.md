---
title: Fixing dark/black objects when converting from TS4 to TS3
url: https://simblr.cc/ts3/tutorial/551-fixing-dark-black-objects-when-converting-from-ts4-ts4-to-ts3.html
fetched: 2026-10-28
game: ts3, ts4
tags: mesh, conversion, normals
status: community-reported
author: bioniczombie
---
# Dark/black converted objects (TS4 -> TS3)

## Key fact
- Cause: mesh exported from Blender without normals. Fix: tick **"Write Normals"** in the Blender mesh exporter.
  Black objects = missing/zero normals.
