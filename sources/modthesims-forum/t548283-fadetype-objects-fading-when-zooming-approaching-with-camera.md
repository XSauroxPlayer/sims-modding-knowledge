---
title: FadeType (objects fading when zooming/approaching with camera)
url: https://modthesims.info/showthread.php?t=548283
fetched: 2026-10-28
game: ts3
tags: object-creation, modl, rcol, camera, fade
status: community-reported
author: Arsil
---
# MODL FadeType and CustomFadeDistance (MTS Modding Discussion, Feb 2015)

Arsil (single post, experiments; credits a cmomoney post). Synthesis: `topics/object-creation.md`.

- MODL (chunk entry 0 under the RCOL block) has `FadeType` and `CustomFadeDistance`; they make an object fade
  as the camera approaches (used for a walk-in tent).
- `FadeType` 0 = no fade. 1 and 2 fade subtly (fully only when the camera is inside); 3 fades much earlier and makes
  the object vanish completely. 4, 5, 8 and `0xFFFFFFFF` behave like 0: valid values look like 0-3 (observed, not a
  spec). Test used `CustomFadeDistance` 5.
