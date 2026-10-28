---
title: How TS3 applies a CLIP's runtime IK to a Sim's hands
game: ts3
tags: ik, clip, rig, slots, animation, engine
status: verified-in-binary
---
# TS3 runtime IK: what the engine does with a CLIP's IK table

Original research by the project author: a read-only static analysis of the game executable **TS3W.exe 1.67**
(Windows). Function addresses below are RVAs (image base 0x400000) so that others can find the same code; no
decompiled code is reproduced here. The description was also checked against converted clips that play in game
(hands landing on object levers and handles), so the overall model is `verified-in-game` as well.

Each statement carries one of these marks:
- **[binary]** read directly in the executable;
- **[inferred]** consistent with the code, but one link in the chain was not proven;
- **[open]** not established.

## Notation
- A rotation is a unit quaternion `(x, y, z, w)` with the Hamilton product `a·b`.
- A frame is a pair `(p, q)` (position, rotation). Composition makes `B` a child of `A`:
  `A ∘ B = (p_A + rot(q_A, p_B), q_A·q_B)`.
- The engine keeps two pose arrays per Sim: **LOCAL** (each bone relative to its parent) and **MODEL** (each bone in
  Sim-root space, rebuilt as `MODEL[i] = MODEL[parent(i)] ∘ LOCAL[i]`). The Sim's world transform `(p_sim, R_sim)`
  maps MODEL space to the world. [binary]

## 1. Data
- **Rig chains.** The `_RIG` (0x8EAF13DE) v4 IK chain record holds: the chain bones (for an arm: upper arm, forearm,
  hand), eleven *Info* bone indices (`<S>_Info1..Info10` plus one extra entry), the pole bone
  (`<S>_armExportPole`), the `<S>_slotInfo` bone, the `<S>_slotOffset` bone, and the number of bones after the chain
  root whose MODEL transform is rebuilt after solving. At most six chains are handled. [binary]
- **Chain roles.** On the adult rig `auRig` the chain index is also its role: 0 left arm, 1 right arm, 2 and 3 legs
  (with pelvis and floor correction), 4 root. [inferred from the code paths; the order matches EA clips, which the
  project author checked over EA's CLIP files]
- **CLIP IK table.** For each chain the CLIP lists targets `{index N, actor namespace, slot or bone name}`. When the
  clip is bound to actors, each target becomes `{object id, slot bone index on that object, N}`; up to 11 per
  chain. [binary]

## 2. Per clip: weights and groups (ClipNode evaluate, RVA 0x14E950)
Right after a clip is sampled into LOCAL, the engine builds one *group* per chain:

- The group carries an **offset frame** = the raw LOCAL transform of the `slotOffset` bone, and a group weight of
  1 if the chain has a `slotOffset` bone, else 0. The `slotInfo` bone index is remembered as the group's mask
  index. [binary]
- For each bound target the entry weight is **the local position Z of the Info bone `Info<N+1>`**, multiplied by the
  clip's bone-weight mask when there is one. Entries whose weight is not above **2⁻¹⁶ (≈ 1.53·10⁻⁵)** are dropped.
  The threshold is 2⁻¹⁶, not 0.01. [binary]
- Each surviving entry stores the **Info bone's local rotation** and a zero translation. The Info bone's
  translation is never used except for its Z as the weight. [binary]
- A group with a positive weight sum is added to the chain's request. Foot and root targets
  (`rootWorld`, `L_footWorld`, `R_footWorld`) get extra handling through `world_offset` that does not affect the
  hands. [binary]

## 3. Blending clips (MixerNode evaluate, RVA 0x154CA0; blend-in RVA 0x17E880)
When clips are blended, the groups of every child clip are **concatenated**, not averaged. Each copied group and
each of its entries is scaled by the child's blend weight, by the remaining layer weight and by the layer mask at
the group's `slotInfo` bone (for the group) or the entry's Info bone (for the entry). [binary]

A higher-priority layer that has used up the remaining weight at the `slotInfo` bone therefore zeroes the IK group
of a lower layer. [inferred: the multiplication is in the code; which layers reduce the remaining weight at
`slotInfo` was not traced]

## 4. Building the target (IkNode evaluate, RVA 0x150920)
The IK node sits above the whole blended clip tree. Per frame it: evaluates the tree, builds MODEL from the blended
LOCAL pose, sorts the chains so that a chain whose target is a bone of another chain of the same Sim is solved after
that chain (RVA 0x1508A0), then builds one target per chain. [binary]

For one entry with normalised weight `a = w / Σw` (entries with `a ≤ 2⁻¹⁶` are skipped), the target frame `F` is:
- **target on another object:** with `S` the object's slot in world space (object world matrix times the slot's
  local transform), `F.q = R_sim⁻¹ · S.q · q_Info` and `F.p = rot(R_sim⁻¹, S.p − p_sim)`;
- **target on the Sim's own bone:** `F = MODEL[bone] ∘ (0, q_Info)` [rotation binary, position path inferred];
- **no bound object:** `F = (0, q_Info)` already in Sim space.

