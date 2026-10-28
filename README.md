# Sims Modding Knowledge

A searchable set of notes on modding The Sims 3, with the parts of The Sims 2 and The Sims 4 that matter when
converting content to The Sims 3. It covers animation clips (CLIP), Jazz state machines, rigs, IK and slots, object
creation, script modding, tuning, and TS2 formats.

Each source page summarises one public tutorial, forum thread, wiki page or blog post and links back to it. Topic
pages combine those sources into one view per subject and point out where they disagree.

This is an unofficial fan project. It is not affiliated with, endorsed by or sponsored by Electronic Arts, Maxis or
Mod The Sims (MTS). "The Sims" is a trademark of Electronic Arts Inc.

## Layout
- `INDEX.md` - every page with its author, game, tags and status. Start here.
- `topics/` - syntheses per subject (9 pages). Each lists its sources and a "Contradictions" or "Open" section.
- `sources/<site>/` - one summary per source page (78 pages), each with the original URL and author.
- `research/` - original research by [XSauroxPlayer](https://github.com/XSauroxPlayer) (currently how TS3 applies a clip's runtime IK).
- `templates/source-page.md` - the template for a new source page.
- `tools/` - search and index scripts (Python 3.9+, no dependencies).

## How the pages were written and checked
The summaries were written with AI assistance (Claude) from the public pages, then checked against the source and,
where possible, against the game. Every page carries a `status` in its front matter, and topic pages also label
single facts inline. The labels mean:

| status | how it was established |
|---|---|
| `verified-in-game` | Tested in game by XSauroxPlayer: content built that way works (or fails) as stated. |
| `verified-in-binary` | Checked by XSauroxPlayer byte for byte on EA game files, or by static analysis of the game executable (`research/`). |
| `community-reported` | What the source says. Summarised faithfully but not independently checked here. |
| `contradicted` | The source conflicts with another source or with a verified finding. The page says where and why. |

A source page is `community-reported` unless part of it is contradicted; facts on it that were verified are marked
in its "Relevance" or "Against verified findings" notes. Topic pages take the label of their core model.

Treat everything as notes, not as an EA specification. If you find an error, open an issue or a pull request (see
`CONTRIBUTING.md`).

## How to search
```
python tools/search.py slotOffset                 # all pages mentioning slotOffset, topics first
python tools/search.py IK "Info" --game ts3 -C 1  # all terms must match, with one line of context
python tools/search.py BOND --status contradicted --files
python tools/build_index.py                       # rebuild INDEX.md after adding pages
```
Terms are case-insensitive regular expressions. Plain `grep -ri` over the folders works too.

## Third-party content
- The sources summarised here belong to their authors and sites. Pages keep only summaries, short quotes (one
  sentence at most), names and facts, always with a link and credit. Read the original for the full content, and
  follow each site's own terms when you reuse anything from it.
- No game files, extracted EA data, mod downloads or decompiled code are included.
- SimsWiki (simswiki.info): no content licence or copyright page could be found on the site (checked 2026-10-28:
  the usual MediaWiki copyright and disclaimer pages return "not found", and the footer shows no licence). Its pages
  are therefore treated as owned by their contributors: summarised and linked, not copied.
- ModestPixels' Sims 3 Modding Knowledge Pack (v1.0, October 2026) was shared privately with XSauroxPlayer and is
  summarised with ModestPixels' permission in `sources/modestpixels/knowledge-pack.md`; the pack itself is not
  included.
- Mod The Sims forum posts, tumblr posts, blogs and other sites: owned by their authors, under each site's terms.
- Some pages were read through a normal web browser because the site refuses plain HTTP clients. Sites whose
  robots.txt disallows automated readers (for example sims4studio.com) were not read.

## Licence
Original text: CC BY-SA 4.0. Code in `tools/`: MIT. Details in `LICENSE`. Third-party material keeps its own terms.
