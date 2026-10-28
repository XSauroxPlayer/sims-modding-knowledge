---
title: TS3 tuning (ITUN, XML tuning, commodity kinds)
summary: ITUN structure, custom-interaction ITUNs, nested class names, advertising, scriptcache
status: community-reported
---
# Tuning (TS3)

Sources: `sources/simlogical/itun-custom-interaction.md`, `sources/nonasims/script-class-and-tuning.md`, wiki
`Sims_3:HowIMadeAToiletClassWithTuning` and the `_XML` 0x0333406C / ITUN 0x03B33DDF pages (see INDEX; curated when
marked so).

## ITUN (interaction tuning)
- One ITUN per interaction/object pair, mostly in `GameplayData.package`. Plain XML; editable as text in s3pe.
- Header: `<Interaction name="Namespace.Class+Interaction+Definition"/>`, `<Object name="Namespace.ObjectClass"/>`,
  `<CodeVersion name="BaseGame" considerCodeVersion="False"/>`.
- `<Current_Tuning>`: `<Disallow DisallowAutonomous DisallowUserDirected DisallowPlayerSim/>`; `<BaseAvailability>`
  with `AgeSpecies` (`"T,Y,A,E"`), motive, mood, skill, career thresholds, lot/world/room, misc (pregnant,
  inventory); `<Check>`; `<Tradeoff name>` with `<Localization autoGenerate>`, `<Time value addRoute>`,
  `<Exit funExit stressExit interruptible>`, `<RouteLeadIn>`, `<AskJoinInteraction joinable>`, `<ScoringFunction>`,
  `<ActionTopic>`, `<Output>` of `<Change type advertised locked actual updateType timeDependsOn
  updateEvenOnFailure updateAboveAndBelowZero/>`.
- `advertised` = autonomy attraction; `actual` = real change; `updateType` `ImmediateDelta` or `ContinuousFlow`.
  `type` is a CommodityKind (motives, skills, traits, career roles such as `BeRepairman`, `BeButler`).
- Custom interaction: copy a similar EA ITUN, instance = FNV64 of a unique name (EA style
  `InteractionName_TargetObjectName`), fix Interaction/Object/CodeVersion/Tradeoff names. Nested classes use `+`
  (`Sims3.Gameplay.ActorSystems.Children.GiveBottle+Definition`).
- CommodityKind values (patch 1.63-1.67) are listed by Nona; some have fixed values (Bladder 17774806, Decoration
  18193954, Fatigue 17774812); an updated list is on Simlogical.

## Object class tuning (XML, not ITUN)
- A custom object class gets its own tuning by copying the EA class's tuning XML from gameplay data with instance =
  **FNV64 of the OBJK script class key**; the class declares `[assembly: Tunable]` and `[Tunable] private static
  X.Tuning kX = new X.Tuning();` fields (Inge Jones' toilet, `sources/simswiki/howimadeatoiletclasswithtuning.md`).

## Practical notes
- After tuning/script changes, delete `scriptcache.package` (Documents\Electronic Arts\The Sims 3).
- Autonomy mods ("no autonomous X") are just ITUN `DisallowAutonomous` edits.
- Excel-style tuning text keys (pattern inferred from one example): STBL id = FNV64 of `Gameplay/Excel/<path>:<Key>`; a TV channel name is
  FNV64 of `Gameplay/Excel/TV/TVChannel:<Name>`; a missing string shows a blank pie menu (MTS t=396117).

- Cache files the game rebuilds (MTS cache guide, via the ModestPixels pack, `sources/modestpixels/knowledge-pack.md`): `scriptCache.package`
  (mods), `compositorCache.package` (objects), `CASPartCache.package` (CAS), `simCompositorCache.package` (Sims),
  `socialCache.package`. Thumbnail caches are separate.
- Install layout since patch 1.12: `Mods\Resource.cfg` plus `Mods\Packages` and `Mods\Overrides` under the
  game's Documents folder; ZIP files must be extracted first.

## Not yet covered
- Simlogical "ITUN Modding Discussion" page; MTS Tuning forum threads.

## GameplayData basics (wiki)
- `Game\Bin\Gameplay\GameplayData.package` holds DMTR, ITUN and _XML. ITUN rows carry the autonomy flag, ages
  `B,P,C,T,Y,A,E`, little dogs `CD,AD,ED`, large dogs `CL,AL,EL`, and per-motive **Advertised** (autonomy's
  expectation) vs **Actual** (real gain) values (`sources/simswiki/tutorial-sims-3-xml-tuning-modding.md`).
- Custom skills in ITUN outputs: register the SKIL `CommodityKind` and `SkillNames` in the enum parsers from the
  static constructor, and keep the CommodityKind in 0x20000000-0x2FFFFFFF (`IsSkill`: `k >> 28 == 2`) (MTS t=690249).
- Enum extension at load time (`ParserFunctions` enum parsers) is the general trick that lets tuning XML reference
  mod-defined enum names; it must run before tuning is parsed (static constructor).
