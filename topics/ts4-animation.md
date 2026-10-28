---
title: TS4 animation technique that transfers to TS3
summary: s4animtools workflow, events, IK baking math, naming; what carries over to TS3 and what does not
status: community-reported
---
# TS4 animation (only what transfers)

Sources: `sources/s4animtools-wiki/*.md` (event, basic IK, pose/jaw/rig pages), s4animtools source code
(`ik_baker.py`, `rig_constants.py`, https://github.com/thepancake1/_s4animtools). Sims 4 Studio pages are not read: sims4studio.com blocks AI crawlers in robots.txt.

## Transfers to TS3 (same engine lineage)
- Clips at 30 fps, actor-name binding (rig name = actor `x`), FNV hashes for names.
- IK model: per chain targets `{chainId, slotId, targetNamespace, targetJointName}` (TS4 `IkConfiguration`) = TS3 CLIP
  IK table; world-IK channels; weights 1 over the contact range, 0 keys just outside (s4animtools baker).
- IK math (s4animtools `ik_baker.py`): `src = target_rig.matrix_world @ target_bone.matrix`,
  `tgt = obj.matrix_world @ chain_bone.matrix`, `offset = src.inverted() @ tgt` - the same "hand in slot frame"
  quantity TS3 stores in `<S>_slotOffset` (see `topics/ik-and-slots.md`).
- Rules: forearm and calf only rotate on Z; start/end in the base pose so IK blends between clips.
- Parent/unparent, effect start/stop by unique name, visibility, script events exist in both games
  (TS3 event numbers: `topics/clip-format.md`).

## TS4 only (do not port blindly)
- Events: Reaction, Suppress Lipsync, Snap (undocumented), Focus Compatibility.
- Jaw owned by lipsync unless "Allow Jaw Animation" or Suppress Lipsync.
- Clip naming: no actor name in the clip name (exporter appends the rig name); TS3 uses the `a_`/`a2o_`... prefixes and
  age hashing instead.
- Rig bone names: `b__L_Hand__`, `b__ROOT_bind__`, grips `[grip_L, grip_R, root_bind, f_L, f_R]`, walk targets
  `b_L_handDangle_slot` - TS4 rig; TS3 bone names differ.

## Open
- Sims 4 Studio wiki/forum not readable by policy (robots.txt). TS4 wiki pages on simswiki
  (`Sims_4:0x6B20C4F3`, `Sims_4:0x8EAF13DE`, `Sims_4:0x02D5DF13`) are queued; see INDEX for their status.

## TS4 -> TS3 conversion (forum)
- FloTheory's pipeline (MTS t=664843): S4S exports the TS4 clip as `.blend`; the community retarget rig
  `RigBase ts4 to ts3_FACE_V2.blend` drives a TS3 rig; bake by keying the TS3 rig, Auto-Clamped interpolation against
  stutter, export with ClipTool (Blender 2.79). Eyes often break. Child/toddler: paste adult keys onto `CuRig`/`PuRig`
  (prefix `c_`/`p_`).
