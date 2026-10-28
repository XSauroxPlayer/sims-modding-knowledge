---
title: Script mod loads but static constructor never fires - [Tunable] kInstantiator not triggering
url: https://modthesims.info/showthread.php?t=699933
fetched: 2026-10-28
game: ts3
tags: script-modding, tunable, xml, kinstantiator, debugging
status: community-reported
author: MTS thread participants (see the thread)
---
# kInstantiator not triggering (MTS Modding Discussion, Jul 2026)

Synthesis: `topics/script-modding.md`.

- Symptom: assembly listed as loaded (ErrorTrap "Loaded Assemblies") but the static constructor never runs.
- Cause: the `_XML` (0x0333406C) tuning resource. Its instance must be FNV64("Namespace.Class") of the class holding
  `kInstantiator` **and its content must set that tunable**; fixing the XML content in s3pe solved it (Destrospean;
  he also published a drag-and-drop tool that generates the `_XML` resources from the assembly in a package).
- Confirmed not to matter: Roslyn-compiled assemblies (linker 48.0) and corflags `0x3` (ILONLY + 32BITREQUIRED)
  match working mods; patch 1.67.2.
