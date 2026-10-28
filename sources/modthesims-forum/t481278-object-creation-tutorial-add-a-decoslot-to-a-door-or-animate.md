---
title: Object Creation - Tutorial - Add a decoslot to a door or animated object
url: https://modthesims.info/showthread.php?t=481278
fetched: 2026-10-28
game: ts3
tags: object-creation, slots, rslt, rig, tsrw, s3pe
status: community-reported
author: BloomsBase (credits CMO)
---
# Add a deco slot to a door / animated object (MTS Tutorials, July 2012)

BloomsBase (credit CMO). Synthesis: `topics/object-creation.md`, `topics/ik-and-slots.md`.

1. Clone a door in TSRW; Slot tab: duplicate `cntm_0`; placement flags small, medium, large, decorative; unique
   name hash (`decoslotdoor`) and **bone hash** (`decoslotdoor_00`); raise Y to 1.75.
2. Open the RIG in s3pe (TSRW s3pe plugin + s3pi wrappers) > RIG editor; add a child joint under the moving joint
   (`_bind_0_doorswing`) named exactly as the slot's bone hash string, so the slot follows the animated part.
3. The new joint's position is **relative to its parent joint**: subtract the parent's offset (e.g. height
   1.75 - 1.116090 = 0.63391; X -0.377234 to cancel the hinge offset). Scale 1 on every axis.
4. Pitfall: X and Z sometimes need swapping depending on how the mesh is oriented.

## Against verified findings
- Consistent with what XSauroxPlayer verified on EA game files: RSLT slots reference a bone by FNV32 hash. That a slot on
  an animated part follows it only via a child joint is the tutorial's claim, not verified independently. The axis-swap
  remark is unexplained (likely Y-up vs object space).
