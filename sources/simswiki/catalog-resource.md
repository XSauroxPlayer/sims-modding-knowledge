---
title: Sims 3:Catalog Resource
url: https://simswiki.info/index.php?title=Sims_3:Catalog_Resource
fetched: 2026-10-28
game: ts3
tags: format, catalog, objd, thumbnails, object-creation
status: community-reported
author: SimsWiki contributors
---
# TS3 catalog resources (common block, thumbnails, materials)

Related: `0x319e4f1d.md` (OBJD). Synthesis: `topics/object-creation.md`.

## Types
CFEN 0x0418FE2A, CSTR 0x049CA4CD, CPRX 0x04AC5D93, CTTL 0x04B30669, CRAL 0x04C58103, CTPT 0x04ED4BB2, CFIR
0x04F3CC01, CWAT 0x060B390C, CCFP 0x0A36F07A, CFND 0x316C78F2, **OBJD 0x319E4F1D**, CWAL 0x515CA4CD, CWST 0x9151E6BC,
CRST 0x91EDBD3E, CRMT 0xF1EDBD86.

## Common block (all catalog resources)
`DWORD version (>= 0xC)`, `QWORD name GUID`, `QWORD desc GUID` (STBL keys), `7BITSTR internal name`, `7BITSTR internal
desc`, `FLOAT price`, `FLOAT niceness (1.0)`, `FLOAT crap score (0)`, `BYTE BuildBuyProductStatusFlags`, `QWORD PNG
icon IID`, `BYTE 0`, `FLOAT environment score`, `DWORD fire type (0 none, 1 chars, 2 ash pile)`, `BYTE stealable`,
`BYTE repossessable`, `DWORD UI sort index`; v>=0xD `BYTE placeable on roof`; v>=0xE `BYTE visible in worldbuilder`;
v>=0xF `DWORD product name hash`.
- Status flags: 0x1 ShowInCatalog, 0x2 ProductForTesting, 0x4 InDevelopment, 0x8 ShippingProduct, 0x10 DebugProduct,
  0x20 ObjProductMadeUsingNewEntryScheme.

## Thumbnails
- Icon IID non-zero: thumbnails are types 0x2E75C764/65/66 (small/medium/large) with that IID.
- Icon IID zero: type depends on the catalog type (objects, proxies, foundations, roofs: **0x0580A2B4/B5/B6**;
  fences 0x2653E3C8..; stairs 0x5DE9DBA0..; railings 0x2D4284F0..; paint brush 0x05B1B524..; fireplaces
  0x05B17698..; wall/floor patterns 0x0589DC44..) and the IID = the catalog resource's IID. Medium = small + 1, large =
  small + 2. Several thumbnails differing only in **group** = the different default appearances (presets).
- Group 0 is fine except for wall/floor patterns (need non-zero group). Walls have no thumbnails.

## Material list (OBJD, fences, railings, wall/floor patterns)
- Presets in catalog order; "you can safely delete them". Each: type byte, offsets, then a Material Block + TGI
  block list.
- Material block: complate XML index, name, pattern, list of complate variables (typecodes 1 string, 2 ARGB,
  3 TGI index, 4 float, 5 Vector2, 6 Vector3, 7 bool), nested sub-blocks for patterns.
- Complate string encoding: byte A; `A & 0x80` = literal (length `A & 0x3F`, or next byte if `A & 0x40`), otherwise an
  index into the wiki's string table (`A`, or `(A & 0x3F) + B` if `A & 0x40`).
