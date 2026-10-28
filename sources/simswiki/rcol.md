---
title: Sims 3:RCOL
url: https://simswiki.info/index.php?title=Sims_3:RCOL
fetched: 2026-10-28
game: ts3
tags: format, rcol, scenegraph, jazz, mesh
status: community-reported
author: SimsWiki contributors
---
# TS3 RCOL container (wiki)

## Header
`DWORD version`, `DWORD public chunk count`, `DWORD unused`, `DWORD external count`, `DWORD internal count`, then
internal chunk TGIs `{QWORD instance, DWORD type, DWORD group}`, external TGIs (same layout, e.g. DDS images), then per
internal chunk `{DWORD absolute position, DWORD size}`.

## Chunk references
1-based (0 = null), high nibble = kind: `0x0xxxxxxx` public internal chunk, `0x1xxxxxxx` private internal chunk (add
the public count to get the index), `0x2xxxxxxx` external (unused), `0x3xxxxxxx` delayed = external resource list.

## Resource types (named by their first chunk; GEOM is the exception)
GEOM 0x015A1849, MODL 0x01661233, MATD 0x01D0E75D, MLOD 0x01D10F34, MTST 0x02019972, TREE 0x021D7E8C, S_SM 0x02D5DF13,
TkMk 0x033260E3, BOND 0x0355E0A6, LITE 0x03B4C61D, ANIM 0x63A33EA7 (animated texture), VPXY 0x736884F1, RSLT
0xD3044521, FTPT 0xD382BF57.

## Model chunks
VBUF 0x01D0E6FB, **shadow VBUF 0x0229684B (no VRTF)**, IBUF 0x01D0E70F, **shadow IBUF 0x0229684F**, VRTF 0x01D0E723,
SKIN 0x01D0E76B, plus MATD/MLOD/MTST/MODL; swizzle info type 0.
- Consistent with shadow LODs verified in game by XSauroxPlayer (LODs 0x10000/0x10001, 8-byte position-only vertices,
  short x/y/z normalized plus a fourth short 32767, decoded as `PosOffset + short * PosScale` from the MATD named by the
  mesh's `ScaleOffsetIndex`). Whether EA's shadow meshes actually use the 0x0229684B/0x0229684F chunk types was not
  checked.

## Jazz chunks (inside S_SM)
S_SM 0x02D5DF13, S_St 0x02EEDAFE, S_DG 0x02EEDB18, S_AD 0x02EEDB2F, S_PD 0x02EEDB46, Play 0x02EEDB5F, Rand 0x02EEDB70,
SoPn 0x02EEDB92, SoDn 0x02EEDBA5 (unused), SNSN 0x02EEEBDC, Prop 0x02EEEBDD, AcOp 0x02EEEBDE, Stop 0x0344D438.
