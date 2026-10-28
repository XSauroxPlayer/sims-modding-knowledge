---
title: The Code Snippet Jar!
url: https://modthesims.info/showthread.php?t=632115
fetched: 2026-10-28
game: ts3
tags: script-modding, snippets, animation, alarms, persistence, routing, interactions
status: community-reported
author: Lyralei, gamefreak130, Battery, zoe22, echoweaver, SimStateDude and others
---
# The Code Snippet Jar (MTS Modding Discussion, sticky, 2019-2022)

Multi-author snippet collection (Lyralei, gamefreak130, Battery, zoe22, echoweaver, SimStateDude...). Only the first
page of the thread was fetched. Synthesis: `topics/script-modding.md`.

- **Test a CLIP without Jazz:** `Actor.PlaySoloAnimation("<clip name>", true)` plays one clip on the Sim
  (EA example `a2o_object_genericSwipe_x`).
- Replacing an EA interaction: assign the new definition to the EA `Singleton` in **OnPreload**, not in
  OnWorldLoadFinished (`WashHands.Singleton = new CustomWashHands.Definition()`).
- Alarm types (gamefreak130): `AlwaysPersisted` survives owner reset and save; `DeleteOnReset` survives save only;
  `NeverPersisted` neither. Global alarms (owner null) are best re-added on world load.
- Background work without blocking the main thread: `Simulator.AddObject(new Task_GenericAction(cb))`;
  one-shot tasks via `OneShotFunctionTask`.
- Persistent static data: `[PersistableStatic]` fields; data across travel via a "ferry" (save on
  `World.OnWorldQuitEventHandler`, restore on load).
- Routing near an object: `Actor.CreateRoute()` + `PlanToPointRadialRange(target.Position, min, max, ...)` with
  `IHasRouteRadius.CarryRouteToObjectRadius`.
- Inventory: override `StacksWith` for stacking; `HandToolAllowUserPickup` for inventory pickup;
  `sim.Inventory.FindAllOfType(typeof(T))`, `lot.CountObjects<T>()`.
- Interaction localisation key: `InteractionDefinitionUtilities.GetInteractionLocalizationKey(type, iop)`.
- Notification styles: kSimTalking, kSystemMessage, kGameMessagePositive/Negative, kDebugAlert, kCustom,
  kCelebrityUpdate.
