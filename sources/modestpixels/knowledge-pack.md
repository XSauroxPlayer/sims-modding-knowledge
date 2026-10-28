---
title: Sims 3 Modding Knowledge Pack v1.0 (ModestPixels)
url: none (shared privately; the public pages it cites are listed below)
fetched: 2026-10-27
game: ts3
tags: clip, jazz, rig, stbl, locales, packages, caches, script-modding, testing, tools
status: contradicted
author: ModestPixels
---
# ModestPixels: Sims 3 Modding Knowledge Pack v1.0 (October 2026)

A documentation pack (not a mod) compiled by ModestPixels: modding foundations, packages and localization, assets,
animation and routing, audio, testing, and case studies from ModestPixels' own projects. It was shared privately with
XSauroxPlayer and is summarised here **with ModestPixels' permission**. The pack itself is not published or included
here; the public pages it cites are listed at the end.

The pack marks each statement as a documented or public fact (backed by a linked page) or as a recommendation (an
engineering practice to test). This summary keeps that split. Most format facts below were also
checked on the linked pages on 2026-10-27. Synthesis: `topics/clip-format.md`, `topics/jazz.md`, `topics/rigs.md`, `topics/script-modding.md`,
`topics/tuning.md`, `topics/object-creation.md`.

## Format facts (from the pages the pack cites)
- **CLIP 0x6B20C4F3**: one frame = 1/30 s. The actor/slot table has one primary entry per rig IK chain, with the IK
  targets as secondary entries. Event types 1 attach prop (prop, object and slot hashes plus a 4x4 matrix),
  2 unparent, 3 sound (128-byte name), 4 script event id, 5 effect, 6 visibility, 9 destroy prop, 10 stop effect.
  Clip names are not plain FNV64: adult/object names (`a_`, `o_`, `a2a_`, `a2o_`) are hashed with the top bit
  cleared; other ages hash the adult name, set the top bit and XOR an age mask into the top byte (2nd byte for the
  target). Masks: b 1, p 2, c 3, t 4, h 5, e 6, ad 8, cd 9, al A, ac D, cc E, ah 10, ch 11. The game tries the age
  clip first and falls back to the adult one.
- **Jazz 0x02D5DF13**: names are FNV32. State flags Public 0x1, Entry 0x2, Exit 0x4, Loop 0x8, OneShot 0x10,
  OneShotHold 0x20, Synchronized 0x40, Join 0x80, Explicit 0x100. Play flags as the wiki listed them on 2026-10-27:
  AtEnd 0x1, LoopAsNeeded 0x2, OverridePriority 0x4, Mirror 0x8, TimingMaster 0x10, TimingSlave 0x20,
  TimingIgnored 0x40, ForceBlend 0x80, BaseClipIsSocial 0x400, BaseClipIsObjectOnly 0x1000, HoldPose 0x4000,
  BlendMotionAccumulation 0x8000. Priorities Low 6000, Normal 10000, High 20000, CarryRight 30000,
  CarryLeft 40000, Ultra 50000, LookAt 60000. `Create Prop` takes the object's catalog id rather than a name.
- **_RIG 0x8EAF13DE**: only the newer EA format (v3/v4) matters; the early Granny-based format was superseded around
  the Pets-era changes. Base-game rigs live in `DeltaBuild0`; v4 adds IK chains.
- **DBPF**: resources are keyed by type, group and a 64-bit instance (high and low halves); some index fields can be
  stored once in the index header instead of per entry, so a parser must handle both.
- **STBL 0x220557DA**: the top byte of the instance is the language; each entry has its own 64-bit string id;
  strings are UTF-16 little-endian. When several tables define the same string id, the table whose instance has the
  lowest low 32 bits wins; with the same instance, normal package priority decides.
- **Locales**: ids 0x00 to 0x16 are hexadecimal (23 languages), for example 0x00 English, 0x05 Dutch, 0x07 French,
  0x08 German, 0x13 Spanish (Spain), 0x14 Spanish (Mexico). Reading the range as decimal is a common mistake.
