---
title: Simlogical - Creating an Object Start to Finish (index) and 4-channel object upgrade (orangemittens)
url: http://www.simlogical.com/ContentUploadsRemote/uploads/830/index.htm
fetched: 2026-10-28
game: ts3
tags: object-creation, textures, slots, mesh, tools
status: community-reported
author: orangemittens
---
# orangemittens: object creation start to finish; upgrading to 4 channels

Pages: http://www.simlogical.com/ContentUploadsRemote/uploads/830/index.htm (index of a 21-part tutorial; the parts are inside `OM_Tut.7z`, not downloaded per the
no-binaries rule), http://www.simlogical.com/ContentUploadsRemote/uploads/2241/ (4-channel upgrade, read in full), http://www.simlogical.com/ContentUploadsRemote/uploads/948/ (Pose Pack Creator, tool page).

## Start to finish (pipeline overview only)
- s3oc clone -> s3pe export mesh resources -> MilkShape mesh + UV -> Blender bakes multiplier, mask, specular ->
  Blender makes the low MLOD and **edits/adds slots** (part 19) -> MilkShape readies meshes for s3pe import ->
  Texture Tweaker 3 (3T) assembles images, enables channels, default pattern, preview.
- Tools credited: s3oc/s3pe (Inge and Peter Jones), s3pe wrappers (Atavera), Blender add-ons (Cmomoney), MilkShape
  plugins (Wes Howe), Texture Tweaker 3 (Inge Jones).

## 4-channel upgrade with Texture Tweaker 3
- Open the cloned package in 3T, "Upgrade to 4 channel CASTable".
- The mask is still 3-channel: channels 1-3 are R, G, B of the mask; the **4th channel is the mask alpha**. Paint the
  4th area another colour (e.g. yellow) for the RGB part, build an alpha that is white only on that area (black
  elsewhere -> transparent), combine, save **DXT5**, import to overwrite in 3T.
- Then set pattern tiling to match the image sizes for each preset.
- Use the current 3T; older versions unsupported.

## Relevance
- Mask channel layout (RGB + A as 4th) matters when mapping TS2 recolour regions to TS3 channels.
