---
title: s4animtools wiki - pose/animation export, jaw animation, rig export (3 pages)
url: https://github.com/thepancake1/_s4animtools/wiki/How-do-I-make-a-pose-or-animation%3F
fetched: 2026-10-28
game: ts4
tags: animation, clip, rig, naming
status: community-reported
author: thepancake1
---
# s4animtools: making a clip, jaw, exporting rigs (TS4)

Pages: `How-do-I-make-a-pose-or-animation?` (2024-04-28), `How-can-I-animate-the-mouth-jaw-bone?`
(2022-02-14), `How-do-I-export-rigs?` (2022-02-14), plus `How-do-I-make-a-pose?--Getting-started`.
Other page URLs:
- https://github.com/thepancake1/_s4animtools/wiki/How-can-I-animate-the-mouth-jaw-bone%3F-For-Alpha-3-and-above.-Enabling-jaw-movement-tutorial
- https://github.com/thepancake1/_s4animtools/wiki/How-do-I-export-rigs%3F-For-Alpha-3-and-above.-Exporting-Rig-Tutorial
- https://github.com/thepancake1/_s4animtools/wiki/How-do-I-make-a-pose%3F--Getting-started-with-s4animtools

## Key facts
- Panel toggles: "Is Sims 4 Actor" + "Is Enabled for Animation" on the base rig (not the control rig).
- **Rig name = actor name** the clip plays on; EA Sim clips use actor `x`.
- 30 fps: a 5 s pose = 150 frames.
- Clip name must be unique, creator-prefixed (`a_thepancake1_wave`); do **not** include the actor name,
  the exporter appends the rig name to the clip name.
- Jaw: the jaw is normally owned by lipsync; enable "Allow Jaw Animation for Entire Animation" (or use
  Suppress Lipsync events, see event-tutorial.md) or jaw keys are ignored.
- Object rigs: name the object (creator prefix) exactly as the actor used in the animation, "Export Rig",
  then batch-import in Sims 4 Studio.
- Test tool mentioned: Andrew's Pose Player.

## Relevance for TS3
- TS3 also binds clips to actor names (CLIP actor table, Jazz `Actor`), and TS3 clip name prefixes encode
  age/species (`a_`, `o_`, `a2o_`...; see topics/clip-format.md). Naming rules differ in detail.
