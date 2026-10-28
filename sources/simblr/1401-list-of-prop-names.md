---
title: List of prop names (Lyralei)
url: https://simblr.cc/ts3/tutorial/1401-list-of-prop-names.html
fetched: 2026-10-28
game: ts3
tags: props, script, debug
status: community-reported
author: Lyralei
---
# Lyralei: list of prop names for NRaas "Create Object" (TS3)

2023-11-12. Companion to `1400-how-to-create-objects-with-nraas.md`.

## Key facts
- Entry format: `name,pack,Full.Class.Name` (class optional), typed into NRaas DebugEnabler > Options > Create Object.
  Examples: `CoffeeCup`; `LoveLetter,EP8,Sims3.Gameplay.Core.LoveLetter` (looks like a bill);
  `glassParty,EP3,Sims3.Gameplay.Objects.CookingObjects.Glass` (empty); `glassRoundPool,EP10,...Glass`;
  `BowlSnack,EP6,Sims3.Gameplay.Objects.Miscellaneous.SnackBowl`; `Package,BaseGame,Sims3.Gameplay.Objects.Misc.AttractionGift`;
  `suitcaseVintage,EP9`.
- Names come from EA source code and packages, "all tested" per the author. They are EA prop instance names
  (the kind passed to EA's create-object-by-name helpers).
- Useful when a TS2 prop must be mapped to an existing TS3 prop object.
