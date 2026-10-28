---
title: Modding - General - Tutorial: Sims 3 Localized Coding (Q&A)
url: https://modthesims.info/showthread.php?t=434670
fetched: 2026-10-28
game: ts3
tags: script-modding, stbl, localization, fnv64
status: community-reported
author: MTS thread participants (see the thread)
---
# Localized Coding Q&A (MTS Tutorials, 2011)

Q&A for the wiki page `Tutorial:Sims_3_Localized_Coding`. Synthesis: `topics/script-modding.md`, `topics/tuning.md`.

- Code uses `Localization.LocalizeString("<Ns>/<Mod>/<Interaction>:<Key>", args)` (gendered overload
  `LocalizeString(isFemale, key, args)`); the STBL entry id is **FNV64 of that full key string** (example given:
  FNV64("Enirei/LocalizedMod/SayHello:Message") = 0x3345B37043CBFBB2). Changing the key in code but not in the STBL
  source text leaves the string missing.
- Overrides copied as `public` fail to compile ("cannot change access modifiers"): the EA definitions use
  `protected` for `Run`, `GetInteractionName`, `Test`, `GetPath`.
- s3pe quirk (2011): "Replace" on an empty STBL created by Add Resource threw a wrapper error; Import worked.
