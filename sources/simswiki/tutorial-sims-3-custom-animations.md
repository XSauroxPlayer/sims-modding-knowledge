---
title: Tutorial:Sims 3 Custom Animations
url: https://simswiki.info/index.php?title=Tutorial:Sims_3_Custom_Animations
fetched: 2026-10-28
game: ts3
tags: animation, clip, jazz, script-modding, objk, s3sa, obsolete
status: community-reported
author: RothN
---
# Custom object animations (simswiki, RothN, category "Obsolete Tutorials")

Marked outdated by the wiki itself (superseded by TS3 Animator / ClipTool and by MTS t642029). Kept for the
resource-level facts. Synthesis: `topics/jazz.md`, `topics/script-modding.md`.

- OBJK: tick **Script** and set it to `Namespace.Class`; if the cloned object was not animated, also tick **Sacs**
  and **Animation** in the OBJK components.
- S3SA: instance = FNV64 of a chosen name (here the class name), group 0.
- CLIP exported to file name `S3_6B20C4F3_00000000_<FNV64(animName)>_<animName>%%+CLIP.animation`; AnimTool's
  "Package To Animation" avoided the "magic required for the Animation Name hash" (author's words: hashing errors
  with the legacy tool).
- AnimTool fields: **Anim Name** (e.g. `a2o_test_x`) and **Source Name** (e.g. `a2o_test.ma`), the latter is what
  Jazz uses in `Assign Actor "<SourceName>"."x" as "x"`.
- C#: `AcquireStateMachine("<machine>"); SetActor("x", Actor); EnterSim("Enter"); AnimateSim("<state>");
  AnimateSim("Exit");` between `StandardEntry()` / `StandardExit()`.
- Milkshape: bones not present in the exported template clip do not animate in game.
