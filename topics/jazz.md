---
title: Jazz state machines (TS3 S_SM 0x02D5DF13)
summary: SmoothJazz syntax, script side (StateMachineClient), states/flags/priorities, props, slots, pitfalls
status: community-reported
---
# Jazz (animation state machines)

Sources: `sources/simblr/110-tutorial-jazz-scripts-adding-animations-to-your-objects-finished.md` (Lyralei, full
recipe), s3pi-wrappers `JazzGraph` (https://github.com/ChaosMageX/s3pi-wrappers), wiki pages `Sims_3:Jazz` /
`Sims_3:0x02D5DF13` (see INDEX for status), MTS threads t=642029, t=646478, t=469283, t=586434, t=661691,
the ModestPixels knowledge pack (`sources/modestpixels/knowledge-pack.md`).

## Minimal working machine (Lyralei, MTS t=642029)
- Jazz text (SmoothJazz, **tabs not spaces**): `State Machine "N"`, `Actor "x"`, `Actor "obj"`,
  `Assign Actor "<clip>.ma"."x" as "x"` (clip **source file name with .ma** + actor name inside the CLIP),
  states `Enter` (`Public, Entry, Explicit`), `Exit` (`Public, Exit, Explicit`), at least one custom state with
  `Play "<clip>" for "x"` (name without `.ma`, or a 64-bit hash) and `Transitions to`.
- Loops: `Properties Public, Loop, Explicit` + `Select Random { Weight n { Next State "..." } }`.
- Script: `StandardEntry(); EnterStateMachine("N", "Enter", "x"); SetActor("obj", Target); EnterState("x","Enter");
  AnimateSim("Do"); ... AnimateSim("Exit"); StandardExit();` - forgetting `StandardExit` leaves the Sim animating
  while walking. Loop with `DoLoop(ExitReason.Default, cb, null)`.
- Lower level: `StateMachineClient.Acquire(actor, "N", AnimationPriority.kAPDefault)`, `SetActor`,
  `SetParameter("IsMirrored", true)`, `EnterState`, `RequestState`, `AddOneShotScriptEventHandler(id, handler)` for
  CLIP event type 4.
- Use the simlogical SmoothJazz build; the MTS build does not work with the current patch. S3PE "cannot read
  resource" on the result = wrong build.

## Props
- `Actor "taper"`, `Create Prop <OBJD instance, decimal> as "taper"`, `Play 0x... for "taper"`; the prop CLIP's actor
  name must match the Jazz actor or the hand stays empty (Leefish, MTS t=469283). CLIP event 9 destroys a Jazz prop.
  Rename the actor name **and hash in the CLIP header and in every CLIP event**, and fix the `Assign Actor` line
  (`sources/modthesims-forum/t469283-...md`). `Create Prop` also takes hex (`0x000004b6`), not a string (Arsil).
- Script side of a renamed machine: `StateMachineClient.Acquire(sim, "<machine name>")` must match the Jazz
  `State Machine` name; CLIP script events reach C# via `AddOneShotScriptEventHandler(<event id>, handler)` (EA
  fireplace uses id 0x65 to start the fire).
- Script-created props: `SetActor("name", obj)` after `EnterStateMachine`; clean up with `UnParent()` + `Destroy()`.

## Slots and IK from Jazz
- Play node slot setup: `ActorSlot {chainId, slotId, actorHash, slotHash}` and `ActorSuffix {actor, param}`
  (s3pi-wrappers). Lets Jazz assign or rename CLIP IK targets at play time. See `topics/ik-and-slots.md`.

## Flags and priorities
- StateFlags: Public 0x1, Entry 0x2, Exit 0x4, Loop 0x8, OneShot 0x10, OneShotHold 0x20, Synchronized 0x40,
  Join 0x80, Explicit 0x100 (wiki and s3pi agree).
- Priorities: Low 6000, LowPlus 8000, Normal 10000, NormalPlus 15000, FacialIdle 17500, High 20000, HighPlus 25000,
  CarryRight 30000, CarryRightPlus 35000, CarryLeft 40000, CarryLeftPlus 45000, Ultra 50000, UltraPlus 55000,
  LookAt 60000 (wiki `Sims_3:Jazz`, read 2026-10-28).
