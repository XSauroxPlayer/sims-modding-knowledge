---
title: Modding - General - Tutorial: Sims 3 Pure Scripting Modding (Q&A)
url: https://modthesims.info/showthread.php?t=424674
fetched: 2026-10-28
game: ts3
tags: script-modding, mscorlib, namespace, crash, visual-studio
status: community-reported
author: MTS thread participants (see the thread)
---
# Pure Scripting Modding Q&A (MTS Tutorials, 2010-2011)

Q&A for `sources/simswiki/tutorial-sims-3-pure-scripting-modding.md`. Synthesis: `topics/script-modding.md`.

- Custom-namespace crash: object classes outside an EA namespace crash to desktop when the object is created from
  buy mode (reported after Late Night). The exception is thrown in **unmanaged** code; cause unknown (twallan
  speculated the script class is used as a store lookup key). Static constructors are unrelated to it.
- Libraries are identical across base game and EPs at the same patch level; check the S3SA code version in s3pe
  (0.2.0.128 at the time).
- VS 2010's "Do not reference mscorlib" often did nothing; fix by editing the `.csproj` reference path to the game's
  mscorlib. A mod compiled against .NET's mscorlib happened to work for one user, but see t=434786 on why it is risky.
