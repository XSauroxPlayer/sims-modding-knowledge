---
title: "TESTERS WANTED: S3 RIG Maker (v1.0)"
url: https://modthesims.info/showthread.php?t=401882
fetched: 2026-10-28
game: ts3
tags: rig, granny, tools, history
status: community-reported
author: ChaosMageX
---
# S3 RIG Maker v1.0 (MTS Meshing, May 2010)

ChaosMageX. Historical: the 2010 granny rig editor. Synthesis: `topics/rigs.md`.

- Early TS3 rigs were Granny2 `.gr2` ("grannyrig") files; the tool read them with `granny2.dll` (from the Expotron
  3ds Max plugin) and wrote them with CAW's `CSHostWrap.dll`. A "Z is up" boolean changes the written transforms.
- Bone position = bottom row of the 4x4 transform; the author's quaternion/matrix conversion was known to be wrong,
  advice was to set only positions and leave rotation identity.
- No validation of duplicate bone names or parent indices.
- Today obsolete: use the unencrypted EA `_RIG` v3/v4 format (simswiki `0x8eaf13de`, `topics/rigs.md`).
