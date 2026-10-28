---
title: Sims 3 Animator
url: https://modthesims.info/showthread.php?t=420327
fetched: 2026-10-28
game: ts3
tags: animation, clip, jazz, tools, history, smd
status: community-reported
author: MTS thread participants (see the thread)
---
# TS3 Animator 4 with Jazz editor (MTS Modding Discussion, 2010-2011)

Historical tool thread (marked obsolete by the author). Synthesis: `topics/jazz.md`, `topics/clip-format.md`.

- Converted CLIPs via SMD and wrote packages (merging the `_KEY` name map); needed `granny2.dll`.
- Tip that still applies to any re-export: round-tripping an EA clip through an intermediate format drops
  undocumented extra frame data EA left in the clip.
- Graphical Jazz editor saved its own `.sacs` source and could not reopen compiled Jazz (SmoothJazz recommended).
- Jazz semantics stated in the editor notes: a Choice under a **Random** node carries a weight 0.0-1.0 (default
  1.0); a Choice under **Select On Parameter** carries the parameter value that selects it; only the Animation
  node's Track Mask may be blank.
- RIG exporter tested, RSLT exporter not.
