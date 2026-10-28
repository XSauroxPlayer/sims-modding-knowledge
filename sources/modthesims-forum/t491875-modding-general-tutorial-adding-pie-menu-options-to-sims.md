---
title: Modding - General - Tutorial: Adding pie menu options to sims
url: https://modthesims.info/showthread.php?t=491875
fetched: 2026-10-28
game: ts3
tags: script-modding, interactions, events, xml, s3sa, debugging
status: community-reported
author: CmarNYC (as credited by the ModestPixels pack; the thread credits Velocitygrass, Buzzler, twallan)
---
# Adding pie menu options to Sims (MTS Tutorials, ~2012)

Multi-lesson tutorial (credits Velocitygrass, Buzzler, twallan). Synthesis: `topics/script-modding.md`.

- Packaging: S3SA (0x073FAA07) group 0, name = full `Namespace.Class`; `_XML` (0x0333406C) group 0 with the **same
  name** (instance = FNV64 of it) holding the `kInstantiator` tunable. Agrees with the wiki pure-scripting tutorial.
- Adding to Sims: on `OnWorldLoadFinished` iterate `Queries.GetObjects<Sim>()` and `sim.AddInteraction(...)`; also
  listen to `EventTypeId.kSimInstantiated` (births, story progression, MasterController) and `kSimAgeTransition`.
- **Pitfall:** a Sim reset fires `kSimInstantiated` again; check the Sim's interaction list for your definition before
  adding, or the option appears twice.
- Grouping: `GetPath(...)` returns `string[]` submenu levels (`"MyStuff Options..."`). `ThreeButtonDialog` returns
  `ButtonPressed` for simple choices.
- Error handler: `((IScriptErrorWindow)AppDomain.CurrentDomain.GetData("ScriptErrorWindow")).DisplayScriptError(null, ex)`
  with a log-file fallback; the full event list is the enum `Sims3.Gameplay.EventSystem.EventTypeId`.
