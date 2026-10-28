---
title: Emmiting effects in animations
url: https://modthesims.info/showthread.php?t=541491
fetched: 2026-10-28
game: ts3
tags: animation, clip, effects, events, fx, script, rslt
status: community-reported
author: brando130, Arsil
---
# Effects in animations (MTS Modding Discussion, Nov 2014)

brando130, Arsil. Synthesis: `topics/clip-format.md`, `topics/script-modding.md`.

- ClipTool keeps an EA clip's events (s3pe Grid data, e.g. an effect event) when that clip is used as **Base Clip**
  for the export.
- Effect event `Unknown1`/`Unknown2`: in `a2o_bathtub_takeBath_spaJets_bathtub` they are the FNV64 of the
  **EventName** `spaJets` split in halves (`Unknown02` = high 32 bits `0xA3F62C45`, `Unknown01` = low 32 bits
  `0xC3E8A495`) (brando130).
- Arsil: the two fields are not always present and not always FNV64(event name); for `candle_smoke` and
  `eplincensesmoke` the **FNV32 of the effect name** is in `EffectNameHash`.
- The effect's `SlotNameHash` for the bathtub matched a **bone name hash in the effect section of the object's RSLT**
  (`bathtub_rig`, FullBuild0), not the slot name hash (Arsil, unconfirmed).
- Script alternative that worked (brando130): `VisualEffect.Create("ep7BuffSpicyMouthFlame_main")`,
  `ParentTo(Actor, Sim.FXJoints.Head)`, `Start()`, then `PlaySoloAnimation(...)`. Sync is loose: play a setup clip,
  start the effect, then the main clip. EA's Zzz effect uses `Sim.ContainmentSlots.Mouth` instead of an FX joint.
  Effect names can be found in EA code (`BuffTooSpicy.CreateEffectsAndPrepForAnimation`).

## Against verified findings
- Verified in game by XSauroxPlayer: clips that store **FNV64(effect name)** low/high in the two DWORDs play
  their effects. brando130 reads the same DWORD order
  (low first) but says the hashed string is the **event name**. In his example the event name may also be the
  effect's name; **not resolved** - check one EA clip where event name and effect name differ.
