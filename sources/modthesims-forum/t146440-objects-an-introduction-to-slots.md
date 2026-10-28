---
title: Objects - An introduction to Slots
url: https://modthesims.info/showthread.php?t=146440
fetched: 2026-10-28
game: ts2
tags: ts2, slots, slot-resource, cres, bhav, object-creation, routing
status: community-reported
author: Atavera (article); Numenor and others (Q&A)
---
# Slots 101 (MTS Sims 2 Creation > Tutorials, Modding InfoCenter, April 2006)

Atavera (article), Numenor and others (Q&A). The attached PDF was not downloaded. Synthesis: `topics/ts2-formats.md`.

## Slot kinds
- **Routing** slots: where a Sim walks to (facing, many routing flags). **Container** slots: hold objects, FX, Sims
  (chair/bed). **Target** slots: positions used by animations (e.g. sink knobs), can hold FX.
- BHAV slot numbers are counted **per kind**, not by entry index: entries Container, Target, Container, Routing ->
  container 0, target 0, container 1, routing 0.

## SLOT resource fields (SimPE names)
- `S2` = position source: 0 = use F1/F2/F3 offsets directly; **2 = take the offset from the Resource Node (CRES)**,
  the normal case. Then `I9` indexes Text List `0x90`; that string names the `cTransformNode` block in the CRES
  (must equal its `cObjectGraphNode` name).
- Container: `I6` max size (always 0 in practice), `I7` height type = the placement values of Init BHAVs:
  1 ground, 2 low table, 3 table, 4 on counter, 5 non-standard (on Sims), 6 hand, 7 sitting, 8 end table, 9 in
  counter, 10 under counter, 11 decorative. I7 does not move the slot; it tells Sims which put/get animation height
  applies.
- To move a slot, edit the **CRES transform Translation** (Hierarchy tab), not the SLOT file.

## Primitives using slots
- Container: Snap Into `0x71`, Effect Start/Stop `0x70`, Create New Object Instance `0x2A`, Snap `0x2E`
  (container -> routing, e.g. out of bed). Routing: Go To Routing Slot `0x2D`, Snap `0x2E`. Target: mostly used by
  ANIM resources; Effect Start/Stop `0x70`.

## Q&A notes
- CRES is a tree: a table's routing slots show Z -0.8 because they hang under the +0.8 surface node, so their world
  Z is 0. Staircase top routing slots have Z 3.
- Put/get animations exist per standard height; a nonstandard seat height misplaces sitting Sims.
- Items near a large bounding (clickable) mesh can become unpickable.

## Against verified findings
- SLOT layout verified on EA game files by XSauroxPlayer (`verified-in-binary`): resource `0x534C4F54`,
  78-byte entries, `u16 type` (0 container, 1 location, 3 routing, 4 target - a fourth kind, **location**, that the
  article does not list), x y z always 0 in the objects read, `bone_index` = row of STR# 0x90 (empty rows counted).
  Agrees with "S2 = 2, I9 indexes 0x90" (SimPE's I9 = `bone_index`, I7 = `height`: the Love Tub's seats use 7 for
  sitting and 5 on Sims, matching the table above).
- The per-kind numbering rule above matters when reading `0x2D` (Go To Routing Slot) operands; XSauroxPlayer's
  parser indexes entries and was not re-checked against this rule.
