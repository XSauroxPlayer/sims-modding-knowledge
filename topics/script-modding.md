---
title: TS3 script modding (C# core/gameplay, S3SA, state machines, props)
summary: project setup, S3SA, script class, StateMachineClient usage, props and slots from script, debugging
status: community-reported
---
# Script modding (TS3)

Sources: wiki `Sims_3:Creating_a_game_compatible_Visual_Studio_project`, `..._Microsoft_Visual_2008_ExpressEdition`,
S3SA 0x073FAA07 (see INDEX), `sources/simblr/110-...` (Lyralei Jazz + script), MTS threads (see INDEX),
`sources/nonasims/script-class-and-tuning.md`. Jazz details: `topics/jazz.md`; slots/IK: `topics/ik-and-slots.md`.

## Basics
- Script mods are .NET 2.0 Class Libraries compiled against the game's own decrypted `mscorlib` (default mscorlib
  reference disabled or replaced by hand in the .csproj), `ScriptCore`, `SimIFace`, `Sims3GameplayObjects`,
  `Sims3GameplaySystems`, `Sims3StoreObjects`, `Sims3Metadata`, `System`, `System.Xml`, `UI`, all Copy Local = False,
  platform x86 (`sources/simswiki/creating-a-game-compatible-visual-studio-project.md`).
- Stored in an S3SA resource (0x073FAA07) with instance = **FNV64 of the DLL name** (e.g. `"ToiletInge.dll"`,
  `sources/simswiki/howimadeatoiletclasswithtuning.md`). Other tutorials hash the full class name or any unique
  string: the S3SA instance only has to be unique (`sources/simswiki/tutorial-sims-3-object-modding.md`,
  MTS t=642029). No piecemeal overrides of EA assemblies
  (`sources/simswiki/0x073faa07.md`).
- Subclassing an EA object: subclass the EA class, expose each `[Tunable] static` component tuning by overriding its
  virtual property (`CleanableTuning`, `RepairableTuning`, ...), point OBJK at the new class (toilet recipe).
- **Object classes must live in a namespace starting with `Sims3.Gameplay.Objects`**, or buying the object from the
  catalog crashes the game (`sources/simswiki/tutorial-sims-3-object-modding.md`). If the cloned object had no
  animation, also tick OBJK **Sacs** and **Animation** (`sources/simswiki/tutorial-sims-3-custom-animations.md`).
- Pure script mods (no object): `[assembly: Tunable]` + a `[Tunable] static bool kInstantiator` + static constructor;
  an `_XML` (0x0333406C) resource with **instance FNV64("Namespace.Class")** sets the tunable at startup, which runs
  the static constructor; do real work in `World.OnWorldLoadFinishedEventHandler`
  (`sources/simswiki/tutorial-sims-3-pure-scripting-modding.md`).
- Object classes are named in OBJK `Script` (see `topics/object-creation.md`). After changes delete
  `scriptcache.package`.

## Animation from script
- High level: `StandardEntry(); EnterStateMachine("Machine", "Enter", "x"); SetActor("obj", Target);
  EnterState("x", "Enter"); AnimateSim("State"); ... AnimateSim("Exit"); StandardExit();`. Missing `StandardExit`
  leaves the Sim animating while walking. Loops: `DoLoop(ExitReason.Default, callback, null)`.
- Low level: `StateMachineClient.Acquire(actor, "Machine", AnimationPriority.kAPDefault)`, `SetActor`,
  `SetParameter("IsMirrored", true)`, `EnterState`, `RequestState`, `AddOneShotScriptEventHandler(id, handler)` for
  CLIP script events (event type 4).
- Props: `GlobalFunctions.CreateObjectOutOfWorld(...)`, `SetActor("name", obj)` after entering the machine; EA hot
  beverage pattern `cup.AddToUseList(Actor)`, `SetHiddenFlags(HiddenFlags.Model)`, `AnimateSim`,
  `CarrySystem.VerifyAnimationParent(cup, Actor)`; cleanup `UnParent()` + `Destroy()`.
- `ParentToSlot(Actor, Sim.ContainmentSlots.RightHand)` mid-clip puts the object on the fingers; EA uses IK targets as
  "magnets" during the clip and parents only after it ends, or uses a CLIP parent event (Lyralei, MTS t=646478).
- Slot handles: `Sim.ContainmentSlots.RightHand/LeftHand/Mouth`, `Sim.FXJoints.Head`, objects
  `Slot.ContainmentSlot_N`, `Slot.FXJoint_N`, `Slots.Hash("Routing")`.

- **Quick CLIP test without Jazz:** `Actor.PlaySoloAnimation("<clip>", true)` (MTS t=632115).
- Replace an EA interaction by reassigning its `Singleton` in OnPreload, not on world load (MTS t=632115).
- Localised strings: `Localization.LocalizeString("<Ns>/<Mod>/<Interaction>:<Key>")`, STBL id = FNV64 of the key
  (MTS t=434670).

## Tuning link
- Each script interaction can be tuned with an ITUN keyed on its `+Definition` class (`topics/tuning.md`).

## Project setup and debugging (forum)
- SharpDevelop works as well as Visual Studio: .NET 2.0 class library, game DLL references, `[assembly: Tunable]`,
  "Do not reference mscorlib", x86 (MTS t=632267).
- Debugging: alarm-delayed notifications for preload code, `OnWorldLoadFinished` where alarms do not run; show
  exceptions via the game's `ScriptErrorWindow` or `ScriptError.WriteMiniScriptError()` (MTS t=633012).
- Effects from script: `VisualEffect.Create(name)`, `ParentTo(sim, Sim.FXJoints.Head)` or a containment slot,
  `Start()` (MTS t=541491).
- Clones keep the OBJK script class, so they play the original Jazz; new animations need a renamed script class and a
  Jazz copy with a new instance (MTS t=586434).

- The game's mscorlib is **Mono's**, not .NET's: building against .NET's mscorlib compiles, but calls into missing
  or stripped code fail at runtime (MTS t=434786). The custom-namespace buy-mode crash is thrown in unmanaged code,
  cause unknown (MTS t=424674).
- Sim interactions from a pure script mod: add on world load to `Queries.GetObjects<Sim>()`, listen to
  `kSimInstantiated` and `kSimAgeTransition`, and skip Sims that already have the interaction (a reset re-fires
  instantiation) (MTS t=491875).

## Not yet covered
- Core modding (2009 IL round trip, one core mod at a time): `sources/modthesims-forum/t354419-...md`.
- Interaction tuning (ITUN) beyond the age/species codes in `topics/tuning.md`; localized strings (MTS t=434670,
  queued).

## API reference
- Community API docs: simswiki `TS3PR` page tree, one page per namespace/type, generated by reflection in 2021
  (nested types such as interaction `Definition` classes omitted; most type pages are stubs). Decompiled game DLLs
  stay the source of truth (`sources/modthesims-forum/t651931-sims-3-code-documentation.md`).
