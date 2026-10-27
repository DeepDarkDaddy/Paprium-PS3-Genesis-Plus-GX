# Source manifest

**Maintainer of this PS3 port and source release: DeepDarkDaddy.** Original upstream authorship remains intact.

Seven **complete replacement files** below were extracted from the user-provided STEP1489A source evidence (`STEP1495B`) and the exact STEP1495X corrected header. Their hashes are checked by `scripts/verify_source.py`.

| Repo overlay | SHA256 |
| --- | --- |
| `core/cart_hw/punchium.h` | `522D4E65B3C325109ACF0784341E3603ACC37A691DAC8CFB2EF6087508F47F2F` |
| `core/cart_hw/md_cart.c` | `24663A7B62002E7A0E99ACF0F6EA239BAF1FB405E7AC1946ED279E5B31D4CA55` |
| `core/vdp_ctrl.c` | `1176751265B03498DB8B720203BA8D530C553A5605CA16A2CC2801B855D8BD22` |
| `core/vdp_render.c` | `EFCF0527BE074354C81C2BA91E18D7DB8C42395778C1E64E3D6D970D81D58FAA` |
| `libretro/libretro.c` | `1C2A03F566EB9AB79F3ADFA1E7059C06847E09D54DB495C4342CC5CACDD588A5` |
| `libretro/libretro_core_options.h` | `14C30187486C9FF59442DF8865E1C9EF0A3CE1F724A959D669102B487BFE8C95` |
| `libretro/libretro_core_options_intl.h` | `F2E19E6BE557D607A120CDEA50BE037C3251F94B3F2B81082EDFC8AF2BEF3A31` |

All other source files required for compilation come from the full baseline checkout. The seven-file overlay is **not** independently buildable. Preserve the original project history and license when creating a complete tree.

The STEP1495X header preserves STEP1495L sprite-link fix and applies three PCM sample-table field reads. Both patch files are retained separately under `patches/`.
