---
title: Triggering the right animation with RequestState
url: https://modthesims.info/showthread.php?t=604851
fetched: 2026-10-28
game: ts3
tags: animation, jazz, script, clip-naming
status: community-reported
author: Armise, Lyralei, PuddingFace
---
# Triggering an EA animation with RequestState (MTS Modding Discussion, Dec 2017-Jan 2018)

Armise, Lyralei, PuddingFace. Beginner thread. Synthesis: `topics/jazz.md`.

- `RequestState` fails (Sim exits the interaction) when the state machine has no Jazz script that knows the state:
  a CLIP cannot be played by name from C# through a state machine without Jazz.
- To reuse a Sim-Sim clip on an object: re-export it in Blender under an `a2o_` name, optionally author an object
  clip, write a Jazz script using both, and a C# interaction that drives the Jazz.
- Clip name prefixes: `a2a` adult-to-adult, `c2a` child-to-adult, `a2o` adult-to-object (e.g.
  `a2a_magicWand_castSpellSolo_highSkill_success_x`). Clips live in the FullBuild packages.
- Example mods with their own Jazz: PuddingFace's pinch cheek, Einrei's vampire, Sauzaer's vampire powers.
