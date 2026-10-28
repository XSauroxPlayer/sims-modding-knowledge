---
title: Other - TS4 to TS3 Animation Conversion Tutorial
url: https://modthesims.info/showthread.php?t=664843
fetched: 2026-10-28
game: ts3, ts4
tags: animation, clip, ts4-to-ts3, retarget, blender, cliptool, s4studio, rigs, toddler, child
status: community-reported
author: FloTheory
---
# TS4 to TS3 animation conversion (MTS Tutorials, FloTheory, Feb 2022)

Screenshot tutorial; text read only. Synthesis: `topics/ts4-animation.md`, `topics/clip-format.md`.

- Pipeline: Sims 4 Studio exports an EA (or custom) TS4 clip as `.blend` (Clip Pack > Animation > EA Clip; pick the
  **age**, gender does not matter). Blender **2.79** + TS3 ClipTool.
- Retarget: open the community rig `RigBase ts4 to ts3_FACE_V2.blend` (a TS4 rig driving a TS3 `AfRig`), Append the
  TS4 Action, Set Action on the TS4 rig, then **bake by keying the TS3 rig** (select all, `I`) and export
  "Sims 3 animation" with the age prefix (`a_` adult).
- Stutter fix: set the keys' interpolation to **Auto-Clamped**. Eye animation often breaks in TS4->TS3 conversion
  (separate video fix).
- Adult -> child/toddler: copy keyframes from `AmRig/AfRig`, append `CuRig` (child) or `PuRig` (toddler), key
  LocRot, paste keyframes, delete the adult rig, export with prefix `c_` (child) or `p_` (toddler). Works because the
  rigs share bone names; proportions are not adjusted.
- Custom TS4 clips: export the CLIP to a package with S4PE, open it as a project in S4S, export `.blend`.
- Reported failure: a clip exported this way loaded on a TS3 rig as an "empty" T-pose (unanswered, 2024).

## Against verified findings
- Pasting adult keys onto child/toddler rigs keeps adult translations; not compared with a per-age retarget.
