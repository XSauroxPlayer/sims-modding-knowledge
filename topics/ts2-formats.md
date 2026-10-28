---
title: TS2 formats (for TS2 -> TS3 conversion)
summary: TS2 package, SLOT, CRES, BHAV, ANIM and object facts, verified ones restated with their status, plus community sources
status: verified-in-game
---
# TS2 formats

Facts marked `verified-in-game` were tested in game by XSauroxPlayer; `verified-in-binary` facts were checked
byte for byte on EA game files by XSauroxPlayer. Community facts link their source page.

## Verified facts
- Packages: DBPF 1.1, QFS compression, resources keyed by type/group/instance plus a second instance word; when two
  packages hold the same key, the last one loaded wins. (`verified-in-binary`)
- BHAV instruction (format 0x8007): 23 bytes = u16 opcode, u16 true jump, u16 false jump, u8 version, 16 bytes of
  operands. Jump targets 0xFFFD = return true, 0xFFFE = return false, 0xFFFC = error. Opcodes below 0x100 are
  primitives. (`verified-in-binary`)
- ANIM timing: tick = 1/800 s; EA keys are baked at 24 fps, key i at time i/(n-1) of the clip. (`verified-in-game`)
- SLOT resource `0x534C4F54`: 64-byte name, versions 0x46/0x47, 78-byte entries, `u16 type` (0 container,
  1 location, 3 routing, 4 target), x y z always 0 in EA objects, `bone_index` = row of STR# 0x90 (empty rows
  counted). (`verified-in-binary`)
- TS3 targets of a conversion, checked on EA TS3 files: RSLT slot names `RoutingSlot_<i>`, `ContainmentSlot_<i>`,
  `FXJoint_<i>`; slot bone hash = FNV32 of the lowercase rig bone name (4862 of 4883 EA slots match a bone); slot
  matrix = the bone's bind pose in object space; seat containment slots carry flag 0x1. (`verified-in-binary`)
- TS3 shadow LODs 0x10000/0x10001: 8-byte position-only vertices (normalised shorts plus a fourth short 32767),
  decoded as PosOffset + short * PosScale from the MATD chosen by ScaleOffsetIndex. A 28-byte body-style vertex
  crashed the game. (`verified-in-game`)
- TS3 mesh geometry states: state name = FNV32 of the lowercase name (`empty` = C7EE8594). EA hides a part with a
  state that has 0 primitives and 0 vertices; a mesh without that state is drawn whole; the MTST material state is
  not what hides it. (`verified-in-game`)

## Community sources
- `sources/modthesims-forum/t146440-objects-an-introduction-to-slots.md` - Slots 101 (Atavera): slot kinds,
  `S2 = 2` position from CRES with `I9` -> STR# 0x90, `I7` height codes (1 ground ... 11 decorative), slot numbering
  **per kind** in BHAV operands, slot primitives (`0x2A`, `0x2D`, `0x2E`, `0x70`, `0x71`), CRES is a tree (routing
  slot Z relative to the surface node). Agrees with the verified SLOT layout; it misses type 1 (location).
- `sources/modthesims-forum/t84487-objects-modding-infocenter-the-resource-node-cres.md` - CRES is a tree rooted at
  `cResourceNode`; `cTransformNode` translation in tiles, quaternion rotation; SimPE axes X left, Y/Z swapped;
  shapes/lights load only when a `cShapeRefNode`/`cLightRefNode` block references them.
- `sources/gardenofshadows/ts2-to-ts3-object-tsrw.md` - manual TS2 -> TS3 object conversion with TSRW.
- `sources/simblr/7096-converting-animations-from-the-sims-medieval-the-sims-3-to-the-sims-2.md` - the reverse
  direction (TSM/TS3 -> TS2 animation), useful for bone name maps.
- `sources/tumblr/aikea-guinea-pose-tips.md` - TS2 rig has no separate middle-finger bones (check against the TS2
  rig's bone list).
- `sources/simswiki/understanding-the-scenegraph.md` - link storage: CRES->SHPE and GMND->GMDC by TGI, SHPE->GMND
  and SHPE->TXMT by name, TXMT->TXTR twice (`stdMatBaseTextureName` + File List), MMAT `modelName` = CRES name.

## Contradictions and open points
- Morita (simblr 7096) sets TS2 AniMesh length as frames x 50 ms. **Contradicted** for EA data by the verified ANIM
  timing above: EA TS2 ANIMs are baked at 24 fps; 50 ms is that author's exporter setting. (`contradicted`)
- Slots 101 says BHAV slot numbers count per kind; XSauroxPlayer's SLOT reader indexes entries and was not
  re-checked against this rule when reading `Go To Routing Slot` operands. (open)
