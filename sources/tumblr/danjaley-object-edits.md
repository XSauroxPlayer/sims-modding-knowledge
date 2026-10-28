---
title: Removing Parts of an Object; default replacement mesh (Danjaley)
url: https://danjaleyreblogs.tumblr.com/post/166611404162/removing-parts-of-an-object-i-promised
fetched: 2026-10-28
game: ts3
tags: object-creation, mesh, default-replacement, geometry-states
status: community-reported
author: Danjaley
---
# TS3 object mesh edits - Danjaley, 2017

Also covers https://danjaley.tumblr.com/post/161743367998/hii-have-a-question-about-making-sims3-mod-how (default
replacement answer). Read in a web browser (tumblr 403 to plain fetch).

## Removing parts
- Texture route: clear the parts in multiplier and overlay; works only if the object already uses transparency
  (enabling alpha usually needs TSRW). Example: child broom, a geostate object, so mesh edits were harder.
- Mesh route (Milkshape): a typical decor object has **two groups: the object and the drop shadow plane**; animated
  or glass/FX objects have more.
- **You cannot empty a group** or the mesh will not reimport: leave one triangle and collapse it to a point
  (Milkshape Ctrl+N, Snap together) so it is invisible.

## Default replacement mesh
- Clone with s3oc **without renumbering**, export the mesh in s3pe, edit, reimport; keep the size close to the
  original so EA animations still fit (e.g. a much larger bottle clips).
