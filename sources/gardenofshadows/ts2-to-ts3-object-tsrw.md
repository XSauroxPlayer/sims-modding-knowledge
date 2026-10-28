---
title: Garden of Shadows - Converting an object from TS2 for use in TS3 using TSRW (aikea-guinea, 2011)
url: http://gardenofshadows.org.uk/gardenofshadows/index.php?topic=22146.0
fetched: 2026-10-28
game: ts2, ts3
tags: object-creation, conversion, mesh, textures, shadows, tools
status: community-reported
author: aikea-guinea
---
# TS2 -> TS3 object conversion with TSRW (aikea-guinea, March 2011)

Forum tutorial (public, no login) converting a TS2 magazine into a TS3 object: SimPE export, TSR Workshop clone,
MilkShape mesh work, Photoshop textures. Page 1 of the thread read (posts #1-#6); page 2 (`topic=22146.15`) not read.

## Procedure (key facts)
- TS2 side: SimPE exports the texture (PNG) and the GMDC as Wavefront OBJ.
- TSRW: clone a simple EA object (the author uses an Ivy Ball Topiary), export the High and Low LOD as `.wso`
  (TSRW object, keeps bone/joint info).
- MilkShape: the cloned High LOD has **group 0 = ground shadow quad, group 1 = object**. "Don't change the order of the
  groups, or you'll end up with some interesting material issues in the game." Import the TS2 OBJ, delete the clone's
  group 1, rename the TS2 group to `Group 1`, then Joints > Select Unassigned > Assign.
- Ground shadow: a flat quad with a shadow texture (texture-based, distinct from the mesh sun shadow). Move its UVs to
  the wanted shadow shape, resize the quad around the object, then set **all its normals to 0** (Vertex > Extended
  Manual Edit) so it renders black/correct. Raise the object mesh if the shadow pokes through.
- Low LOD usually has no shadow group: delete group 0, rename group 1 to group 0, decimate (DirectX Mesh Tool); the
  decimation drops joint assignments, re-import the `.wso` skeleton and reassign.
- Textures (CASTable object): multiplier = greyscale shading, 50% grey base (DXT5); overlay = original TS2 texture,
  PNG -> DXT5; mask/control = solid 255 red / 255 green per recolor channel, DXT1 no alpha; specular = brightened
  multiplier with **black alpha** so the game lays the pattern's specular over it (DXT5).
- TSRW assembly: import High/Low `.wso`, Generate Sunshadow (Shadow High and Shadow Low, "Low Detail"), set overlay,
  for the CASTable preset make the overlay empty and import mask/multiplier/specular; pattern tiling 1,1;
  Slots > Footprint > From Mesh > Calculate (gives off-grid placement and route blocking); Edit > Project Contents >
  Export To Package.
- Pitfall (post #4-#5): "groupcount does not match. 3 in file, expected 2" when a TS2 object has two meshes with two
  textures; fix = merge into one group and remap both parts onto one atlas texture.

## Relevance
- A converter that writes MLOD/MODL directly should match the group order (shadow quad first), the zero normals on
  the ground shadow quad and the texture roles described here.
- Not verified independently; TSRW-specific steps (wso, sunshadow generator) have no direct equivalent outside TSRW.
