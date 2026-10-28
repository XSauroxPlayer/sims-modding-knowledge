---
title: Sims_3:0x8EAF13DE (_RIG, skeleton and IK chains)
url: https://simswiki.info/index.php?title=Sims_3:0x8EAF13DE
fetched: 2026-10-28
game: ts3
tags: rig, ik, format, animation
status: community-reported
author: SimsWiki contributors
---
# TS3 _RIG (0x8EAF13DE)

Three historical formats: raw Granny2 (.gr2), Granny2 with a wrapper (first DWORD = 0x8EAF13DE), and since the Create A
Pet demo an **unencrypted EA format** (the one to use; the old ones "should never be used").

## New format (v3/v4)
`DWORD major (3-4)`, `DWORD minor (1-2)`, `DWORD bone count`, per bone: `FLOAT[3] position`, `FLOAT[4] orientation
quaternion`, `FLOAT[3] scale`, `DWORD name length` + ASCII name, `DWORD mirror index` (own index, or the index of the
left/right opposite bone), `DWORD parent index`, `DWORD FNV32 name hash`, `DWORD flags` (usually 0x23; 0x3F on one of a
mirrored pair). Then `DWORD skeleton name length` + name. If major >= 4: `DWORD IK chain count`, per chain `DWORD
length`, `length` bone indices, `InfoNode[11]` bone indices, PoleVector, SlotInfo, SlotOffset, Root bone indices.
Version 3 has no IK data and an empty skeleton name.

## Old wrapper (for reference)
Offsets to IK chains, IK target slots, info nodes, compress nodes (`b__R_Calf__Compress__` style), full bone list.
Chain entry: chain length, pole, chain start, SlotInfoNode, SlotInfoRootNode, SlotOffsetNode, SlotOffsetRootNode,
`InfoNodeFlags` (bits 0-10 = enabled info nodes), InfoNode0..10, links {end bone, start bone}.

## Against verified findings
- 11 info nodes per chain = `<S>_Info1..Info10` plus one extra entry; `Info<N+1>` local Z carries the weight of CLIP
  IK target N (verified in the game binary and in game by XSauroxPlayer, `research/ts3-native-ik.md`). The wiki
  does not say what the info nodes mean.
- auRig chain order (0 L arm, 1 R arm, 2-3 legs, 4 root) comes from XSauroxPlayer's checks on EA clips, not
  from the wiki.
- The mirror index field is what mirrored clips use to swap left/right bones (inference, not verified).