- Semantics from the wiki (`sources/simswiki/jazz.md`): only named transitions are followed; Select on Parameter has
  no default case; clip lookup tries the age-specific clip first, then the adult one (hashes are of the adult name);
  `{param}` substitution in clip names; Slot Suffix appends a parameter to slot names (bed side, car/sofa seat).
- **CONTRADICTION (Play node flags)**: the wiki table (page read 2026-10-28; besides the values below it has rows UseTimingPriority 0x100, UseTimingPriorityAsClockMaster 0x200, AdditiveClipIsSocial 0x800,
  AdditiveClipIsObjectOnly 0x2000, and Interruptible 0x60) gives AtEnd 0x1, LoopAsNeeded 0x2,
  OverridePriority 0x4, Mirror 0x8, TimingMaster 0x10, TimingSlave 0x20, TimingIgnored 0x40, ForceBlend 0x80,
  BaseClipIsSocial 0x400, BaseClipIsObjectOnly 0x1000, HoldPose 0x4000, BlendMotionAccumulation 0x8000.
  s3pi-wrappers `AnimationNodeFlags` gives AtEnd 0x1, LoopAsNeeded 0x2, OverridePriority 0x4, Mirror 0x8,
  OverrideMirror 0x10, TimingMaster 0x20, TimingSlave 0x40, TimingIgnored 0x60, Interruptible 0x80, ForceBlend 0x100,
  UseTimingPriority 0x200, UseTimingPriorityAsClockMaster 0x400, BaseClipIsSocial 0x800, AdditiveClipIsSocial 0x1000,
  BaseClipIsObjectOnly 0x2000, AdditiveClipIsObjectOnly 0x4000, HoldPose 0x8000, BlendMotionAccumulation 0x10000.
  From bit 0x10 up they differ by one bit. Evidence for s3pi: the wiki itself says TimingIgnored is "shorthand for
  OverrideTiming0, OverrideTiming1" (Master | Slave): 0x20 | 0x40 = 0x60 fits s3pi, while the wiki's own values give
  0x30, not its 0x40; the wiki looks like one row shifted (Mirror and OverrideMirror merged). Still unverified on EA
  data. XSauroxPlayer's tools copy EA machines byte for byte and never write
  these flags, so check an EA machine before writing them by hand.
- The ModestPixels pack lists the wiki's Play flag values (read 2026-10-27, fewer rows, same numbers), so it sides with
  the wiki here and is marked `contradicted` on this point (`sources/modestpixels/knowledge-pack.md`). Its state flags and priorities agree with the
  wiki and s3pi.
- Machine, state and actor names are FNV32 hashes; clip names are FNV64 (wiki, repeated by the ModestPixels pack;
  `community-reported`).

## Pitfalls
- SmoothJazz wants tab indentation, and the build on MTS is reported broken on the current patch; Lyralei recommends
  the simlogical build (`sources/simblr/110-tutorial-jazz-scripts-adding-animations-to-your-objects-finished.md`,
  repeated in the ModestPixels pack; `community-reported`).
- `Create Prop` takes the prop object's catalog id (ModestPixels pack, from the wiki), consistent with the forum's
  "OBJD instance, decimal or hex" (MTS t=469283).
- Keep one table per interaction: runtime participant -> Jazz actor -> clip actor -> slot or prop. When a whole object
  follows a Sim's hand, check which participant is bound to the prop role first (ModestPixels pack, method advice).
- Object clip names should start with `o_` (Lyralei's claim, t=642029; not verified here). The old AnimTool flow sets
  a CLIP Source Name like `a2o_test.ma`, which is what `Assign Actor` uses (`sources/simswiki/tutorial-sims-3-custom-animations.md`).
- SmoothJazz rewrites `a2o`/`a2c` to `a2a` and `c_` to `a_`, and chokes on `:` in ids.
- Mirroring: EA picks the mirrored variant per side; snapping to the other side without mirroring gives a wrong-side
  pose (Lyralei, MTS t=661691).
- Timing: Sim and object clips in the same state should share start/end frames; split start / loop / stop states to
  avoid slips (Lyralei, MTS t=646478).
