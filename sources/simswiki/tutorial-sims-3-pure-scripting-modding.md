---
title: Tutorial:Sims 3 Pure Scripting Modding
url: https://simswiki.info/index.php?title=Tutorial:Sims_3_Pure_Scripting_Modding
fetched: 2026-10-28
game: ts3
tags: script-modding, tunable, xml, s3sa, events, alarms
status: community-reported
author: SimsWiki contributors
---
# Sims 3 Pure Scripting Modding (simswiki; example namespace "TwoBTech")

Synthesis: `topics/script-modding.md`. MTS Q&A thread: t=424674.

- Entry point trick: `[assembly: Tunable]` in AssemblyInfo, a class with a `[Tunable] static bool kInstantiator`
  and a static constructor. The game parses every `_XML` tuning resource at startup and assigns tunables, which
  touches the class and runs its static constructor.
- The `_XML` resource (type 0x0333406C) that sets `kInstantiator` **must have instance FNV64("Namespace.Class")**
  of the class holding the tunable; the S3SA name/instance can be anything unique. Pitfall: XML content must start
  with `<`, not BOM/garbage bytes.
- The static constructor runs long before the main menu; hook `World.OnWorldLoadFinishedEventHandler` to do real
  work. Use `AlarmManager.Global.AddAlarm(1f, TimeUnit.Seconds, cb, "name", AlarmType.NeverPersisted, null)` to
  delay until the clock runs; `EventTracker.AddListener(EventTypeId.kSimEnteredVacationWorld, cb)` returning
  `ListenerAction.Keep` for event hooks.
- Required references: Sims3GameplayObjects.dll, Sims3GameplaySystems.dll (gameplay.package), plus the
  scripts/simcore DLLs, saved under their exact ManifestModule names.
