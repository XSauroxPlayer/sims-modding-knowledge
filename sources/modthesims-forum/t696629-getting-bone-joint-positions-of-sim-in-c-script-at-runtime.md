---
title: Getting Bone/Joint positions of Sim in C# script at runtime
url: https://modthesims.info/showthread.php?t=696629
fetched: 2026-10-28
game: ts3
tags: script-modding, rig, joints, camera, open-question
status: community-reported
author: MTS thread participants (see the thread)
---
# Bone positions from script (MTS Modding Discussion, May 2026)

Open question, **no answer** at fetch time: no public managed API was found to read a Sim's live head/bone transform
(the asker looked at `LookAtManager`, `Sim.FXJoints`, ScriptCore animation handles; `CameraController` can only use the
Sim's logical position and forward). Unresolved; native code (Ghidra) suggested by the asker as the fallback.
