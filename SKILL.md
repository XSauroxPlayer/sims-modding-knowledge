---
name: sims-modding-knowledge
description: Look up how The Sims 3 (and the TS2/TS4 parts that matter for converting to TS3) store and play animation clips (CLIP), IK and slots, Jazz state machines, rigs, objects, script mods and tuning. Use before writing or debugging a Sims mod, a CLIP/_RIG/RSLT/OBJD parser, a Jazz graph, or a TS2/TS4 -> TS3 conversion, and whenever a Sims file format or engine behaviour would otherwise be guessed.
---

# Sims modding knowledge

A curated, source-linked knowledge base. Every page summarises a public source or original research, links it,
and carries a status label. Answer from these pages, not from memory, and cite the page you used.

## How to look things up
1. Start with `INDEX.md`. It lists the topic pages (one synthesis per subject) and every source page with its
   game, tags and status.
2. Read the matching topic in `topics/`:
   - `clip-format.md`: CLIP binary layout, channels, IK table, events, clip name hashing.
   - `ik-and-slots.md`: rig IK chains, Info/slotOffset bones, RSLT slots, BOND offsets.
   - `jazz.md`: Jazz state machines, flags, priorities, props from Jazz.
   - `rigs.md`: _RIG format, Sim and object rigs.
   - `object-creation.md`: cloning, MLOD, textures, footprints, slots, script class; conversion from TS2/TS4.
   - `script-modding.md`: C# script mods, S3SA, StateMachineClient, strings and locales.
   - `tuning.md`: ITUN and XML tuning.
   - `ts2-formats.md` and `ts4-animation.md`: source formats for conversion work.
3. For runtime hand IK (what the engine does with a clip's IK table), read `research/ts3-native-ik.md`.
4. Search when the topic is not obvious. Terms are case-insensitive regular expressions, and all of them must
   match:
   ```
   python tools/search.py slotOffset
   python tools/search.py IK Info --game ts3 -C 1
   python tools/search.py BOND --status contradicted --files
   ```
   Filters: `--game ts2|ts3|ts4`, `--tag`, `--status`, `--files`, `-C <lines>`, `--max <n>`. Plain `grep -ri`
   over the folders works too.
5. Follow a source page's URL when you need more detail than its summary.

## How much to trust a fact
Each page and many single facts carry a label:
- `verified-in-game`: tested in game; behaves as stated.
- `verified-in-binary`: checked on EA game files or in the game executable.
- `community-reported`: what the source says; not independently checked. Treat it as a strong hint and test it.
- `contradicted`: sources disagree. Read the page's "Contradictions" section, and do not pick a side without
  testing.

When two pages disagree, prefer the verified one and say that the other disagrees.

## When answering or writing code
- Name the page you relied on, and its label when it is not verified.
- If nothing here covers the question, say so instead of guessing, and suggest how to verify it: an EA reference
  file, an in-game test, or the executable.
- Do not copy game files or decompiled code into this repository.

## Contributing back
Add a page with `templates/source-page.md` and follow `CONTRIBUTING.md`: summary in your own words, URL and
author credited, one status label, quotes of one sentence at most. Then run `python tools/build_index.py`.