- **Resource roles**: S3SA 0x073FAA07 wraps a managed assembly (not a renamed DLL, so use the tool's import);
  `_XML` 0x0333406C holds XML tuning; ITUN holds interaction tuning (eligibility, autonomy, advertising).
- **Caches** (MTS cache guide): `scriptCache.package` (mods and hacks), `compositorCache.package` (objects),
  `CASPartCache.package` (CAS), `simCompositorCache.package` (Sims and default skins), plus `socialCache`; the game
  rebuilds them. Thumbnail caches are a separate thing.
- **Install layout** (MTS, after patch 1.12): `Mods\Resource.cfg` with `Packages` and `Overrides` under the game's
  Documents folder; a ZIP must be extracted, the game does not load it.
- **Script projects**: C# class library for .NET Framework 2.0 with the ordinary references removed and the game's
  `mscorlib`, `System` and `System.Xml` referenced, Copy Local off. The pure-script tutorial does not require the
  S3SA resource name to match the DLL file name.
- **Compatibility**: NRaas documents that a core mod built for another patch (for example 1.69) triggers a version
  mismatch warning at startup.

## Tool notes
- cmomoney's Blender tools: object mesh tools (TS3 Tools), GEOM tools for CAS meshes, and a slot editor that handles
  routing, container, effect and IK target slots with their flags. Each release targets a specific Blender version.
- Sims 3 ClipTool needs Blender 2.67b and ships prepared Sim and pet rigs.
- denton47's TS3 Sound Tool (beta) depends on EALayer3 and ADPCM; samples in one Audio Tuner must not mix the two
  codecs.
- Heaven (heavensims): recolourable objects need enabled channels, suitable masks and matching preset pattern
  settings (NonCASTable to CASTable with Texture Tweaker).

## Recommendations (the pack's own method)
- Separate the systems before debugging an animated feature: mesh vs skeleton, clip vs actor, state machine, world
  movement, and interruption or reset handling.
- Equal bone counts or similar bone names do not prove compatible bind poses; compare influences and bind
  transforms, and test one joint before a full clip.
- Keep one table per interaction mapping each runtime participant to its Jazz actor, clip actor and slot or prop.
  If a whole object follows a Sim's hand, check which participant is bound to the prop role first.
- Foot sliding: measure world speed against the stride; root translation in the clip plus controller movement
  doubles the displacement, and neither gives walking in place. Decide which system owns travel.
- Test objects already present at load and objects created later, new Sims, save and reload, and repeated use.
  Do not assume static fields persist or reset as needed (NRaas Relativity and Saver show explicit lifecycle
  handling).
- Reimport an exported clip onto the target rig and check its first and last pose and duration.

## Against verified findings
- Agrees with XSauroxPlayer's verified findings on the CLIP frame rate (`verified-in-game`), the effect event and
  the v4 rig IK chains (`verified-in-binary`, `research/ts3-native-ik.md`).
- **Contradicted**: the Play flag values the pack took from the wiki (TimingIgnored 0x40, ForceBlend 0x80 and the
  rows above them) disagree with s3pi-wrappers `AnimationNodeFlags` from bit 0x10 up; see `topics/jazz.md`.
- `Create Prop` taking a catalog id agrees with the forum finding that it takes the OBJD instance, in decimal or hex
  (MTS t=469283).
- The pack credits MTS t=491875 (pie menu options for Sims) to CmarNYC and the Pure Scripting Modding tutorial to
  Buzzler.

## Public pages the pack cites
- NRaas, Patch 1.69: https://www.nraas.net/community/Patch-1-69
- XML Tuning Modding: https://modthesims.info/wiki.php?title=Tutorial:Sims_3_XML_Tuning_Modding
- Pure Scripting Modding (Buzzler): https://modthesims.info/wiki.php?title=Tutorial:Sims_3_Pure_Scripting_Modding
- Object Modding: https://modthesims.info/wiki.php?title=Tutorial:Sims_3_Object_Modding
- Core Modding Basics: https://modthesims.info/wiki.php?title=Tutorial:Sims_3_Core_Modding_Basics
- Game compatible Visual Studio project: https://modthesims.info/wiki.php?title=Sims_3:Creating_a_game_compatible_Visual_Studio_project
- DBPF: https://modthesims.info/wiki.php?title=Sims_3:DBPF
- sims3-package-interface (marcos4503): https://github.com/marcos4503/sims3-package-interface
- S3SA 0x073FAA07: https://modthesims.info/wiki.php?title=Sims_3:0x073FAA07
- STBL 0x220557DA: https://modthesims.info/wiki.php?title=Sims_3:0x220557DA
- Locales: https://modthesims.info/wiki.php?title=Sims_3:Locales
- Installing package files: https://modthesims.info/wiki.php?title=Game_Help:Installing_Sims_3_Package_Files/Setup_and_Files
- Pie menu options for Sims (CmarNYC): https://db.modthesims.info/showthread.php?t=491875
- NRaas source, Common.cs: https://github.com/Chain-Reaction/NRaas/blob/master/NRaas/Common.cs
- NRaas source, Relativity.cs: https://github.com/Chain-Reaction/NRaas/blob/master/NRaasRelativity/Relativity.cs
- NRaas source, Saver.cs: https://github.com/Chain-Reaction/NRaas/blob/master/NRaasSaver/Saver.cs
- Delete cache files: https://modthesims.info/wiki.php?title=Game_Help:Sims_3_Delete_Cache_Files
- RCOL: https://modthesims.info/wiki.php?title=Sims_3:RCOL
- Blender 2.7 TS3 Tools (cmomoney): https://modthesims.info/d/433882
- Blender 2.6 GEOM Tools (cmomoney): https://modthesims.info/t/443780
- Sims 3 ClipTool download: https://sims3cliptool.wordpress.com/download/
- DXT compression types: https://modthesims.info/wiki.php?title=Sims_3:DXT_Compression_Types
- NonCASTable to CASTable (Heaven): https://heavensims.tumblr.com/post/166999961940/noncastable-to-castable-using-texture-tweaker
- Blender 2.65 TS3 Slot Editor (cmomoney): https://modthesims.info/d/456325/blender-2-65-ts3-slot-editor-updated-6-23-17.html
- _RIG 0x8EAF13DE: https://modthesims.info/wiki.php?title=Sims_3:0x8EAF13DE
- CLIP 0x6B20C4F3: https://modthesims.info/wiki.php?title=Sims_3:0x6B20C4F3
- Jazz: https://modthesims.info/wiki.php?title=Sims_3:Jazz
- Jazz scripts tutorial (Lyralei): https://simblr.cc/ts3/tutorial/110-tutorial-jazz-scripts-adding-animations-to-your-objects-finished.html
- TS4 to TS3 animation conversion (FloTheory): https://modthesims.info/showthread.php?t=664843
- TS3 Sound Tool (denton47): https://modthesims.info/showthread.php?t=659038
