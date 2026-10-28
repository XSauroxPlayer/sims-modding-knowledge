---
title: TS3 object creation and TS2/TS4 -> TS3 object conversion
summary: clone workflow, MLOD groups and shadows, textures and channels, footprint and slots, script class, pitfalls
status: community-reported
---
# Object creation (TS3)

Sources: `sources/gardenofshadows/ts2-to-ts3-object-tsrw.md` (TS2 -> TS3 via TSRW),
`sources/simlogical/object-start-to-finish-and-4-channel.md` (orangemittens pipeline, 4 channels),
`sources/nonasims/script-class-and-tuning.md` (OBJK script class), `sources/simblr/551-...` (black objects),
`sources/simblr/1400-...` and `1401-list-of-prop-names.md` (spawning props), wiki format pages OBJD 0x319E4F1D,
OBJK 0x02DC343F, MLOD/MODL, RSLT 0xD3044521, FTPT 0xD382BF57 (see INDEX; curated when marked so).
Slots and hands: `topics/ik-and-slots.md`.

## Workflow the community uses
1. Clone an EA object with similar behaviour and slots (s3oc or TSRW). The clone keeps OBJD/OBJK/RSLT/FTPT/MODL/MLOD
   structure; edit rather than build from scratch.
2. Replace the mesh (MilkShape + WesHowe plugins, Blender + Cmomoney add-ons, or TSRW `.wso`).
3. Textures: multiplier (greyscale shading), mask/control (one colour per recolour channel), specular, optional overlay.
4. Footprint and slots: TSRW Footprint editor "From Mesh > Calculate"; Blender for editing/adding slots
   (orangemittens part 19).
5. Package with s3pe / TSRW Export To Package.

## Mesh facts
- Cloned High LOD: **group 0 = ground shadow quad, group 1 = object**; keep the order or materials break
  (aikea-guinea). The ground shadow is a textured quad whose **normals are all 0**. Low LOD usually has no shadow group.
- Sun shadows are separate shadow LODs (TSRW "Generate Sunshadow"). Verified in game by the project author: shadow
  LODs 0x10000/0x10001 use 8-byte position-only vertices (shorts normalised with the MATD PosOffset/PosScale); a
  28-byte body-style vertex format crashed the game. The ground shadow quad inside the main LOD is a different thing
  and was not compared.
- Black object in game = mesh exported without normals ("Write Normals" in the Blender exporter).
- TSRW import of a mesh with more groups than the clone fails ("groupcount does not match"); merge groups and atlas
  the textures.

## Textures and channels
- Mask: channels 1-3 = R, G, B; channel 4 = **mask alpha** (orangemittens). DXT5 for masks with alpha, multiplier and
  specular; DXT1 for a mask without alpha (aikea-guinea).
- Specular with black alpha lets the pattern's own specular show through.
- Texture Tweaker 3 can upgrade a 3-channel EA clone to 4 channels; the mask still needs the 4th region + alpha.

## Script class and behaviour
- OBJK component `Script` holds the class (e.g. `Sims3.Gameplay.Objects.FoodObjects.DriedFoodHigh`). A stray
  character before `Sims3.` crashes the game on purchase. Delete `scriptcache.package` after changes; re-buy placed
  objects.
- Changing behaviour often also needs matching slots and footprint (rabbit-hole rugs).
- Props that are not in Buy mode can be spawned by name with NRaas DebugEnabler "Create Object" (prop list in simblr
  1401) to check they resolve.

## TS2 -> TS3 specifics
- TS2 GMDC exported to OBJ via SimPE, texture as PNG -> DDS; one TS2 texture becomes the TS3 overlay, a greyscale
  multiplier is made by hand. TS2 multi-mesh objects need merging into the clone's group count.
- A converter that writes these resources directly should match the MLOD group order, ground shadow normals and
  texture formats above; check them first when an object looks wrong. Verified TS2 facts: `topics/ts2-formats.md`.

## Slots on objects (forum)
- Slotless object: add RSLT container entries (FNV32 name) that reference a `_RIG` joint by FNV32 of its plain-text
  name; copy the joint naming scheme from an EA end/coffee table (MTS t=427576). Easier: clone an object that has
  slots and swap the mesh.
- Slot on an animated part (door): add a child joint under the moving joint, named as the slot's bone string; its
  position is relative to the parent joint (subtract the parent offset); X/Z may need swapping (t=481278).
- TS2 side (SLOT kinds, I7 height codes, per-kind slot numbering, CRES transforms): `sources/modthesims-forum/t146440-objects-an-introduction-to-slots.md`, `topics/ts2-formats.md`.

## Camera fade
- MODL `FadeType` (0 none, 1-2 subtle, 3 strong/vanishing, other values act like 0) and `CustomFadeDistance` make
  walk-in objects fade near the camera (MTS t=548283, observed values only).
