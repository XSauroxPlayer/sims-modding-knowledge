---
title: Modding - General - Tutorial - Creating S3 Custom Poses with Milkshape or Blender
url: https://modthesims.info/showthread.php?t=438716
fetched: 2026-10-28
game: ts3
tags: animation, poses, clip, clip-naming, milkshape, smd, cliptool
status: community-reported
author: MTS tutorial author (credits WesHowe, cmomoney, Atavera, mesher; see the thread)
---
# Custom poses with Milkshape or Blender (MTS Tutorials, April 2011, updated 2012)

Author credits WesHowe, cmomoney, Atavera, mesher. Blender users are redirected to Sims3 ClipTool
(`sources/sims3cliptool/cliptool-site.md`). Synthesis: `topics/clip-format.md`.

- Template: in FullBuild0 export an `a_xevt_701`/`702` CLIP with s3pe **Export and rename**, giving the new name.
- **Name must start with `a_`** (or the age prefix of the rig): otherwise "the tool hash will not be correct" and
  the pose does not play. Use a unique creator-prefixed name to avoid instance collisions.
- Old pipeline: AnimTool v0.5 (WesHowe) CLIP -> SMD with a rigfile.txt, pose in Milkshape 1.8.5, SMD -> CLIP,
  import into a new package. Several CLIPs can share one package. Played with cmomoney's Pose Player.
- Milkshape: joints that light **red** (e.g. `b_R_Right_Bicep`-style helper bones) must not be rotated; a slight
  rotation of the wrist bone fixes creased wrists. Milkshape cannot do toddler/pet poses; ClipTool can.

## Against verified findings
- Agrees with the ClipTool rule that the clip name's age prefix matters (`topics/rigs.md`); the "hash" is the
  CLIP instance derived from the name (s3pe Export and rename), not verified further here.
