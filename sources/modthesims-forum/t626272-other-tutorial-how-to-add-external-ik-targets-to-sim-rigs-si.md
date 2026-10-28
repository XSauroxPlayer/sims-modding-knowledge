---
title: Tutorial - How to add External IK targets to Sim rigs (simplified)
url: https://modthesims.info/showthread.php?t=626272
fetched: 2026-10-28
game: ts3
tags: animation, ik, blender, rig, cliptool
status: community-reported
author: TheSweetSimmer
---
# External IK targets on Sim rigs in Blender (MTS Tutorials, April 2019, marked "Outdated")

TheSweetSimmer. Authoring aid only: Blender IK empties so hands/feet stay put while animating; nothing here is
exported as game IK. Synthesis: `topics/ik-and-slots.md`.

- Select a hand/foot bone > Pose > Inverse Kinematics > Add IK to Bone > "To New Empty Object".
- Set the IK constraint **chain length 3** (hand > forearm > upper arm); 0 drags the whole body.
- Name empties per rig and side (e.g. `af_L_HandIKTarget`).
- Not to be confused with the game's CLIP IK targets (s3pe IK target entries + Info/slotOffset tracks), see
  t668470 and t629522.
