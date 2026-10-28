---
title: Nona's Sims - change an object's script class; tuning mods and commodity kinds (2012)
url: https://nonasims.wordpress.com/2012/05/07/tutorial-how-to-change-the-script-class-of-an-object/
fetched: 2026-10-28
game: ts3
tags: script-modding, tuning, itun, objk, object-creation
status: community-reported
author: Nona Mena
---
# Nona Mena: script class (OBJK) and ITUN/commodity kinds

Pages: `2012/05/07/tutorial-how-to-change-the-script-class-of-an-object/`,
https://nonasims.wordpress.com/2012/04/25/tutorial-tuning-mods-and-commodity-kinds/ ,
https://nonasims.wordpress.com/2012/05/11/edit-your-custom-foods-easily-s3sr-objk-resource-scripts-batch-processing-no-s3pe-needed/
and the script-class page above.

## Script class (OBJK)
- An object's behaviour is its script class, stored in the **OBJK** resource, component `Script`, field `String`
  (e.g. `Sims3.Gameplay.Objects.FoodObjects.DriedFoodHigh`). s3pe: right-click OBJK > Edit OBJK.
- **A leading space or any character before `Sims3.` crashes the game when the object is bought.** "All objects in the
  game must have a script class that starts with 'Sims3.'" (her wording, not verified here; MTS sources state the stricter rule that object classes must live under
  `Sims3.Gameplay.Objects`, see `topics/script-modding.md`).
- After changing the class delete `Documents\Electronic Arts\The Sims 3\scriptcache.package`; already placed objects
  may need to be sold and re-bought.
- Changing the class alone is not always enough: slots and footprint must fit the new behaviour (Jynx rabbit-hole
  rugs). Batch editing of many OBJKs is possible with S3SR scripts (third page).

## ITUN and commodity kinds
- ITUN resources (mostly in `GameplayData.package`, also in store content) gate autonomy and user-direction:
  `<Disallow DisallowAutonomous DisallowUserDirected DisallowPlayerSim>`, `<AgeSpecies AgeSpeciesValue="T,Y,A,E">`,
  motive/mood/skill/career thresholds, lot/world/room restrictions, `<Tradeoff>` with `<Time value addRoute>`,
  `<Exit funExit stressExit interruptible>`, `<Output>` list of `<Change type advertised locked actual updateType ...>`
  (`updateType` ImmediateDelta or ContinuousFlow).
- `advertised` drives autonomy scoring, `actual` the real change. The page lists all CommodityKind enum values of
  patch 1.63-1.67 (Bladder = 17774806, Decoration = 18193954, Fatigue = 17774812, ...); updated list on Simlogical.

## Relevance
- See `topics/tuning.md` and `topics/script-modding.md`.
