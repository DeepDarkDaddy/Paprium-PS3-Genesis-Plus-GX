# Programs and prerequisites

## Required to work with source

| Program | Purpose | Where to obtain |
| --- | --- | --- |
| **Git** | Get the upstream PUNCHiUM repository and manage forks | https://git-scm.com/ |
| **Python 3** | Optional helper scripts and legacy descriptor-repair helper | https://www.python.org/ |
| **PowerShell 5.1+** | Included Windows scripts | Built into Windows; PowerShell 7 also supported for most operations |
| **GNU make** | Build the core with `Makefile.libretro` | MSYS2/MinGW or a Unix toolchain; https://www.msys2.org/ |
| **PS3DEV / PSL1GHT SDK** | PPU cross compiler, headers, link libs and tools | https://github.com/ps3dev/ps3dev and https://github.com/ps3dev/PSL1GHT |
| **PS3 PowerPC compiler/binutils** | `ppu-gcc`, `ppu-g++`, `ppu-ar` or compatible `powerpc64-ps3-elf-*` | Your PS3DEV/PSDK toolchain |
| **Compatible RetroArch PS3 frontend sources** | Link Genesis Plus GX static `.a` into a usable frontend/SELF | https://github.com/libretro/RetroArch or your known-compatible PS3 fork |
| **SELF packaging tool** | Convert linked executable into suitable PS3 SELF for testing | Available as part of compatible PS3 development environment |
| **RPCS3 or supported PS3 homebrew environment** | Test results on supported runtime | https://rpcs3.net/ |

## Known tested developer environment (not supplied here)

- Windows with the legacy `C:\PSDK3v2\ps3dev\ppu\bin` toolchain; `powerpc64-ps3-elf-gcc.exe`, `powerpc64-ps3-elf-g++.exe`, `powerpc64-ps3-elf-ar.exe`, `powerpc64-ps3-elf-objdump.exe`.
- GNU Make at `C:\devkitPro\msys2\usr\bin\make.exe`.
- Python 3.12.x.
- SELF packager at `C:\PSDK3v2\host-win32\bin\make_fself.exe`.
- An existing compatible PS3 RetroArch frontend and verified linker arguments.

**Important:** Toolchains with different GCC/binutils versions can produce different descriptor/TOC layouts. The historical successful linking required a specific strict function-descriptor/TOC repair step. This kit does **not** pretend that an ordinary `make` automatically produces the byte-identical, tested `.SELF`.

## Licenses and assets

The tools are downloaded/installed separately. **Do not** commit a Sony SDK, licensed PS3 keys, ROMs, BIOS images, game data, music folders, or cached private files. The source fork itself imposes non-commercial distribution and complete-source conditions. See `LICENSE-AND-REDISTRIBUTION.md`.
