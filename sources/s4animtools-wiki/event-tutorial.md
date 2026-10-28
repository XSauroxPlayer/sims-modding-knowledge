---
title: s4animtools wiki - How do I add animation events? (Event Tutorial)
url: https://github.com/thepancake1/_s4animtools/wiki/How-do-I-add-animation-events%3F-Event-Tutorial
fetched: 2026-10-28
game: ts4
tags: animation, clip, events, fx, sound, props
status: community-reported
author: thepancake1
---
# s4animtools: CLIP event tutorial (TS4)

Author thepancake1, page last edited 2023-01-16. TS4 Blender add-on; the event model is the same family as
TS3 CLIP events (see `topics/clip-format.md`), so the semantics transfer, the binary layout does not.

## Key facts
- Every event's first parameter is the frame/time. Time is in seconds unless suffixed `f` for frames;
  `1` == `30f` (TS4 clips run at 30 fps, same as TS3).
- Actor-hash parameters accept plain names; the tool FNV-hashes them.
- **Parent**: `frame, child actor, parent actor, parent bone`, e.g. `40f,chocolateBar,x,b__Head__`
  (`x` = the Sim actor in EA clips). **Unparent** = same event with `0,0` for parent actor and bone.
- **Sound**: `frame, sound name` (object sounds or Sim voices).
- **Script** (xevt): `frame, script id`; triggers game code at an exact frame.
- **Snap**: undocumented ("way too complicated").
- **Reaction**: `frame, reaction ASM name`; plays on listener Sims; the reaction ASM needs a private state
  unless overridden. (TS4-only.)
- **Play Effect**: `frame, VFX name, actor, bone, 0, 0, unique VFX name`. The two zeros are unknown
  fields kept for later packs. The unique name is what Stop Effect refers to (e.g. confetti1..3).
- **Stop Effect**: `frame, unique VFX name, 0, 0`.
- **Suppress Lipsync**: `frame, duration` - lets the jaw be animated for that span.
- **Visibility**: `frame, actor, visibility`.
- **Focus Compatibility**: unknown.

## Relevance for TS3
- TS3 CLIP event 5 (effect) and 10 (stop effect) also pair by name hash; TS3 has no lipsync/reaction events
  (wiki event list: 1,2,3,4,5,6,9,10). Treat TS4-only types as not portable.
