---
title: Tutorial:Sims 3 Core Modding Basics
url: https://simswiki.info/index.php?title=Tutorial:Sims_3_Core_Modding_Basics
fetched: 2026-10-28
game: ts3
tags: script-modding, core-mod, il, s3sa, ui
status: community-reported
author: SimsWiki contributors
---
# Sims 3 Core Modding Basics (simswiki; example: CAS slider hack)

Synthesis: `topics/script-modding.md`. Older forum version: MTS t=354419.

- A core mod is a **resource override**: an S3SA with the same key as one of the game's **eight core libraries**
  (three .NET/Mono framework assemblies, five TS3 script-engine assemblies) from `gameplay.package`,
  `scripts.package`, `simcore.package` in `Game\Bin`.
- Workflow: export the DLL (s3pe Grid > Assembly > Export, name from `ManifestModule`), `ildasm ui.dll /out=ui.il`,
  edit the CIL, `ilasm` back, import into an S3SA with the original key.
- Example target: `Sims3.UI.CAS.CASFacialBlendPanel.AddSliderGridItem` in `UI.dll`: slider count limit `0x14` (20),
  slider range -256..256 (`0xFFFFFF00`..`0x100`, value = data * 256); the `mSliderData` array is sized in the
  constructor and must be enlarged too.
- A modern alternative is patching the DLLs with a library such as Mono.Cecil (not covered by this source).
