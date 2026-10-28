---
title: Objects - Modding Infocenter - The Resource Node (CRES)
url: https://modthesims.info/showthread.php?t=84487
fetched: 2026-10-28
game: ts2
tags: ts2, cres, scenegraph, joints, quaternion, object-creation
status: community-reported
author: Numenor (structure credited to Raquelcesar)
---
# The Resource Node (CRES) (MTS Sims 2 Creation > Tutorials, Modding InfoCenter, Aug 2005)

Numenor (structure credited to Raquelcesar). The PDF attachment was not downloaded. Synthesis: `topics/ts2-formats.md`.

- CRES blocks form a **tree** ("CRES hierarchy"), not a sequence. Root is always a `cResourceNode` (block 0x00);
  each block's Child Nodes list gives its children. Transforms of a node apply to all descendants.
- `cTransformNode` holds translation (unit = **one tile**) and rotation as a quaternion (SimPE also shows axis+angle).
- Game axes (as SimPE shows them): **positive X moves left**, and **Y/Z are swapped** compared to 3D editors.
- Some blocks are joints (e.g. cheap PC `Joint3` = `cddrawer_trans`); animations move joints, and vertices bound to
  that joint in the GMDC follow.
- Scenegraph chain starts at the CRES: shapes, lights and mirrors are listed in its Reference tab but only load if a
  hierarchy block points at them (`cShapeRefNode` for shapes and mirrors, `cLightRefNode` for lights).

## Against verified findings
- XSauroxPlayer's TS2 extractor reads CRES transforms for slot and bone positions. The "X left, Y/Z swapped"
  note is SimPE's display convention and was not re-checked here.
