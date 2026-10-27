# DeepDarkDaddy — Paprium-compatible Genesis Plus GX PS3 port

**PS3 port lead / maintainer:** DeepDarkDaddy  
**Source release:** STEP1495X (2026)  
**Target:** PlayStation 3 / PS3 RetroArch Genesis Plus GX libretro core

### PS3-specific compatibility results

- Graphics and animation: corrected last-sprite link-byte handling for PS3 big-endian layout (`STEP1495L`; `0xB02` to `0xB03`).
- PCM samples, impact sounds and character voices: corrected three playback metadata reads (`STEP1495X`, type at `+4`, length-high byte at `+5`, including looping samples).
- Runtime testing, verification, and source-release preparation led by **DeepDarkDaddy**.

The working STEP1495X PS3 SELF reference SHA256 is
`D97AE11C92C59D3570DA1B9BBEF85BE484EB9CEE213F69F1F22B88FFAEEBB1D6`.

This file credits work on the PS3 adaptation only. Original Genesis Plus GX/PUNCHiUM source, concepts, and copyrights belong to their respective authors. No endorsement by commercial game rights holders is implied. Refer to `LICENSE.txt`, `CREDITS.md`, `AUTHORS.md`, and `LICENSE-AND-REDISTRIBUTION.md`.
