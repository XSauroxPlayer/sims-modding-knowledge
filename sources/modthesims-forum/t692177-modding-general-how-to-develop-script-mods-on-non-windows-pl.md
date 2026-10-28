---
title: How to develop script mods on non-Windows platforms (+ things that might also be useful for SharpDevelop)
url: https://modthesims.info/showthread.php?t=692177
fetched: 2026-10-28
game: ts3
tags: script-modding, mono, linux, monodevelop, monopatcher
status: community-reported
author: Destrospean
---
# Script mods on Linux (MTS Tutorials, Destrospean, Jul 2025)

Synthesis: `topics/script-modding.md`.

- TS3 runs scripts on **Mono targeting .NET 2.0**; MonoDevelop 5.7 is the last IDE able to build for .NET 2.0. Setup:
  Distrobox `ubuntu:xenial` container with Mono 3.12 and MonoDevelop 5.7 pinned (`apt-mark hold`).
- **Mono Patcher** (a community runtime method-patching framework for TS3) needs a C# 5.0 compatibility patch to build
  with MonoDevelop 5.7 or SharpDevelop (patch attached in the thread, not downloaded).
- s3pe, TSRW, Milkshape and the Tashiketh/CmarNYC tools run under Wine/Proton; ILSpy has a cross-platform build.