Inside a group the entries' rotations are summed with weights `a` (flipping the sign of a quaternion that lies in
the opposite hemisphere) and normalised; positions are summed with the same weights. The group frame is then
`G = (Σ a·F.p, normalise(Σ ±a·F.q)) ∘ offset`, i.e. **`slotOffset` is applied once, after the targets are
averaged**. Groups are combined the same way with weights `g.w / total`. The result is the chain target in MODEL
space. The pole is the **FK (blended) position** of the pole bone. A chain with more than one bone and no pole is
skipped. [binary]

Consequences:
- **There is no IK/FK blend.** Info weights are normalised within a group and group weights by their total, so any
  chain with a surviving entry gets 100% IK, however small the clip's blend weight or the Info Z. Only the
  zero/non-zero gate at 2⁻¹⁶ matters. Partial Info weights mix *targets*, not IK with FK. [binary]
- With a single target the hand goes to `slot ∘ Info rotation ∘ slotOffset`. With several targets the
  `slot ∘ Info` frames are averaged first and `slotOffset` is applied once.
- Pelvis adjustment and root motion scale (tunables, debug name "Root Motion Scale") apply only to chain roles 2, 3
  and 4, never to arms. [binary]

## 5. Solver (RVA 0x17D990): analytic two-bone IK, once per chain
Let `P0, P1, P2` be the MODEL positions of the upper arm, forearm and hand in the current blended pose, `T` the
target position, `d = T − P0`, `D² = |d|²`, and `L1² = |P1 − P0|²`, `L2² = |P2 − P1|²` (bone lengths taken from the
current pose, so there is no stretch). [binary]

1. **Bend plane.** `n = normalise((pole − P0) × d)`. A swivel rotation about `d` exists but its angle is always 0.
   The elbow lies in the plane of shoulder, target and pole, on the pole's side: the pole is a point, not a
   direction. [binary]
2. **Elbow.** `t = ½(1 + (L1² − L2²)/D²)` (0 if `D² ≤ 10⁻¹²`), `C = P0 + t·d`, `m = d × n`,
   `h² = L1² − D²·t²`. **Soft reach limit:** if `h² ≤ k1·L1²` then `h² = max(0, k1·L1² + k2·(h² − k1·L1²))`
   with `k1 = 0.001`, `k2 = 0.01`. Desired elbow `E = C + √(h²/|m|²)·m`. [binary]
3. **Upper arm.** Rotate by the shortest arc (RVA 0x17D380; identity for parallel vectors) taking the current elbow
   direction `P1 − P0` to `E − P0`, expressed in the bone's own frame; rebuild MODEL. [binary; that the frame is
   the bone's inverse model rotation is inferred]
4. **Forearm.** Shortest arc taking the new wrist direction to `T − P1`; rebuild MODEL. [binary]
5. **Hand.** The hand's MODEL rotation is set **exactly** to the target rotation:
   `LOCAL_hand.q ← LOCAL_hand.q · conj(MODEL_hand.q) · target.q`; then rebuild MODEL for the chain's bones. [binary]

Properties: only rotations are written, never bone translations; an unreachable target leaves the arm straight
towards it with the hand short; there is no twist distribution, so forearm-twist or helper bones keep their FK
local transforms and just follow. [binary]

## 6. Timing
Clip nodes write their groups while sampling; mixers concatenate and weight them while blending FK; the IK node
then solves **once per frame, on the final blended pose**, arms in dependency order. The IK result is never
blended back with FK. [binary]

## 7. Body shape and outfits
- None of the functions above applies a per-body-shape or per-outfit hand offset, and bone lengths come from the
  current pose. In this path `slotOffset` is applied exactly once. [binary for these functions]
- Whether BOND (0x0355E0A6) or morph bone deltas reach LOCAL before the IK node, or only at skinning time, was not
  traced. If they are applied at skinning they move the hand *after* IK, which would explain a constant hand-to-slot
  error per body shape. [open]

## Function reference (TS3W.exe 1.67, RVAs; names are descriptive, not EA's)
| RVA | role |
|---|---|
| 0x150920 | IK node evaluate: evaluates the clip tree, builds targets, calls the solver |
| 0x1508A0 | chain ordering by dependency |
| 0x17D990 | chain solver (two-bone analytic, one-bone root, hand rotation) |
| 0x17D380 | shortest-arc quaternion between two vectors |
| 0x174600 | MODEL rebuild from LOCAL for a bone range |
| 0x14E950 | clip node evaluate: Info weights and rotations, slotOffset group |
| 0x154CA0, 0x17E880 | mixer evaluate, blend-in of IK groups with weight and mask |
| 0x17CAA0 | bone mask lookup (−1.0 out of range) |
| 0x1695A0 | binding of CLIP IK targets to objects and slot bones |
| 0x179460 | CLIP IK table parse |
| 0x17C4B0 | `_RIG` parse (IK chains) |
| 0x3CFE50 | FNV-1 32-bit lower-case name hash |

## Open points
- Which layers reduce the remaining weight at the `slotInfo` bone (section 3).
- The position path for targets on the Sim's own bones (section 4).
- Whether BOND/morph deltas act before or after IK (section 7).
- What the eleventh Info entry is used for.
