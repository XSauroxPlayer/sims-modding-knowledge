---
title: Sims 3 Code Documentation
url: https://modthesims.info/showthread.php?t=651931
fetched: 2026-10-28
game: ts3
tags: script-modding, api-docs, ts3pr, simiface
status: community-reported
author: Lyralei, gamefreak130
---
# Sims 3 Code Documentation (MTS Modding Discussion, sticky, Jan-Mar 2021)

Lyralei, gamefreak130. Synthesis: `topics/script-modding.md`.

- The community API reference is the simswiki **TS3PR** page tree (`simswiki.info/wiki.php?title=TS3PR`),
  started 2010 and refreshed in 2021, MSDN-style: one page per namespace, one page per type.
- gamefreak130 generated a page for every namespace of `Sims3StoreObjects`, `ScriptCore`, `SimIFace`,
  `Sims3GameplaySystems`, `Sims3GameplayObjects` (and others) by reflection (`Assembly.Load` + LINQ over
  exported types). **Nested types (e.g. interaction `Definition` classes) were left out.** Most type pages are stubs;
  filled examples include `SimIFace/Sims3.SimIFace`, `BlockedStatus`, `AnimationPriority`.
- Lyralei: some SimIFace classes (e.g. `AnimationsUtil`) look like leftovers from EA's GrannyRig era and are unused
  by current game code; debug engine functions are still callable from mods.
- A terminology spreadsheet was added under the TS3PR programmer's reference pages.
- Practical note: for real signatures, decompiling the game DLLs (ILSpy/dnSpy) remains the source of truth; the
  wiki explains concepts that the decompiler does not.
