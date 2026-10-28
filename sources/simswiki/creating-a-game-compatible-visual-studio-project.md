---
title: Sims 3:Creating a game compatible Visual Studio project
url: https://simswiki.info/index.php?title=Sims_3:Creating_a_game_compatible_Visual_Studio_project
fetched: 2026-10-28
game: ts3
tags: script, build, s3sa
status: community-reported
author: SimsWiki contributors
---
# TS3 script mod: game compatible Visual Studio project (wiki)

Synthesis: `topics/script-modding.md`. Script resource layout: `0x073faa07.md` (S3SA).

## Procedure
1. C# **Class Library**, target **.NET Framework 2.0**; prefix the assembly name with your handle.
2. Remove all default references (System, System.Data, System.Xml).
3. Build > Advanced: **Do not reference mscorlib.dll** (VS2008). VS2010 needs it ticked plus a manual reference;
   VS2012+ has no option: add the game's mscorlib by hand in the .csproj:
   `<Reference Include="mscorlib"><HintPath>...game mscorlib.dll...</HintPath><Private>False</Private></Reference>`.
4. Reference the extracted and decrypted game assemblies: mscorlib, ScriptCore, SimIFace, Sims3GameplayObjects,
   Sims3GameplaySystems, Sims3StoreObjects, Sims3Metadata, System, System.Xml, UI.
5. All references **Copy Local = False**.
6. VS2012+: warning MSB3270 (MSIL vs x86 `Sims3Metadata`) - set the platform target to **x86**.

## Notes
- The point is to compile against the game's own (Mono-era, 2.0-profile) mscorlib, not the desktop one.
