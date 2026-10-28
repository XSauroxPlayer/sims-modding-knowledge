---
title: Best methods on debugging script mods
url: https://modthesims.info/showthread.php?t=633012
fetched: 2026-10-28
game: ts3
tags: script-modding, debugging, csharp
status: community-reported
author: Lyralei, gamefreak130, Battery
---
# Debugging TS3 script mods (MTS Modding Discussion, Sep 2019)

Lyralei, gamefreak130, Battery. Synthesis: `topics/script-modding.md`.

- Preload code: schedule an **alarm** a few Sim-minutes later that shows a notification with values set during
  preload; where alarms do not run (application startup) use an `OnWorldLoadFinished` handler (gamefreak130).
- Show caught exceptions in the game's script error window:
  `((IScriptErrorWindow)AppDomain.CurrentDomain.GetData("ScriptErrorWindow")).DisplayScriptError(null, ex)`,
  fallback `new ScriptError(null, ex, 0).WriteMiniScriptError()` writes the XML error log (Battery, from MTS
  t=491875). UI-time errors may only reach the text/XML file.
- Keep pure logic separate and test it in a console program; bisect by enabling methods one at a time.
- An MTS download that re-enables EA's script error window still worked in 2019 (one window per error).
