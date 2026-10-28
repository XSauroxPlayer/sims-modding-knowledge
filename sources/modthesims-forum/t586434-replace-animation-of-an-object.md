---
title: Replace animation of an object
url: https://modthesims.info/showthread.php?t=586434
fetched: 2026-10-28
game: ts3
tags: animation, clip, jazz, default-replacement, objk, script
status: community-reported
author: silvian, Lyralei
---
# Replace animation of an object (MTS Modding Discussion, Dec 2016)

silvian, Lyralei. Synthesis: `topics/jazz.md`.

- Default replacement of a CLIP: export the EA CLIP (note type/group/instance), edit in Blender on the right rig,
  re-import into a new package with **identical TGI**. Affects every object using that clip.
- A clone (S3OC/TSRW) keeps the **OBJK script class**, so it plays the same Jazz/CLIPs as the original; cloning
  does not copy the CLIPs, and new CLIPs on the clone are never called.
- To give a clone its own animations: decompile the script (ILSpy), rename the namespace, ship a copy of the Jazz
  script with **new instance** (not overriding EA's) and point its `Play` lines at the new clip names (age prefix as
  in pose making, e.g. `af_...`).
