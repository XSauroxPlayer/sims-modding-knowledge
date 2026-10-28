---
title: Tutorial:Sims 3 XML Tuning Modding
url: https://simswiki.info/index.php?title=Tutorial:Sims_3_XML_Tuning_Modding
fetched: 2026-10-28
game: ts3
tags: tuning, itun, xml, gameplaydata
status: community-reported
author: SimsWiki contributors
---
# Sims 3 XML Tuning Modding (simswiki)

Synthesis: `topics/tuning.md`.

- Tuning lives in `Game\Bin\Gameplay\GameplayData.package`: three resource kinds, **DMTR, ITUN, _XML**.
- ITUN (interaction tuning): autonomy flag, allowed ages/species codes `B,P,C,T,Y,A,E` (Sims), `CD,AD,ED` (little
  dog), `CL,AL,EL` (large dog), traits, lot restrictions, and per-motive **Advertised** (what autonomy expects) vs
  **Actual** (what the Sim gets) values; raise Advertised to make an autonomous action more frequent.
- _XML: class tunables (costs, durations...). A tuning mod is a package with copies of the edited resources (same
  TGI) - export keeps the `_KEY` name resource.
