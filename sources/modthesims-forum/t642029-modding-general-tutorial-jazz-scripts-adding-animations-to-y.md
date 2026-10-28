---
title: Modding - General - [TUTORIAL] Jazz scripts - Adding animations to your objects (FINISHED)
url: https://modthesims.info/showthread.php?t=642029
fetched: 2026-10-28
game: ts3
tags: jazz, animation, clip, script-modding, object-animation, looping, cliptool, smoothjazz
status: community-reported
author: Lyralei
---
# Jazz scripts: adding animations to objects (MTS Tutorials, Lyralei, May 2020)

Four posts: C# side, Jazz side, s3pe assembly, object animation with ClipTool. Synthesis: `topics/jazz.md`,
`topics/script-modding.md`, `topics/clip-format.md`.

## C# side (Interaction.Run)
- Minimal sequence: `StandardEntry(); EnterStateMachine("<machine>", "Enter", "x"); SetActor("<objActor>", Target);
  EnterState("x", "Enter"); AnimateSim("Exit"); StandardExit();`. The Sim actor is always named `"x"`.
- `AnimateSim(state)` = `RequestState` on actor `"x"`; `RequestState("<actor>", "<state>")` drives another actor.
- A spawned prop becomes an actor the same way: `GlobalFunctions.CreateObject(ResourceKey.FromString("0x319E4F1D:0x00000000:<OBJD instance>"), pos, 0, fwd, null, null)`
  then `SetActor("fabric", prop)`; unparent and `Destroy()` it after the exit state.
- **Pitfall:** skipping `StandardExit()` left a Sim replaying the animation while walking ("sew in the air").
- Loops: `AnimateSim("Loop"); bool flag = DoLoop(ExitReason.Default, callback, null); AnimateSim("Exit");` - the
  callback runs each time the looping clip restarts; end the loop by `Actor.AddExitReason(...)` (UserCanceled,
  MoodFailure, Finished...). Progress bar: `Stages = new List<Stage>{ new SimpleStage(name, timeToCompletion,
  progressTest, showCompletionTime, selectable, visibleProgress) }`; skills via `SkillManager.AddElement` +
  `StartSkillGain`/`StopSkillGain`.

## Jazz side
- Template: `State Machine "<name>"` / `Properties Default` / `Actor "x"` / `Actor "<obj>"` /
  `Assign Actor "<clipName>.ma"."<actorInClip>" as "<jazzActor>"` / states with `Play "<clipName>" for "<actor>"`.
- The `.ma` suffix: the CLIP's internal source/animation name is `<clip>.ma`; `Play` uses the name **without** `.ma`.
  A `Play` may also give the clip instance as hex (`Play 0x6008783968663930 for "x"`).
- Always have `State "Enter"` (`Properties Public, Entry, Explicit`) and `State "Exit"` (`Properties Public, Exit,
  Explicit`) plus at least one playing state. Loop state: `Properties Public, Loop, Explicit` with
  `Select Random` / `Weight n` / `Next State "..."`.
- SmoothJazz: the MTS build no longer works with the current patch; the simlogical build does (author's
  experience). "Parser doesn't recognise literal" = spaces instead of **tabs** for indentation.

## s3pe
- Import the `.jazz` package (Resources > Import > From package). "Cannot read resource" in preview = wrong
  SmoothJazz version. S3SA instance = FNV64 of the full class name (`Sims3.Gameplay.Objects.<User>.<Class>`); OBJK
  Script = same full class name.

## Object animation (ClipTool)
- Blender + ClipTool: Scene > Load prop (the cloned package), pose the rig, key LocRotScale, export Sims 3 Animation.
- Claim: **object clip names must start with `o_`** or the game does not recognise them. Decorative objects without a
  real rig still have a single root bone to animate. Pose Player cannot play object animations.

## Against verified findings
- `o_` prefix rule: consistent with the age/species prefix rule for Sim clips (`topics/rigs.md`, t438716), not
  re-verified for objects here.
