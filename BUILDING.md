# Build instructions — STEP1495X source

**PS3 port / source release maintained by DeepDarkDaddy.** The build uses upstream Genesis Plus GX and PUNCHiUM source; preserve their notices and licensing. The verified seven source snapshots and STEP1495X SELF hashes are unchanged by this attribution update.

This folder is the **complete source checkout**: C sources, headers, `Makefile.libretro`, and the original upstream `LICENSE.txt`. No source export/merge step is needed.

## Needed tools

Read [REQUIRED_SOFTWARE.md](REQUIRED_SOFTWARE.md). The historical Windows environment had Python 3.12, GNU make, PS3DEV/PSL1GHT, and `powerpc64-ps3-elf-gcc/g++/ar` under `C:\PSDK3v2\ps3dev\ppu\bin`. Those tools are not redistributed.

### 1. Validate the exact final fixes

```powershell
python scripts/verify_source.py
```

The verifier checks seven complete files by SHA256, including the exact `punchium.h`, and asserts the SAT and PCM fixes.

### 2. Attempt a core static archive build

```powershell
python scripts/build_static_core.py --toolchain-bin "C:\PSDK3v2\ps3dev\ppu\bin" --make "C:\devkitPro\msys2\usr\bin\make.exe"
```

You can override those paths with CLI arguments. The helper invokes `Makefile.libretro` with `platform=psl1ght`. It requires the build toolchain and may need adjustments on other versions. The expected output is `genesis_plus_gx_libretro_psl1ght.a`, **not** a launchable SELF.

### 3. Linking a working PS3 SELF

The historical final STEP1495X build:

1. Compiled `md_cart.o` from the fully corrected `punchium.h` (STEP1495L sprite fix plus STEP1495X PCM table fix).
2. Replaced **only** `md_cart.o` in a pre-existing, known-good 83-member libretro static archive, retaining the other 82 objects.
3. Linked against a compatible PS3 RetroArch frontend with verified STEP1463 link arguments.
4. Applied a strict ELF import / function-descriptor / TOC relocation repair, refusing mismatched reference inputs.
5. Packaged a test SELF and verified it in RPCS3 before permanent promotion.

**This GitHub checkout does not include** the matching RetroArch frontend project, the 33-argument historical linker input, golden ELF reference objects, or all strict-repair inputs. Therefore this checkout is **not sufficient to reproduce the known-good SELF byte-for-byte**. Do not promise third parties a one-click build. Publishing those reproducibility dependencies is a separate task, subject to licensing.

No Paprium ROMs, external soundtrack files, audio blobs, BIOS, proprietary Sony toolchain, user configuration, or save data are included.
