---
title: How do you add Slots to an Object that dosent have any?
url: https://modthesims.info/showthread.php?t=427576
fetched: 2026-10-28
game: ts3
tags: object-creation, slots, rslt, rig
status: community-reported
author: Raven Shadow, orangemittens
---
# Adding slots to a slotless object (MTS Modding Discussion, Dec 2010)

Raven Shadow, orangemittens. Synthesis: `topics/object-creation.md`, `topics/ik-and-slots.md`.

- TSRW cannot add slots to an object that has none; easiest is to clone an object that has slots and swap the mesh.
- Manual way: add container slots to the **RSLT**; each entry has an FNV32-hashed name and refers to a joint by the
  **FNV32 hash of a `_RIG` joint name** (needed if the slot must move with the object part). Joint names in the RIG
  are plain text and follow an EA naming scheme: copy it from an existing object (end table / coffee table).
- Add the RIG joints at the slot's XYZ, then matching RSLT entries with hashed names (s3pe FNV32 tool).

## Against verified findings
- Agrees with what XSauroxPlayer verified on EA game files: RSLT bone hash = FNV32 of the lowercase joint name.
