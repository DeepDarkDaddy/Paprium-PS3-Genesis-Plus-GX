#!/usr/bin/env python3
"""Read-only SHA256 checks on the seven complete STEP1495X source files."""
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {
    'core/cart_hw/punchium.h': '522D4E65B3C325109ACF0784341E3603ACC37A691DAC8CFB2EF6087508F47F2F',
    'core/cart_hw/md_cart.c': '24663A7B62002E7A0E99ACF0F6EA239BAF1FB405E7AC1946ED279E5B31D4CA55',
    'core/vdp_ctrl.c': '1176751265B03498DB8B720203BA8D530C553A5605CA16A2CC2801B855D8BD22',
    'core/vdp_render.c': 'EFCF0527BE074354C81C2BA91E18D7DB8C42395778C1E64E3D6D970D81D58FAA',
    'libretro/libretro.c': '1C2A03F566EB9AB79F3ADFA1E7059C06847E09D54DB495C4342CC5CACDD588A5',
    'libretro/libretro_core_options.h': '14C30187486C9FF59442DF8865E1C9EF0A3CE1F724A959D669102B487BFE8C95',
    'libretro/libretro_core_options_intl.h': 'F2E19E6BE557D607A120CDEA50BE037C3251F94B3F2B81082EDFC8AF2BEF3A31',
 }

def main():
    for name, target in EXPECTED.items():
        file = ROOT / name
        if not file.is_file():
            raise SystemExit(f'MISSING: {file}')
        got = hashlib.sha256(file.read_bytes()).hexdigest().upper()
        if got != target:
            raise SystemExit(f'HASH MISMATCH: {name} expected={target} actual={got}')
        print('[OK]', name)
    header=(ROOT/'core/cart_hw/punchium.h').read_text(encoding='utf-8', errors='replace')
    required=(
        'punchium_s.ram[0xB03 + (count-1)*8] = 0;',
        'size = (*(uint8_t *)(sfx + data*8 + 5) << 16)',
        'type = *(uint8_t *)(sfx + data*8 + 4);',
        'voice->size = (*(uint8 *)(sfx + voice->num*8 + 5) << 16)',
    )
    for anchor in required:
        if anchor not in header:
            raise SystemExit(f'MISSING required fix: {anchor}')
    if 'punchium_s.ram[0xB02 + (count-1)*8] = 0;' in header:
        raise SystemExit('Old SAT link byte reference remains')
    print('PASS: STEP1495X graphics and PCM fixes verified; no files changed.')

if __name__=='__main__':
    main()
