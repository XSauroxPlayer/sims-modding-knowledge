---
title: IK and slots (TS3, with TS4 notes)
summary: rig IK chains, Info/slotOffset bones, CLIP IK table, RSLT slot arrays, BOND slot offsets, recipes and pitfalls
status: verified-in-binary
---
# IK and slots

Verified reference (read it first, it beats any community source):
- `research/ts3-native-ik.md` - static analysis of TS3W.exe 1.67 by XSauroxPlayer: how a CLIP's IK table moves
  the hands (`verified-in-binary`, and checked in game).

Public code that parses the same data: s3pi-wrappers `ClipResource.cs` (https://github.com/ChaosMageX/s3pi-wrappers)
and, for TS4, s4animtools `ik_baker.py` (https://github.com/thepancake1/_s4animtools).

## Model (community view, matches the verified one)
- The rig (0x8EAF13DE, new format v4) stores IK chains: bones, 11 Info nodes, pole, slotInfo, slotOffset, root.
  Chain order on auRig: 0 left arm, 1 right arm, 2-3 legs, 4 root (`verified-in-game`: checked by XSauroxPlayer
  on EA clips and with hands placed on object levers in game).
- The CLIP IK table lists, per chain, targets `{index N, actor (namespace), slot or bone name}`
  (`sources/simswiki/0x6b20c4f3.md`). Actor = a Jazz actor; EA objects often target plain rig bones, not RSLT slots
  (e.g. `computer:_IKtarget_2_keyboardE`, `diningChair:sit_template`, `x:b__R_carry_slot`).
- Weight of target N = local position Z of `<S>_Info<N+1>` (lizcandor on MTS; verified: gate 2^-16, any weight above
  it gives full IK, no FK blend). `<S>_slotOffset` = hand pose in the target slot frame. `<S>_armExportPole` = elbow pole.
- Jazz can add or override slot assignments (`ActorSlot {chainId, slotId, actorHash, slotHash}`) and actor suffixes
  (`ActorSuffix`), see `topics/jazz.md`.

## Object slots (RSLT 0xD3044521)
- Five arrays: routing, containment (with flags), effect, IK target, cone (radius/angle). Each slot: FNV32 slot name,
  FNV32 bone name in the object rig, 4x3 matrix, optional offset block. IK slots bound to an animated bone move with it.
- Bone prefixes seen: `_cntm_` containment, `_IKtarget_...` (chair `_IKtarget_sitTemplate_butt` moves where the butt
  lands), `_route_0_N` routing; "slots are always rotated the negative way around" (Lyralei).
- Script names: `Sim.ContainmentSlots.RightHand/LeftHand/Mouth`, `Sim.FXJoints.Head`, `Slot.ContainmentSlot_N`,
  `Slot.FXJoint_N`, `Slots.Hash("Routing")`.

## Sim slots and body shape (BOND)
- BOND resources offset Sim slots per body shape (fat/fit/pregnant). Previewing a Sim clip in Blender without the
  BOND offset puts the hand slot on the wrist (MTS t=668206; the OP's `S3_slotOffsetPlacements` .blend action holds
  the per-age offsets; lizcandor: applying them fixed her IK-chain tests). Do not export a Sim clip with the slot
  moved to the BOND position, or the offset is applied twice.
- Info naming confirmed by TheSweetSimmer (t=637608): `L_info_1` = IK target index 0 of the left arm, matching the
  verified `Info<N+1>` rule. Maternity BONDs: `sources/simblr/5695-...md`.

## Recipes and pitfalls (community)
- lizcandor 3-target recipe, world IK preference, invert target for Sim-to-Sim, timing split into start/loop/stop,
  ParentToSlot mid-clip puts mugs "on the fingers" (`community-reported`: lizcandor and TheSweetSimmer in MTS
  t=668470 and t=626272, Lyralei and zoe22 in t=646478, TheSweetSimmer in t=668206).
- EA cups: IK targets as "animation magnets", parenting only after the clip ends (Lyralei).
- TS4 (s4animtools): "forearms and calf bones must be only rotated on the Z axis"; start and end in the base pose so
  IK blends; Bake IK writes world-IK channels (`sources/s4animtools-wiki/basic-ik-tutorial.md`). TS4 `IkConfiguration`
  = `SlotAssignment {chainId, slotId, targetNamespace, targetJointName}` - same idea as TS3.

- cmomoney's Blender 2.65 TS3 Slot Editor edits routing, container, effect and IK target slots with their flags
  (https://modthesims.info/d/456325, cited by the ModestPixels pack, `sources/modestpixels/knowledge-pack.md`).

## Open / contradictions
- Community: "exact default slotOffset values are unknown". Verified: slotOffset is the hand pose in the slot frame,
  composed once after the weighted average of targets (`research/ts3-native-ik.md`). Not a contradiction, the community just did not
  know.
- Community tutorials key partial Info weights for blending in and out; verified engine behaviour: any weight above
  2^-16 gives full IK (weights only mix targets, not IK vs FK). Treat partial-weight "fade" recipes with care.
