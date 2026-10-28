---
title: s4animtools wiki - How do I get rid of the weird snapping in animations? (Basic IK Tutorial)
url: https://github.com/thepancake1/_s4animtools/wiki/How-do-I-get-rid-of-the-weird-snapping-in-animations%3F---Basic-IK-Tutorial
fetched: 2026-10-28
game: ts4
tags: animation, ik, clip, blending
status: community-reported
author: thepancake1
---
# s4animtools: Basic IK tutorial (TS4)

Page last edited 2022-01-30 by thepancake1.

## Key facts
- Problem addressed: Sims "snap" when entering/leaving a custom clip. Fix: add **World IK channels**
  (button "Create World IK Channels"), extend each IK range to the clip end, "Bake IK", re-export.
- Quote: "The forearms and calf bones must be only rotated on the Z axis!" Rotating them on X or Y makes the
  animation look wrong in game (the IK solver assumes hinge joints).
- Animations must start and end in the base pose (e.g. standing) so the IK-driven transition blends;
  a very different start still blends but less fluidly.

## Relevance for TS3
- Same engine lineage: TS3 IK chains on the Sim rig (RIG v4) also solve 2-bone limbs. The Z-only
  hinge rule is TS4-sourced; not verified for TS3. See `topics/ik-and-slots.md`.
- The baking math in s4animtools `ik_baker.py` (https://github.com/thepancake1/_s4animtools): per frame
  `target_bone_world^-1 * chain_end_world`, weight 1 inside the target range, 0 keys just outside.
