# Contributing

Corrections and new sources are welcome. Open an issue or a pull request.

## Adding a source page
1. Copy `templates/source-page.md` to `sources/<site>/<short-name>.md`. Use the site's own id in the name when it
   has one (for example `t668470-using-ik-targets-in-game.md` for an MTS thread).
2. Fill in the front matter: `title`, `url` (the full public link), `fetched` (the date you read it), `game`
   (`ts2`, `ts3`, `ts4`, or a comma-separated list), `tags`, `status` and `author`.
3. Summarise in your own words. Keep only what a modder needs: formats, values, steps that are not obvious, and
   pitfalls.
4. Link the page from the matching topic in `topics/`, and add any disagreement to that topic's "Contradictions"
   section.
5. Run `python tools/build_index.py` and commit `INDEX.md` with your page.

## Status labels
Every page has exactly one `status`:
- `verified-in-game` - you tested it in game and it behaves as stated. Say what you built and what you saw.
- `verified-in-binary` - you checked it byte for byte on EA game files, or by analysing the game executable. Say
  what you checked and on how many files.
- `community-reported` - the source says it; not checked independently. This is the default.
- `contradicted` - the page conflicts with another source or with a verified finding; explain where.

Topic pages also mark single facts inline with these labels. Never upgrade a label without evidence you can
describe.

## Citation rules
- Every source page links its original URL and credits its author(s) in the `author` field. Credit people named
  in the source for the specific facts they contributed.
- Quotes: short, one sentence at most, in quotation marks, and only when the exact wording matters. Everything
  else is paraphrased.
- Do not copy tables, code listings, images or long passages from a source; summarise and link instead.
- Only public pages that need no login. Respect each site's robots.txt and terms, and do not hammer sites.
- Write in English.

## What must not be added
- Game files or data extracted from them (packages, clips, rigs, meshes, textures, sounds, strings).
- Decompiled or disassembled code, or pseudo-code copied from a decompiler. Describe behaviour in prose and maths
  instead, as `research/ts3-native-ik.md` does, and give function addresses so others can check.
- Mod files, tools or binaries of any kind, and links to pirated content.
- Personal data, private messages, or content from private or paid sources.
- Local file paths from your own machine.
