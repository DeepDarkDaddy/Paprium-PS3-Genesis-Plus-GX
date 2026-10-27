# Paprium-capable Genesis Plus GX — PS3 STEP1495X

**PS3 port maintainer and project lead: DeepDarkDaddy**

This PS3 adaptation and its graphics/PCM compatibility fixes were developed, integrated, and tested through the **DeepDarkDaddy-led PS3 porting project**. The underlying Genesis Plus GX emulator and PUNCHiUM extensions are the work of their original authors; see [CREDITS.md](CREDITS.md) and [AUTHORS.md](AUTHORS.md).

**Complete source checkout of the Genesis Plus GX / PUNCHiUM libretro core, with tested PS3 graphics and PCM/SFX corrections.** This repository contains **no Paprium game ROM, audio, BIOS, or PS3 SDK binaries**.

## What's fixed

- **STEP1495L — Sprite graphics:** Corrected the last-sprite link byte in `punchium_sprite_stop()` (`0xB02` to `0xB03`) for big-endian PS3, removing misplaced graphics and bad sprite animations in the tested scenes.
- **STEP1495X — Voice/SFX audio:** Corrected the three PCM sound-table metadata reads (`type` at `+4`, length high byte at `+5`), including the looping voice path. In RPCS3 A/B testing this resolved the faint fighting effects and continuous high-pitched tone. External music was already working.

The **STEP1495X experimental SELF** was installed and SHA256-verified by STEP1495Z. An independent clean-room reproduction of that identical SELF has **not** been established.

### Known-good reference hashes

| Artifact | SHA256 |
| --- | --- |
| STEP1495X graphics+audio PS3 SELF | `D97AE11C92C59D3570DA1B9BBEF85BE484EB9CEE213F69F1F22B88FFAEEBB1D6` |
| `core/cart_hw/punchium.h` | `522D4E65B3C325109ACF0784341E3603ACC37A691DAC8CFB2EF6087508F47F2F` |
| STEP1495L graphics-only SELF (rollback) | `D057A65DA23FE1519E226795467B59AB5205A1E823B83833A47EFA7846853CEA` |

## Start here

Read [REQUIRED_SOFTWARE.md](REQUIRED_SOFTWARE.md) and [BUILDING.md](BUILDING.md). To verify the exact corrected files:

```powershell
python scripts/verify_source.py
```

To attempt a PSL1GHT **static libretro core archive** build on Windows using your configured PS3DEV toolchain:

```powershell
python scripts/build_static_core.py
```

This is not a one-command final PS3 SELF/PKG build. Linking against a compatible PS3 RetroArch frontend and the historical strict ELF descriptor/TOC repair inputs are separate prerequisites. See [BUILDING.md](BUILDING.md).

The seven verified corrected source files are in their regular paths and additionally under `source-overrides/` for auditing. The final patch diffs live in `patches/`. Other files are copied from the verified STEP1489A baseline tree, including the original upstream `LICENSE.txt`.

See [docs/FIX_HISTORY.md](docs/FIX_HISTORY.md), [docs/STEP1495X_AUDIO_FIX.md](docs/STEP1495X_AUDIO_FIX.md) and [docs/GITHUB_PUBLISHING.md](docs/GITHUB_PUBLISHING.md).

## License and attribution

**PS3 port / STEP1495L + STEP1495X compatibility work: DeepDarkDaddy.** This credit is additional to (not a replacement for) the upstream authorship and licensing notices.

Based on Genesis Plus GX and the PUNCHiUM extensions, by their respective authors. **Non-commercial and redistribution conditions apply**. Preserve original `LICENSE.txt` and individual source notices. See [LICENSE-AND-REDISTRIBUTION.md](LICENSE-AND-REDISTRIBUTION.md) and [CREDITS.md](CREDITS.md). This project is independent and does not include or license the commercial Paprium game.
