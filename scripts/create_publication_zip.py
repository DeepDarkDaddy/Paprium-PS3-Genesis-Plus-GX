#!/usr/bin/env python3
"""Make a fresh GitHub source ZIP, excluding builds and the ZIP itself."""
import zipfile, hashlib, pathlib, sys, os
from verify_source import main as verify
ROOT=pathlib.Path(__file__).resolve().parent.parent
EXCLUDE_DIRS={'.git','.vs','dist','build','__pycache__','roms','games','saves','states','music'}
EXCLUDE_EXT={'.elf','.self','.pkg','.a','.o','.d','.exe','.dll','.bin','.iso','.cue','.chd','.zip','.7z','.rar','.mp3','.wav','.ogg','.flac','.srm','.sav','.log'}

def main():
    verify()
    path=ROOT/'dist'/'Paprium_PS3_STEP1495X_Complete_GitHub_Source.zip'
    if path.exists():
        raise SystemExit(f'Refusing to overwrite: {path}')
    path.parent.mkdir(parents=True,exist_ok=True)
    entries=[]
    for src in ROOT.rglob('*'):
        if not src.is_file() or src.is_symlink():
            continue
        rel=src.relative_to(ROOT)
        if set(p.lower() for p in rel.parts[:-1]) & EXCLUDE_DIRS or src.suffix.lower() in EXCLUDE_EXT:
            continue
        entries.append((rel.as_posix(),src))
    with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name,src in sorted(entries):
            z.write(src,name)
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        if bad:
            raise SystemExit(f'Bad ZIP entry: {bad}')
        names=set(z.namelist())
        if 'core/cart_hw/punchium.h' not in names or 'LICENSE.txt' not in names:
            raise SystemExit('ZIP missing required source or license')
        if len(names)!=len(entries):
            raise SystemExit('ZIP entry count mismatch')
    print('Created:',path)
    print('SHA256:',hashlib.sha256(path.read_bytes()).hexdigest().upper())

if __name__=='__main__':
    main()
