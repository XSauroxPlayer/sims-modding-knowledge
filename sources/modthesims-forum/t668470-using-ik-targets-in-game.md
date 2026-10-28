---
title: Using IK targets in-game
url: https://modthesims.info/showthread.php?t=668470
fetched: 2026-10-28
game: ts3
tags: animation, ik, slots, blender, clip
status: community-reported
author: lizcandor, TheSweetSimmer
---
# Using IK targets in-game (MTS Modding Discussion, June 2022)

lizcandor, TheSweetSimmer. Synthesis: `topics/ik-and-slots.md`.

## lizcandor's Blender workflow (TS3 Sim to object, multi-target)
1. IK target object for the left hand; hand bone IK constraint with influence 0.1.
2. On the IK target: 3 "copy transforms" constraints (one per target slot on the object rig) plus copy location and
   copy rotation from the actor's **`L_slotOffset`** bone, as offsets.
3. Key the influences so one slot dominates at each moment.
4. **Copy those influence keys to the Z position keys of `L_Info1`, `L_Info2`, `L_Info3`** (one Info bone per target).
5. Export; in s3pe add the CLIP IK target entries (3 targets on the left-hand chain).
- Result: right position, wrong hand rotation at some moments.

## Answer (TheSweetSimmer)
- Hand rotation depends on the hand's and the slot's rotation; when a Sim targets **another Sim**, the rotation is
  **inverted** (the Sims face each other), so invert the targeted slot. lizcandor confirmed this fixed it. World IK
  is the easiest kind.

## Against verified findings
- Agrees with the binary analysis that `Info<N+1>` local Z carries the weight of target N (her Info1..3 = targets 0..2) and `slotOffset` is applied
  (`research/ts3-native-ik.md`).
- **Possible mismatch**: copying fractional Blender influences to Info Z assumes blended weights; the binary analysis
  says any weight above 2^-16 is full IK and targets are weighted-averaged before slotOffset is composed
  once. Fractional overlap between targets would therefore average positions, not fade IK in and out. Not tested.
