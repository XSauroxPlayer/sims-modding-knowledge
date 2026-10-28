---
title: Kilhian - Making Poses With Blender, parts I-IV (2012)
url: http://kilhian.blogspot.com/2012/07/making-poses-with-blender-part-i.html
fetched: 2026-10-28
game: ts3
tags: animation, clip, tools, blender, poses
status: community-reported
author: Kilhian
---
# Kilhian: Making poses with Blender (ClipTool era, 2012)

Pages: part I (kilhian.blogspot.com/2012/07/making-poses-with-blender-part-i.html), II and III
(kilhian.blogspot.co.uk/2012/07/...-part-ii.html, ...-part-iii.html), IV "For more complex poses & tips"
(kilhian.blogspot.co.uk/2012/10/making-poses-with-blender-part-iv-for.html). Beginner posing guide with long comment
threads; summary of the non-obvious points only.

## Key facts
- Workflow of the time: Blender 2.63 + S3PY animation plugin 1.52 (no plugin for 2.65 yet; later ClipTool 1.60 needs
  2.67b). S3PY Rig Tools ships with the animation plugin; missing Rig Tools panel = outdated plugin.
- **Import an existing animation file onto the rig before setting the keyframe**, for each rig separately, or "the
  pose simply won't work in game". Source of base clips: EA clips extracted with S3PE, or Kaleeko's pre-extracted
  files. (Matches ClipTool's "Base Clip" idea: the exporter reuses an existing clip as a
  template. Why the game rejects a clip exported without it is not explained.)
- Multi-rig poses: select a joint of the rig you are exporting, import the animation, key, export; then repeat for the
  other rig.
- Keep the working .blend and the exported clip per pose to edit later; downloaded poses can be re-edited by importing
  their clip.

## Relevance
- Low for tools that write CLIPs directly. The "needs an imported base clip" report is a hint that early
  exporters copied header data (actor table, events, source file name) from the template clip.
