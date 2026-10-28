---
title: Modding - General - Tutorial - Creating Custom Sims 3 Fully Functional TV Channels
url: https://modthesims.info/showthread.php?t=396117
fetched: 2026-10-28
game: ts3
tags: tuning, stbl, video, tv, fnv64
status: community-reported
author: Odistant
---
# Custom TV channels (MTS Tutorials, 2010, updated 2011; author marks it outdated)

Odistant. The tutorial itself is a PDF attachment (not downloaded); only the thread text was read.
Synthesis: `topics/tuning.md`.

- Blank pie menu entry = missing STBL string: the string id is **FNV64 of `Gameplay/Excel/TV/TVChannel:<Name>`**
  where `<Name>` is the channel name in the XML tuning.
- EA TV videos are `Sims3TV_*` resources in FullBuild1; `eaconv.exe` converts `.video` to `.avi` (VP6 pipeline for
  new videos, audio sync fixed later in the guide).
