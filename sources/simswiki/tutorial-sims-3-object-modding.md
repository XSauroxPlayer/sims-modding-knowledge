---
title: Tutorial:Sims 3 Object Modding
url: https://simswiki.info/index.php?title=Tutorial:Sims_3_Object_Modding
fetched: 2026-10-28
game: ts3
tags: script-modding, objk, s3sa, interactions, catalog
status: community-reported
author: SimsWiki contributors
---
# Sims 3 Object Modding (simswiki; example namespace KolipokiMod)

Synthesis: `topics/script-modding.md`, `topics/object-creation.md`.

- Core DLLs come from S3SA resources in `Game\Bin\gameplay.package`, `scripts.package`, `simcore.package`; the
  s3pe preview's `ManifestModule:` gives the DLL file name to save under.
- Clone with S3OC (Clone > Normal Objects), then read the original script class in OBJK (Edit OBJK, Script row), e.g.
  `Sims3.Gameplay.Objects.Miscellaneous.StuffedAnimal`, and derive from it.
- **Pitfall:** an object's class must live in a namespace starting with `Sims3.Gameplay.Objects`, otherwise the game
  crashes when the object is bought from the catalog.
- Interactions: `ImmediateInteraction` runs without entering the queue; `[DoesntRequireTuning]` means no ITUN is
  looked up; `Test()` false + a `GreyedOutTooltipCallback` shows a greyed-out entry; add interactions in
  `OnStartup()` (called on first instantiation and on every world load).
- S3SA: s3pe Tools > FNV Hash of a unique name (`KolipokiMod_TalkingTeddy.dll`), FNV64 as instance, group 0; s3pe
  also adds a `_KEY` name resource. Then set OBJK Script to the new full class name.
- VS 2010 was reported buggy when compiling against the game's mscorlib; VS 2008 Express recommended (2012-era note).
