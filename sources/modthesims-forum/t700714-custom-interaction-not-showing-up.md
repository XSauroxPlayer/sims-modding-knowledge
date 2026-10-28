---
title: Custom interaction not showing up
url: https://modthesims.info/showthread.php?t=700714
fetched: 2026-10-28
game: ts3
tags: script-modding, interactions, pitfall
status: community-reported
author: MTS thread participants (see the thread)
---
# Custom interaction not showing up (MTS Modding Discussion, Sep 2026)

Beginner question; **no reply** at fetch time, so no confirmed answer. Synthesis: `topics/script-modding.md`.

- Code shape: `kInstantiator` tunable + static constructor registering `World.OnFinishedLoadingWorldFileEventHandler`,
  then `sim.AddInteraction(Singleton, true)` on every Sim; an `ImmediateInteraction<Sim,Sim>` that calls
  `RouteTurnToFace` and `PlaySoloAnimation("a2ad_soc_dogTricks_praise_x")`.
- Not resolved in the thread. Known causes from other curated sources (not confirmed for this case): the
  `kInstantiator` tunable only fires if an `_XML` (0x0333406C) resource named FNV64("Namespace.Class") sets it
  (`sources/simswiki/tutorial-sims-3-pure-scripting-modding.md`); Sims created after load or after reset need
  `kSimInstantiated` handling (t=491875); an `ImmediateInteraction` that plays a looping/route animation is a
  questionable fit.
