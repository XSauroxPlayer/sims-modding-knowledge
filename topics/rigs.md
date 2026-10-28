---
title: Rigs (TS3 _RIG, Sim rigs, object rigs, BOND; TS4 notes)
summary: _RIG format and IK chains, Sim rig names per age, object rigs, slot adjust, tool rig compatibility
status: community-reported
---
# Rigs

Sources: `sources/simswiki/0x8eaf13de.md` (_RIG), `0x0355e0a6.md` (BOND), `0x033260e3.md` (TkMk, per-track weights
on a rig), `sources/sims3cliptool/cliptool-site.md`, `sources/kilhian/making-poses-with-blender-1-4.md`,
`sources/s4animtools-wiki/getting-started-pose-jaw-rig.md` (TS4), verified: `research/ts3-native-ik.md`.

## TS3 _RIG format
- Use the unencrypted EA format (v3/v4): bones with position, quaternion, scale, name, **mirror index** (opposite
  bone), parent, FNV32 hash, flags; skeleton name; v4 adds IK chains `{bone list, InfoNode[11], PoleVector, SlotInfo,
  SlotOffset, Root}`. Old Granny2 rigs are obsolete.
- Info nodes: 11 entries per chain = `<S>_Info1..Info10` plus one extra slot; CLIP IK target N's weight is the local Z of `Info<N+1>` (verified,
  gate 2^-16, any weight above it = full IK). auRig chains: 0 L arm, 1 R arm, 2-3 legs, 4 root (verified).
- Compress bones (`b__R_Calf__Compress__`) are listed separately in the old format.
- Base game rigs live in `DeltaBuild0`; only the newer EA format matters for modding (wiki, repeated by the
  ModestPixels pack, `sources/modestpixels/knowledge-pack.md`). v4 carrying the IK chains agrees with `research/ts3-native-ik.md`
  (`verified-in-binary`).
- Equal bone counts or similar bone names do not prove compatible bind poses: compare bind transforms and
  influences, and test one joint before a whole clip (ModestPixels pack, method advice).

## Sim rigs (names seen in tools)
- ClipTool blends: `afRig` (adult), `puRig` (toddler), `buRig` (baby), `multi-rigs/a2a_soc.blend` (two adults). EA
  clips also use `auRig` (adult), `cuRig` (child) and creature/object rigs. Clip name prefixes encode age
  (`a_`, `c_`, `p_`, `a2o_`, `a2a_`...); a clip without a matching age prefix "explodes" in game (ClipTool).
- ClipTool rigs and WesHowe AnimTool rigs are not interchangeable.
- Kilhian: early Blender exporters needed an existing EA clip imported onto the rig before keying, or the pose did not
  work in game (cause not explained; probably header data copied from the template clip).

## Object rigs
- Objects with an Animation component (OBJK) have their own rig; prop placement follows the prop rig's
  `transformBone` (+ `_rot`) (TheSweetSimmer, MTS t=668206). ClipTool 1.52 fixed bone assignments for props such as beds
  and doors.

## BOND (slot adjust)
- Per-outfit tweaks of slot/bone offset, scale and rotation, no RCOL tag. Community guess (MTS t=629522): source of
  default `slotOffset` values for IK. **Contradicted** by the binary analysis: `slotOffset` is the raw CLIP track and
  the IK functions contain no per-outfit/body-shape offset; BOND at skinning time (after IK) is untraced
  (`research/ts3-native-ik.md` section 7).

## TS4 (technique that transfers)
- TS4 rig name = the actor name the clip plays on (`x` for Sims); object rigs are exported named exactly as the actor.
  TS3 binds by actor name too (CLIP actor table, Jazz `Actor`/`Assign Actor`).
- TS4 IK rule: forearm and calf bones rotate only on Z; clips start/end in base pose so IK blends (`topics/ts4-animation.md`).

## TS4 page differences
- The TS4 _RIG page gates the skeleton name and IK chain fields differently from the TS3 page (TS4 v3 rigs: chains
  without InfoNode/SlotInfo). Minor contradiction about TS3 v3 skeleton names, unresolved:
  `sources/simswiki/sims4-rig-and-rcol.md`.
