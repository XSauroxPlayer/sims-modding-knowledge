---
title: Tutorial - How to position/animate props in an animation CLIP
url: https://modthesims.info/showthread.php?t=668206
fetched: 2026-10-28
game: ts3
tags: animation, clip, props, slots, parent-event, visibility-event, bond, jazz, script, blender
status: contradicted
author: TheSweetSimmer; replies by zoe22, lizcandor, Xantak
---
# Position/animate props in a CLIP (MTS Sims 3 Creation > Tutorials, June 2022)

TheSweetSimmer (OP), replies by zoe22, lizcandor, Xantak (2023 Q&A on script-created props). Synthesis:
`topics/clip-format.md`, `topics/jazz.md`, `topics/ik-and-slots.md`.

## How props attach
- A **parent event** attaches the prop's **origin** to the position/rotation of the named parent bone or slot. The
  prop is then moved by its own rig's `transformBone` (plus `_rot` bone if present), animated in the prop's CLIP.
- Babies are animated exactly like props (object rigs); carried babies are parented to the Sim's right hand.
- Any bone works as parent, slot or not (demo: cup parented to the right cheek).

## Blender workflow
1. Import the prop; in **object mode** add a Copy Transforms constraint on the prop object targeting the Sim rig's
   parent bone (object-level so the prop rig's local pose stays independent).
2. Pose mode on the prop rig: move `transformBone` to the wanted place; animate the Sim.
3. Sim slots in the ClipTool rig sit at their base position; in game they are moved by **slot offsets from BOND
   resources** (clothing/morph/slider data). The OP ships a .blend action `S3_slotOffsetPlacements` (per age) with
   those offsets to preview EA clips correctly (not downloaded here).
4. **Pitfall**: if a slot is the parent and you also export the Sim clip, reset the slot to default before export,
   otherwise the offset is applied twice in game. zoe22: the hand slot sat on the wrist in Blender but not in game
   for this reason; lizcandor: the slot offset was the fix for her IK-chain tests.
5. Constraints need not be removed: export bakes them.

## s3pe CLIP events (needs the s3pi wrappers for the Grid editor; without them Grid is greyed out)
- Parent event, 5 fields: `Timecode` (seconds from clip start), `ActorNameHash` (actor the event plays on),
  `ObjectNameHash` (the prop actor), `SlotNameHash` (parent bone/slot), `Transform` (4x4 matrix: setting elements
  `00, 05, 0A, 0F` to 1 = identity; `00` alone reportedly works). All names as FNV hashes (s3pe FNV tool).
- Hand-offs between parents: one parent event per switch; the prop snaps at the event time, so the Blender
  constraint switch and the event timecode must match exactly (use seconds timecodes in Blender).
- **Visibility event**: 0 invisible, 1 visible, instant; fades are done by a script event.
- Some S3OC-exported objects come without rig data (no pose mode in Blender): copy the rig from the game files into
  the package.

## Script side (Q&A)
- Working pattern from the OP: `AcquireStateMachine("X"); EnterStateMachine("X", "Enter", "x");
  SetActor("scythe", prop); AnimateSim("state");` - the prop must be set as an actor (and declared in the Jazz
  script); `EnterSim` is redundant after `EnterStateMachine`.
- `GlobalFunctions.CreateProp` returns an `ObjectGuid` (no `ParentToSlot`); `CreateObjectOutOfWorld` returns an
  `IGameObject` with `ParentToSlot(Actor, Sim.ContainmentSlots.LeftHand)` and `SetHiddenFlags(HiddenFlags.Nothing)`.
  The asker's soft reset came from not assigning the prop actor.

## Against verified findings
- Agrees with XSauroxPlayer's converted clips: prop placement follows the prop rig's `transformBone` (+ `_rot`).
- BOND slot offsets: this tutorial is about **slots used as parents**; the binary analysis (`research/ts3-native-ik.md`) says the IK `slotOffset`
  is the raw CLIP track with no per-outfit term in the IK code. Both can be true (parenting to a slot vs IK
  target math); not contradictory, but BOND's effect on slot positions at runtime is untraced.
