---
title: Simlogical - How to make an ITUN for a custom interaction (Nona Mena)
url: http://www.simlogical.com/ContentUploadsRemote/uploads/1600/
fetched: 2026-10-28
game: ts3
tags: tuning, itun, script-modding, interactions
status: community-reported
author: Nona Mena
---
# ITUN for a custom interaction (Nona Mena)

## Key facts
- Start from an existing EA ITUN in `GameplayData.package` with similar behaviour (Breastfeed used
  `GiveBottle_Sim`), copy it into the mod package.
- New instance = FNV64 of a unique name; EA convention `InteractionName_TargetObjectName` (e.g. `NonaBreastFeed_Sim`).
- Edit in the XML: `Interaction name`, `Object name`, `CodeVersion name`, `Tradeoff name`. Nested classes use `+`:
  `Sims3.Gameplay.ActorSystems.Children.GiveBottle+Definition` (the Definition class nested in the interaction class).
- `<Output>` holds the motive/skill/commodity changes and advertisement values; see Simlogical "ITUN Modding
  Discussion" and the Commodity Kinds list (`sources/nonasims/script-class-and-tuning.md`).
- Other gates in the same file: AgeSpecies, SkillThreshold, MoodThreshold, etc.

## Relevance
- For script interactions, an ITUN keyed on the interaction's `+Definition` class is how autonomy,
  ages and advertised commodities are tuned without code. See `topics/tuning.md`.
