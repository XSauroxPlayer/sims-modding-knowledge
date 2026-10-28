---
title: CLIP format (TS3 0x6B20C4F3, TS4 notes)
summary: binary layout, frame data types, IK table, events, naming and age hashes, tools and pitfalls
status: community-reported
---
# CLIP format

Main sources: `sources/simswiki/0x6b20c4f3.md` (wiki layout), the s3pi-wrappers `ClipResource.cs` parser
(https://github.com/ChaosMageX/s3pi-wrappers), facts verified in game by XSauroxPlayer (marked
`verified-in-game`), and `research/ts3-native-ik.md` for what the engine does with the IK table.

## Layout in one paragraph
Main header with self-relative offsets (clip, IK/slot table, actor name, events, end) -> `_S3Clip_` v2 block
(frame duration 1/30 s, frame count, tracks, indexed floats, anim name, **source file name**) -> per-bone tracks
(FNV32 bone hash, offset, scale, keyed frames, data type) -> IK table (per rig chain: list of `{index, actor 512 B,
slot 512 B}`) -> `=CE=` events v0x103 -> 16-byte end block `0,0,0,1.0`. Details: `sources/simswiki/0x6b20c4f3.md`.

## Frame data
- Rotation 0x214: XYZW quaternion, 12-bit components; wiki: "framework requires +90 degree rotation".
- Translation 0x112: 3 x 10-bit packed in a DWORD. 0x10B / 0x20C = null translation / rotation.
- 0x103: three WORD indices into the indexed-float table. 0x705: pet morph scalar.
- Every value: `int / max * scale + offset`, sign from the per-frame sign-bit WORD.
- Keyed frames can skip indices (sparse keys).

## Naming and lookup
- `a_`, `o_`, `a2a_`, `a2o_`, `x2y_` prefixes; the engine falls back from the age variant (`t2c_...`) to the adult one.
- Instance = FNV64 of the name, top bit cleared for a/o; age variants set the top bit and XOR age masks
  (table in the source page).
- Jazz finds clip actors through the clip's **source file name** + actor (`Assign Actor "<file>.ma"."x"`), see
  `topics/jazz.md`.
- Object clips must start with `o_` (Lyralei, `sources/simblr/110-...jazz...md`).
- TS4 (s4animtools): rig name = actor `x`, unique clip names with a creator prefix and without the actor name
  (`sources/s4animtools-wiki/getting-started-pose-jaw-rig.md`).

- Age masks XORed into the top byte (second byte for the target actor): b 1, p 2, c 3, t 4, h 5, e 6, ad 8, cd 9,
  al A, ac D, cc E, ah 10, ch 11. Plain FNV64 does not give the right instance for non-adult names (wiki, repeated by
  the ModestPixels pack, `sources/modestpixels/knowledge-pack.md`; `community-reported`).
- Actor/slot table: one primary entry per rig IK chain, the IK targets as secondary entries (wiki and ModestPixels
  pack). The chain side agrees with `research/ts3-native-ik.md` (`verified-in-binary`).

## Events
| type | TS3 meaning | payload |
|---|---|---|
| 1 | parent prop to slot | 3 FNV32 hashes (see contradiction below) + blank + 4x4 identity |
| 2 | unparent | hash |
| 3 | sound | 128-byte name |
| 4 | script (SACS) | event id; script gets it via `AddOneShotScriptEventHandler(id, ...)` |
| 5 | effect | 2 DWORD + hash effect, hash actor, hash slot/bone |
| 6 | visibility | float 0..1 |
| 9 | destroy prop | hash of a Jazz `Create Prop` actor |
| 10 | stop effect | hash effect + blank |

- The two unknown DWORDs of event 5: wiki leaves them unknown; Arsil (forum) guessed FNV64; **clips that store
  FNV64(effect name) low/high play their effects in game** (`verified-in-game` by XSauroxPlayer).
  MTS t=541491: brando130 found the DWORDs = FNV64 of the event **name** (`spaJets`, low half in Unknown01); Arsil saw
  clips where they are absent or differ and the effect name sits as FNV32 in `EffectNameHash`. **Unresolved** whether
  EA hashes the event name or the effect name (they may coincide); the effect-name choice works in game.
- ClipTool keeps an EA clip's events when that clip is the export's Base Clip (t=541491).
- **CONTRADICTION (field naming of event 1)**: wiki = (prop actor, object actor, slot on object); s3pi = (ActorNameHash,
  ObjectNameHash, SlotNameHash) which reads as (actor that plays the event, child prop, parent slot). Check an
  EA clip before relying on the order. TheSweetSimmer's tutorial (MTS t=668206) describes ObjectNameHash as "the parent
  of the object" and SlotNameHash as the parent bone/slot, which leans towards the wiki reading; still unverified.
- Parent event usage (t=668206): attaches the prop **origin** to the parent bone/slot; the prop then moves by its own
  `transformBone`/`_rot` track. Transform = 4x4, set elements `00,05,0A,0F` to 1 (identity). One parent event per
  hand-off, the prop snaps at the timecode (seconds), so match it to the Blender constraint switch exactly. Visibility
  event is instant (0/1); fades need a script event.
- Pitfall: if the parent is a Sim slot and the Sim clip is exported too, reset the slot to its default before export,
  or the BOND slot offset is applied twice in game (t=668206).
- TS4 event syntax in s4animtools (frame suffix `f`, Parent `40f,chocolateBar,x,b__Head__`, unparent `0,0`, effect with
  unique name and Stop Effect by name): `sources/s4animtools-wiki/event-tutorial.md`. TS4 adds Reaction, Suppress
  Lipsync, Snap; TS3 has none of these.

## Timing
- TS3 CLIP: 30 fps (wiki; `verified-in-game` by XSauroxPlayer).
- TS2 ANIM: tick 1/800 s, keys baked at 24 fps, key i at i/(n-1) (`verified-in-game` by XSauroxPlayer). TS2 frames from ticks:
  `tick / 800 * 30 + 1`.
- **CONTRADICTION**: Morita's TSM/TS3 -> TS2 tutorial on simblr treats a TS2 frame as 50 ms
  (`sources/simblr/7096-...ts2.md`); the verified finding above is 24 fps baked keys over 1/800 s ticks.

## Tools and pitfalls
- Exported clip check (ModestPixels pack, method advice): reimport onto the target rig and compare the first and last
  pose and the duration before testing in game.
- Foot sliding (ModestPixels pack): measure world speed against the stride. Root translation in the clip plus
  controller movement doubles the travel; neither gives walking in place. Decide which one owns travel.
- s3pe + s3pi-wrappers (ChaosMageX): grid editing of IK table and events. ClipTool / S3PY RigTools (Blender 2.67b)
  does not export IK tables or events; its "Base Clip" option keeps the EA event grid. S3PE can keep IK targets when
  re-importing an edited clip.
- WesHowe AnimTool: "limit is 256" joints.
- TS4 tools (S4S, s4animtools) drop or rebuild IK channels on export; TS4 rules on IK: `topics/ts4-animation.md`.
