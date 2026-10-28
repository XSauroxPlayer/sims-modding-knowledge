---
title: Skill gain through ITUN for custom skills
url: https://modthesims.info/showthread.php?t=690249
fetched: 2026-10-28
game: ts3
tags: tuning, itun, skills, enums, script-modding
status: community-reported
author: zoe22
---
# Skill gain through ITUN for custom skills (MTS Tutorials, zoe22, 2025-2026)

Synthesis: `topics/tuning.md`, `topics/script-modding.md`.

- EA skilling interactions gain skill from ITUN outputs like
  `<Change type="SkillLogic" advertised="400" locked="True" actual="400" updateType="ContinuousFlow" .../>`.
  Custom (and store) skills can use the same route if:
  1. their `CommodityKind` (from the SKIL resource `<Commodity>Name=0x...</Commodity>`) and `SkillNames` value
     (`<Hex>name=0x...</Hex>`) are added to the game's enum parsers (`ParserFunctions.sCaseInsensitiveEnumParsers` /
     `sCaseSensitiveEnumParsers`, generic `AddEnumValue<T>` helper) **in the static constructor** - OnStartupApp is
     too late because tuning is parsed before;
  2. the CommodityKind value passes `IsSkill(k)`: `(int)k >> 28 == 2`, i.e. **0x20000000-0x2FFFFFFF**. The post gives
     536870912-804999999 decimal; the exact upper bound from that check is 805306367 (0x2FFFFFFF).
- Adding to `SkillNames` is also needed for custom skills in career metrics and dream (wish) trees.
- Not enough for autonomy: a custom commodity must also be loaded as a motive on Sims (see douglasveiga's Gardener
  Service mod). Destrospean posted a helper that derives a valid CommodityKind from a string (Code Snippet Jar).
