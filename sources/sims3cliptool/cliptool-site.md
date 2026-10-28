---
title: Sims 3 Clip Tool for Blender (S3PY Animation Tools) - site and pose tutorials
url: https://sims3cliptool.wordpress.com/
fetched: 2026-10-28
game: ts3
tags: animation, clip, tools, blender, props, rigs
status: community-reported
author: "A" (rigs, plugin) and orangemittens (tutorials)
---
# Sims 3 ClipTool (S3PY Animation Tools) for Blender

Pages read: About (home), `instructions/`, `tutorials/completeposetutorial/`, `tutorials/couplesposetutorial/`,
`tutorials/multiplerigpose/`, `tutorials/poseoutfittutorial/`, `tutorials/poseproptutoria/` (all under
https://sims3cliptool.wordpress.com/). Author "A" (rigs, plugin) and orangemittens (tutorials). Mostly beginner
posing walkthroughs; the useful facts are below.

## Key facts
- Plugin `io_s3py_animation-1.60.zip`, **Blender 2.67b required** (later Blender versions break it). Features: load
  and save CLIPs, a .blend per age/species (afRig, puRig toddler, buRig baby added in 1.55a, `multi-rigs/a2a_soc.blend`
  for two-Sim work), fat/fit/thin/pregnant morph sliders (1.54), load cloned objects as props or for object
  animations, load cloned CAS parts.
- ClipTool rigs and WesHowe AnimTool rigs are not interchangeable. 1.52 accepts CLIPs made in MilkShape.
- Changelog hints: 1.52 "Fixed bone assignments when loading certain props such as beds and doors"; 1.60 loads extra
  BGEO morphs beyond fat/fit/thin/special.
- Export: key everything with LocRot (`a`, `i`, LocRot) or nothing is saved; File > Export > Sims 3 Animation
  (.animation). The clip name **must** have an age prefix (`a_`, `p_` toddler, `c_`...), otherwise export errors or the
  pose "will explode in the game". The exporter shows the name with a hash in front; do not edit it.
- Packaging: s3pe New > Resource > Import from file (.animation), accept the default key, save. Test with Cmo's Pose
  Player by typing the clip name.
- Props: clone with S3OC (Normal objects; modular items such as counters, fences, fireplaces from their own menus),
  then RigTools menu > Load Prop. Objects with several groups (beds): move them by grabbing the object rig.
  Reported issues: props imported lying on their back (wheelchair, guitar) - users rotate by hand; only bones shown =
  outdated ClipTool for the Blender version.
- Two Sims: open `a2a_soc.blend` (or File > Append a second rig), pose both, key and export each rig separately into
  its own package.

## Relevance
- The age-prefix rule matches the CLIP naming
  and age hashing on the wiki (see `topics/clip-format.md`).
- No IK table or event export (also reported on MTS t=629522: re-exported clips lose their IK targets).
