---
title: Sims_4:0x8EAF13DE (_RIG) and Sims_4:RCOL
url: https://simswiki.info/index.php?title=Sims_4:0x8EAF13DE
fetched: 2026-10-28
game: ts4
tags: rig, ik, format, rcol, scenegraph
status: contradicted
author: SimsWiki contributors
---
# TS4 _RIG and RCOL pages (compared with the TS3 pages)

Also read: `https://simswiki.info/index.php?title=Sims_4:RCOL`. The TS4 pages `Sims_4:0x6B20C4F3` (CLIP) and
`Sims_4:0x02D5DF13` (Jazz) return HTTP 404 (no page under that title).

## _RIG (same type id 0x8EAF13DE as TS3)
- Same bone record as TS3 (position, quaternion, scale, name, mirror index, parent, FNV32 hash, flags 0x23/0x3F).
- Version gates differ from the TS3 page:
  - skeleton name: present "if major >= 4 OR from The Sims 3";
  - IK chains: present "if major >= 4 OR from The Sims 4", and inside a chain `InfoNode[11]` and `SlotInfo` are
    present only if major >= 4. So a TS4 v3 rig has IK chains with bones, pole, slotOffset and root only.
- **Contradiction (minor) with `sources/simswiki/0x8eaf13de.md`**: the TS3 page says version 3 has no IK data and an
  empty skeleton name; the TS4 page implies TS3 rigs always carry the skeleton-name field. Both agree that a TS3 v4 rig
  has the full chain record. Not resolved here; check a real v3 TS3 rig before relying on either.

## RCOL
- Header, TGI tables, 1-based chunk references with the 0x0/0x1/0x2/0x3 high-nibble kinds and the resource type list
  are identical to the TS3 page (`sources/simswiki/rcol.md`); the TS4 list omits S_SM, RSLT and FTPT.
