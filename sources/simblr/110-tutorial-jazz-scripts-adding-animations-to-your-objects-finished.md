---
title: "[TUTORIAL] Jazz scripts - Adding animations to your objects (Lyralei)"
url: https://simblr.cc/ts3/tutorial/110-tutorial-jazz-scripts-adding-animations-to-your-objects-finished.html
fetched: 2026-10-28
game: ts3
tags: jazz, animation, script, clip, object-creation, props, looping
status: community-reported
author: Lyralei
---
# Lyralei: Jazz scripts - adding animations to your objects (TS3)

Uploaded 2023-07-28, updated 2025-01-16. Tools: S3OC (clone), SmoothJazz (simlogical build, NOT the MTS
build, which "won't work with the current patch version"), S3PE, Blender + ClipTool, a C# IDE.

## C# side (interaction `Run()`), minimal working pattern
```
StandardEntry();
EnterStateMachine("<StateMachineName>", "Enter", "x");  // name = Jazz "State Machine" name; "x" = the Sim
SetActor("<objActor>", Target);                          // binds a Jazz actor name to a live object
EnterState("x", "Enter");
AnimateSim("Exit");                                      // AnimateSim(state) == RequestState("x", state)
StandardExit();
```
- `SetActor` binds and validates that the actor exists. Extra props: create with
  `GlobalFunctions.CreateObject(ResourceKey(OBJD key), pos, level, forward, ...)`, then `SetActor("fabric", obj)`;
  clean up with `UnParent()` + `Destroy()`.
- `RequestState(actor, state)` runs a state on a non-Sim actor.
- **Always end with `StandardExit()`**, otherwise the Sim keeps the animation while walking (Zoe22: the Sim
  "would walk a little bit, sew in the air").
- Loops: `AnimateSim("Loop"); bool ok = DoLoop(ExitReason.Default, Callback, null); AnimateSim("Exit");`.
  The callback runs each time the looping clip restarts; inside, check
  `Actor.HasExitReason(ExitReason.UserCanceled / MoodFailure)` and `AddExitReason(...)` to stop. Return `ok`.
- Skill gain: `SkillManager.AddElement(SkillNames.X)`, `StartSkillGain`/`StopSkillGain` around the loop;
  `BeginCommodityUpdates()` / `EndCommodityUpdates(ok)` for motives/buffs/traits.
- Progress bar: `new SimpleStage(name, timeToCompletion, progressFn, showCompletionTime, selectable, visibleProgress)`
  assigned to `Stages`; advance progress in the loop callback with `loopData.mDeltaTime`.
- The page lists the full `ExitReason` enum (None, TimedOut, FailedToStart, RouteFailed, MoodFailure,
  HigherPriorityNext, UserCanceled, Finished, ObjectInUse, PriorityOverride, CanceledByScript, ..., Replan,
  Default, SocializingFailed, Canceled, CancelExternal, CausesBlocking).

## Jazz side (SmoothJazz text syntax)
- Skeleton: `State Machine "N" { Properties Default / Actor "x" / Actor "obj" /
  Assign Actor "<clip>.ma"."x" as "x" / State "Do" { Transitions to "Exit"; Play "<clip>" for "x" } /
  State "Enter" { Properties Public, Entry, Explicit; Transitions to "Do" } /
  State "Exit" { Properties Public, Exit, Explicit } }`.
- `Assign Actor` takes the clip name **with `.ma`** plus the actor name *inside the CLIP*, then the Jazz actor;
  `Play` takes the clip name **without** `.ma` (or a 64-bit hash: `Play 0x6008783968663930 for "x"`).
- Enter and Exit states with those properties are mandatory (StandardEntry/Exit rely on them), plus at least one
  custom state.
- Loop state: `Properties Public, Loop, Explicit` + `Select Random { Weight n { Next State "..." } }` for
  weighted random variants (sewing table: 3 loops, weights 1/2/3).
- SmoothJazz error "Parser doesn't recognise literal": it wants **tabs, not spaces**.
- Packaging: SmoothJazz "Package into" -> import into the object package with S3PE. If the S3PE preview says
  "cannot read resource", the SmoothJazz build is the wrong one.

## Script packaging
- S3SA resource: group 0, instance = FNV64 of the full class name (e.g. `Sims3.Gameplay.Objects.Lyralei.MovingTissues`);
  OBJK "script" field = the same namespace + class.

## Object animation
- Blender + ClipTool: Scene > Load prop (cloned package), pose mode on the rig, key LocRotScale, File > Export >
  Sims 3 Animation. **Object clip names must start with `o_`** or the game does not recognise them.
