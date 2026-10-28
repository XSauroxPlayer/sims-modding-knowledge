---
title: Sims 3:HowIMadeAToiletClassWithTuning
url: https://simswiki.info/index.php?title=Sims_3:HowIMadeAToiletClassWithTuning
fetched: 2026-10-28
game: ts3
tags: script, tuning, object-creation, objk
status: community-reported
author: Inge Jones
---
# Toilet with its own class and tuning (Inge Jones, wiki)

Synthesis: `topics/tuning.md`, `topics/script-modding.md`.

## Recipe
- Clone an EA object; if the look is unchanged the package needs only the parts **down to, not including, the VPXY**
  (keep the scenegraph chain through VPXY when the mesh changes; the cloner pulls it in by default).
- Script: S3SA resource with instance = **FNV64 of the DLL name** (`"ToiletInge.dll"`).
- Edit **OBJK** to point to the new script class (subclass of the EA class, here `Toilet`).
- Tuning: copy the EA object's tuning XML from gameplay data and give it instance = **FNV64 of the OBJK script class
  key**; then the values (e.g. break / get dirty on every use) apply to the new class.
- Class pattern: `[assembly: Tunable]`; `[Tunable] private static X.Tuning kXTuning = new X.Tuning();` per component
  (CleanableComponent, EnvironmentMotive, RepairableComponent, Toilet.Tuning), each exposed by overriding the
  matching virtual property (`CleanableTuning`, `EnvironmentTuning`, `RepairableTuning`, `ToiletTuning`); FX names
  via overridden properties (`OverflowFxName` -> `"s30_toiletExpensiveOverflow"`).
- Namespace used: `Sims3.Gameplay.Objects.Plumbing.Mimics` (consistent with the "class must live under `Sims3.`"
  advice in `sources/nonasims/script-class-and-tuning.md`).
