---
title: Sims_3:Jazz (Smooth Jazz syntax and semantics)
url: https://simswiki.info/index.php?title=Sims_3:Jazz
fetched: 2026-10-28
game: ts3
tags: animation, jazz, slots, props, priorities
status: contradicted
author: SimsWiki contributors
---
# Sims_3:Jazz - Smooth Jazz language (wiki)

Binary layout: `0x02d5df13.md`. Synthesis: `topics/jazz.md`.

## Concepts
- "Jazz scripts ARE NOT animations": C# starts a state machine, Jazz decides which clips play and when. Even a door
  opening uses Jazz. Names are FNV hashes; a quoted string is hashed, `0x...` is taken as a hash; some EA data hashes a
  hash-formatted string again (prefix `*` reproduces it). Keywords are case-insensitive; C++ comments.
- State machine fields: `Actor`, `Parameter` (optional default), `Properties` (UnilateralActor, PinAllResources,
  BlendMotionAccumulation, HoldAllPoses; values not given), `Priority` (purpose unclear), `Assign Actor
  "<clip source>.ma"."<actor in clip>" as <jazz actor>` (also `0xHASH."actor"`), and "Unknown Value" slots (index 0
  seen 1-5).
- States: `Properties` (Public 0x1, Entry 0x2 "can be set as current without transitions", Exit 0x4, Loop 0x8, OneShot
  0x10, OneShotHold 0x20, Synchronized 0x40, Join 0x80, Explicit 0x100), `Transitions to` (**only named transitions are
  ever followed**), unknown value 0 (default 6).
- Decision graph nodes: Play, Stop, Actor Operation (`SetMirror` = 1, None = 0), Create Prop, Select Random, Select on
  Parameter (switch, **no default case**), Next State (unknown whether evaluation continues after it).

## Play
- `Play <clip> [For actor] { Track Mask <ref>; Actor a Slot s [, n, n]; Actor a Suffix param; Flags ...;
  Priority1/Priority2; Blend In <sec>; ... }`.
- Clip names may use parameter substitution: `"{age1}2{age2}_greet"` -> `a2t_greet`.
- **Age fallback**: clip hashes are based on the adult name; the game first tries the age-specific clip for the
  primary actor's age/species, then the generic (adult) one.
- Track mask = TkMk 0x033260E3 ("unclear if what is being masked is this animation, or all other animations").
- Actor Slot: slot from the actor's RSLT, two unknown numbers default 0; used only once in all EA Jazz.
- Slot Suffix: appends a parameter value to slot names, used for bed side / car or sofa seat.
- Two priorities per Play/Stop; the second's use is unknown.
- Default flags `AtEnd`.

## Priorities (full list)
Low 6000, LowPlus 8000, Normal 10000, NormalPlus 15000, FacialIdle 17500, High 20000, HighPlus 25000, CarryRight 30000,
CarryRightPlus 35000, CarryLeft 40000, CarryLeftPlus 45000, Ultra 50000, UltraPlus 55000, LookAt 60000.

## Play flags as the wiki shows them today (read 2026-10-28)
AtEnd 0x1, LoopAsNeeded 0x2, OverridePriority 0x4, "Mirror OverrideMirror" 0x8, OverrideTiming0/TimingMaster 0x10,
OverrideTiming1/TimingSlave 0x20, TimingIgnored 0x40 ("Shorthand for OverrideTiming0, OverrideTiming1"),
Interruptible 0x60, ForceBlend 0x80, UseTimingPriority 0x100, UseTimingPriorityAsClockMaster 0x200, BaseClipIsSocial
0x400, AdditiveClipIsSocial 0x800, BaseClipIsObjectOnly 0x1000, AdditiveClipIsObjectOnly 0x2000, HoldPose 0x4000,
BlendMotionAccumulation 0x8000.
- **Contradiction with s3pi** (see `topics/jazz.md`): the wiki's own note says TimingIgnored = TimingMaster |
  TimingSlave, which is 0x30 with the wiki values but 0x60 with s3pi's (0x20 | 0x40 = TimingIgnored 0x60). s3pi is
  internally consistent; the wiki table looks shifted by one row from 0x10 up (Mirror and OverrideMirror merged into
  one row). Not verified against EA data.
- The ModestPixels knowledge pack (`sources/modestpixels/knowledge-pack.md`) records the same table as read on 2026-10-27 with fewer rows
  (TimingIgnored 0x40, ForceBlend 0x80, BaseClipIsSocial 0x400, BaseClipIsObjectOnly 0x1000, HoldPose 0x4000,
  BlendMotionAccumulation 0x8000): same values, so it inherits the same contradiction with s3pi.

## Create Prop / Random
- Props: catalog GUID with type 0x139F7591; examples: repair tools, toy xylophone mallets, the Grim Reaper's scythe.
- `Select Random { Flags AvoidRepeats; Weight n { ... } }`: weights relative (1 vs 10 = 1 in 11).
