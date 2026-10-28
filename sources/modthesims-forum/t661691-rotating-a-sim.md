---
title: Rotating a sim
url: https://modthesims.info/showthread.php?t=661691
fetched: 2026-10-28
game: ts3
tags: animation, jazz, slots, mirroring, script, beds
status: community-reported
author: ani_, Lyralei, zoe22
---
# Rotating a sim - sleeping on the blocked bed side (MTS Modding Discussion, 2021)

ani_, Lyralei, zoe22. Synthesis: `topics/jazz.md`, `topics/ik-and-slots.md`.

- Problem: snapping a Sim to the blocked side's entry slot and playing the nap clip makes it sleep upside down on the
  right side.
- Slot matrices (Lyralei): for custom slots the RSLT matrix must match the rig bone's absolute transform; EA routing
  slots carry `-1` entries (e.g. `_route_0_N`: X `[1,0,0]`, Y `[0,0,-1]`, Z `[0,1,0]`), "slots are always rotated the
  negative way". Wrong signs = Sim facing away (her sheep mod).
- `sim.SetRotation(180f)` after snapping works sometimes.
- Real cause (Lyralei, from EA code and Jazz): the bed code picks the routable side and presets the animations for it;
  the **BedRelax** Jazz mirrors via a state `Un-Reverse Mirror for Single Bed`: `Select on Parameter "MakeOppositeSide"`
  -> `Select on Parameter "IsMirrored"` -> `Actor Operation SetMirror on "bed"` (or `None`). So one clip set serves both
  sides; mirroring is an actor operation, not a second clip.
- Script: `mCurrentStateMachine.SetParameter("IsMirrored", true)`; EA BedRelax parameters seen: `IsMirrored`,
  `IkSuffix`, `IsBedMade`, `IsTent`, `IsTrashBed`, `IsUpperBunk`, `MakeOppositeSide`, `isIgloo`, `IsDreamPod`; entry
  state `"Enter_BedRelax_" + StateNameSuffix` (side suffix). **A state without the Entry flag cannot be entered**
  directly, so re-setting parameters may require re-acquiring the machine.

## Against verified findings
- RSLT matrix = bone bind pose in object space (verified on EA game files by the project author): consistent with
  "must match the rig".
