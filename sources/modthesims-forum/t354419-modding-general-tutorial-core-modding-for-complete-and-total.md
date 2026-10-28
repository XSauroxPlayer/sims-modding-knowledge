---
title: Modding - General - TUTORIAL - Core Modding (for complete beginners)
url: https://modthesims.info/showthread.php?t=354419
fetched: 2026-10-28
game: ts3
tags: script-modding, core-mod, il, dll, history
status: community-reported
author: MTS tutorial author, with help from Delphy and Lemmy101 (see the thread)
---
# Core modding via IL round-trip (MTS Tutorials, July 2009)

Historical (2009, written with help from Delphy and Lemmy101). Synthesis: `topics/script-modding.md`.

- Core mod = editing EA's gameplay DLLs (`Sims3GameplaySystems`, `Sims3GameplayObjects`, `ScriptCore`...) from
  `Game\Bin\Gameplay.package` (XML tuning is in `GameplayData.package`). In s3pe the S3SA "Value" shows
  `ManifestModule:` = the DLL name; export via Grid > Import/Export.
- Round trip: `ildasm file.dll /output=file.il`, edit the MSIL in a text editor, `ilasm` back, re-import. Example:
  make `GenericPrivacySituation.OtherSimCanIgnorePrivacy` return true by replacing its body with `ldc.i4.1; ret`.
- **Only one core mod can be active** (each replaces the same DLL); combine edits into the one you use.
- Core mods (2009) needed the modding framework `Resource.cfg` and `d3dx9_31.dll`; a freeze at the first loading
  screen meant that DLL was missing.
- A modern alternative to the IL round trip is patching the DLLs with a library such as Mono.Cecil (not covered by
  this source).
