---
title: Tutorial - First steps in Sims 3 Script Modding - Setting up SharpDevelop
url: https://modthesims.info/showthread.php?t=632267
fetched: 2026-10-28
game: ts3
tags: script-modding, csharp, ide, s3sa, setup
status: community-reported
author: Battery
---
# SharpDevelop project for TS3 scripts (MTS Tutorials, Aug 2019)

Battery. Same settings as the Visual Studio tutorial (`sources/simswiki/creating-a-game-compatible-visual-studio-project.md`).
Synthesis: `topics/script-modding.md`.

- C# **Class Library, .NET Framework 2.0** (the game needs 2.0).
- Remove all default references; add the game DLLs: `mscorlib`, `ScriptCore`, `SimIFace`, `Sims3GameplayObjects`,
  `Sims3GameplaySystems`, `Sims3Metadata`, `Sims3StoreObjects`, `System`, `System.Xml`, `UI` (Local Copy false is
  fine).
- `AssemblyInfo.cs`: `using Sims3.SimIFace;` and `[assembly: Tunable]`.
- Project options: **Do not reference mscorlib.dll** (the game's own mscorlib is used), target 32-bit x86;
  optimize optional.
