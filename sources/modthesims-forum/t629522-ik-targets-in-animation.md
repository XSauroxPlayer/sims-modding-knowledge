---
title: IK targets in animation
url: https://modthesims.info/showthread.php?t=629522
fetched: 2026-10-28
game: ts3
tags: animation, ik, slots, rig, clip, blender
status: contradicted
author: TheSweetSimmer, simmythesim, Lyralei
---
# IK targets in animation (MTS Modding Discussion, 2019)

TheSweetSimmer, simmythesim, Lyralei. An open question thread; no confirmed answer. Synthesis:
`topics/ik-and-slots.md`.

- Symptom: custom clips with IK targets added in s3pe put the hands in the wrong **position** (rotation roughly
  right); converted EA clips and some idles work.
- Community observations: the rig's offset bones (`R_slotOffset`, `L_footOffset`, `rootOffset`...) control where
  the hands go; Info bones carry the per-target "influence"; a clip with 2 targets always active worked, the
  trouble starts when targets switch.
- Guesses (unverified): slot offsets are per-outfit (simmythesim - cf. BOND resources); values are stored outside the
  CLIP because ClipTool does not export them (Lyralei). Sim rigs in FullBuild only have container and effect slots.
- Adding IK constraints directly in Blender snaps the hands exactly onto the slot, which the game does not do.

## Against verified findings
- XSauroxPlayer's analysis of the game binary (`research/ts3-native-ik.md`) answers this: the per-target
  weight of target N is the local Z of `Info<N+1>` (gate 2^-16), the game averages the `slot ∘ Info` frames (Info rotation counts too)
  and then composes the raw `slotOffset` track once. So the offset **is** animated data in the CLIP, not a global
  default, and the spec found **no per-body-shape or per-outfit hand offset** in the IK functions (section 7 there).
  **CONTRADICTION** with the guess that the offset lives outside the CLIP. The per-outfit guess is only partly
  answered: whether BOND deltas move the hand at skinning time (after IK) is untraced there.
