---
title: Jazz script and animation problems - how to make props appear during an animation?
url: https://modthesims.info/showthread.php?t=646478
fetched: 2026-10-28
game: ts3
tags: jazz, props, ik, script, carry, clip
status: community-reported
author: zoe22, Lyralei
---
# Props appearing mid-animation (tea maker, MTS Modding Discussion, 2020)

zoe22, Lyralei (9 posts, unresolved at the end). Synthesis: `topics/jazz.md`, `topics/script-modding.md`.

- EA hot beverage pattern: `cup.AddToUseList(Actor)`, `cup.SetHiddenFlags(HiddenFlags.Model)`, `EnterStateMachine`,
  `SetActor("coffeeCup", cup)`, `AnimateSim("Make One Drink")`, `CarrySystem.VerifyAnimationParent(cup, Actor)`,
  then `CarrySystem.EnterWhileHolding`. The EA Jazz state `Make One Drink` (`Public, Explicit`) plays nothing itself
  and transitions to `HoldingCup` (`Public, Entry`): the work happens in the transition path.
- `AnimateSim(state)` = `mCurrentStateMachine.RequestState("x", state)`; `EnterState(actor, state)` hashes both names
  and calls `Proxy.EnterState` (Lyralei, from decompiled code).
- `ParentToSlot(Actor, Sim.ContainmentSlots.RightHand)` before the clip puts the mug "on the fingers", not in the
  palm. EA parents only after the clip; during it the cup is driven by IK targets ("animation magnets").
- Reusing `a2o_hotBeverageMachine_get_coffeeCup` on an EA CoffeeCup almost worked (correct grip until the EA clip
  ended, as it was shorter); the same clip on a cloned TeaMug, or a custom IK clip, left the mug invisible.
- `AddOneShotScriptEventHandler(100u, FillTray)`: CLIP script event id 100 calls back into C#.
- Fixes suggested: same start/end frames for Sim and object clips, split start/loop/end states; TheSweetSimmer
  suggested a CLIP **parent event** (not confirmed in the thread).
