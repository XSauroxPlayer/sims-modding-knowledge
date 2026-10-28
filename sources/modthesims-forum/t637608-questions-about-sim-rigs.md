---
title: Questions About Sim Rigs
url: https://modthesims.info/showthread.php?t=637608
fetched: 2026-10-28
game: ts3
tags: animation, rig, slots, ik, world
status: community-reported
author: Slamyy, TheSweetSimmer, SmugTomato
---
# Questions About Sim Rigs (MTS Sims 3 Creation > Miscellaneous, Feb 2020)

Slamyy, TheSweetSimmer, SmugTomato. Synthesis: `topics/rigs.md`, `topics/ik-and-slots.md`.

- ClipTool Blender pose skeleton has hidden bones (L/R breast, belly, belly target slot, back torso target slot)
  and visible export poles, offsets and info bones between the feet.
- TheSweetSimmer: hidden slots are used only for IK targets, effects and other game-side attachments. Pole export
  bones = elbow/knee poles for IK. Offset bones = offsets of the IK targets for arms, legs and root. Info bones = the
  influence of the IK targets: "L_info_1 would be an IK target with the number 0 index for the left arm".
- Breast bones: probably driven by the CAS breast slider (scaling without a dedicated morph) - SmugTomato, a guess.

## Against verified findings
- **Agrees** with the binary analysis in `research/ts3-native-ik.md`: target index N uses `<S>_Info<N+1>`.
