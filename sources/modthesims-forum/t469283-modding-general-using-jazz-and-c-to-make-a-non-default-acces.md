---
title: Using JAZZ and C# to make a non-default accessory for an object
url: https://modthesims.info/showthread.php?t=469283
fetched: 2026-10-28
game: ts3
tags: jazz, script, props, clip, itun, tuning, object-creation
status: community-reported
author: Leefish
---
# Non-default prop for an object via Jazz + C# (Leefish, MTS Tutorials, 2012)

Medieval fireplace that lights with a taper instead of the EA gas lighter, without replacing the lighter globally.
Synthesis: `topics/jazz.md`, `topics/script-modding.md`, `topics/tuning.md`.

## Steps
1. Clone an EA fireplace (routing slots and rig already right for the animations).
2. Script: `namespace Sims3.Gameplay.Objects.Fireplaces.Mimics.LeeFishMod`, `class MedievalFireplace : FireplaceCheap`,
   `[Tunable] static Fireplace.Tuning`, override `FootprintPathingHash` (`Fireplace.mFootprintPathingHash2x1`) and
   `TuningFireplace`. New interaction `LightMyFire : Interaction<Sim, MedievalFireplace>`:
   `RouteToFireplace`, `StandardEntry`, `BeginCommodityUpdates`, `EnableFootprintAndPushSims`, then
   `StateMachineClient.Acquire(actor, "Medieval")`, `SetActor("x", sim)`, `SetActor("Fireplace", target)`,
   `EnterState("x", "Enter")`, `SetParameter("CheapVersion", ...)`,
   `AddOneShotScriptEventHandler(0x65, StartFireCallback)` (CLIP script event id 101 lights the fire),
   `RequestState("x", "LightFire")`, `RequestState("x", "Exit")`, `EndCommodityUpdates(true)`, `StandardExit()`.
   `OnStartup`: `RemoveInteractionByType(LightFire.Singleton)`, `AddInteraction(LightMyFire.Singleton)`.
3. Jazz: copy EA `fireplace` from JazzData, rename the machine to the name used in `Acquire` ("medieval"), add an
   actor `fireplacetaper`, change `Create Prop 1080` (decimal OBJD instance; 1080 = 0x438, the EA lighter) to the
   cloned prop's instance, point `Play` at new CLIP instances, and fix
   `Assign Actor "a2o_fireplace_start.ma"."fireplacetaper" as "fireplacetaper"`.
4. CLIP: the copied prop clip still named the old actor; in s3pe grid set the **actor name and its hash** to the new
   Jazz actor, and also in **every event** - otherwise the Sim's hand is empty (the prop's flame effect is a CLIP
   event).
5. Prop: clone the EA prop (keeps bones and hashes), keep proportions so the clips fit.
6. Without a tuning XML the object was "a death trap"; without an ITUN children could use it and stretched (no child
   clip). ITUN: `<Interaction name="...LeeFishMod.MedievalFireplace+LightMyFire+Definition"/>`; instance = FNV64 of
   `LightMyFire_MedievalFireplace` (short interaction and object names joined by `_`, Buzzler's convention).

## Reply notes
- Arsil (2015): `Create Prop` also accepts hex (`Create Prop 0x000004b6 as "mop"`, cleaningMop.jazz); a string name
  does not work.
- EA "mimic" classes exist only to carry their own tuning XML and footprint.

## Observations
- The ITUN `<Object name>` in the post omits the `Mimics.LeeFishMod` part of the namespace while the interaction
  includes it; not clear whether that is a typo or tolerated by the game.
