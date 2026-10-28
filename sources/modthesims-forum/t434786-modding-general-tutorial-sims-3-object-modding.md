---
title: Modding - General - Tutorial: Sims 3 Object Modding (Q&A)
url: https://modthesims.info/showthread.php?t=434786
fetched: 2026-10-28
game: ts3
tags: script-modding, mscorlib, mono, visual-studio
status: community-reported
author: MTS thread participants (see the thread)
---
# Object Modding Q&A (MTS Tutorials, 2011)

Q&A for `sources/simswiki/tutorial-sims-3-object-modding.md`. Synthesis: `topics/script-modding.md`.

- **The game's mscorlib is Mono's, not .NET's.** Compiling against .NET's mscorlib builds fine, but calls into code
  the game's mscorlib does not implement (or stripped) fail to link at runtime and are hard to debug.
- VS project order that let the game mscorlib be referenced: new project, delete all references, set .NET 2.0, save,
  close and reopen VS, then add the game DLLs (VS 2008 recommended; VS 2010 errored with "already referenced by the
  build system"). Alternative: edit the `.csproj` by hand.
- s3pe "Access denied" on `Game\Bin\gameplay.package`: copy it out of Program Files first.
