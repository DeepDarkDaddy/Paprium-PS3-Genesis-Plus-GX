#!/usr/bin/env python3
"""Attempt a standard PSL1GHT static core build; does NOT install or produce a SELF."""
import argparse, subprocess, pathlib, sys, os, shutil
from verify_source import main as verify
ROOT=pathlib.Path(__file__).resolve().parent.parent

def main():
    parser=argparse.ArgumentParser(description='PS3 static libretro core build, not final SELF')
    parser.add_argument('--toolchain-bin', default=r'C:\PSDK3v2\ps3dev\ppu\bin')
    parser.add_argument('--make', default=r'C:\devkitPro\msys2\usr\bin\make.exe')
    args=parser.parse_args()
    verify()
    make=pathlib.Path(args.make)
    if not make.is_file():
        raise SystemExit(f'GNU make not found: {make}')
    tools={n:pathlib.Path(args.toolchain_bin)/('powerpc64-ps3-elf-'+n+'.exe') for n in ('gcc','g++','ar')}
    for name,path in tools.items():
        if not path.is_file():
            raise SystemExit(f'Missing PS3 cross compiler {name}: {path}')
    archive=ROOT/'genesis_plus_gx_libretro_psl1ght.a'
    if archive.exists():
        raise SystemExit(f'Refusing to overwrite existing archive: {archive}')
    cmd=[str(make),'-f','Makefile.libretro','platform=psl1ght',
         'CC='+str(tools['gcc']).replace('\\','/'),
         'CXX='+str(tools['g++']).replace('\\','/'),
         'AR='+str(tools['ar']).replace('\\','/'),'all']
    log=ROOT/'STEP1495X_static_core_build.log'
    if log.exists():
        raise SystemExit(f'Refusing to overwrite existing log: {log}')
    print('Building static library; command:',cmd, flush=True)
    with log.open('w', encoding='utf-8', errors='replace') as f:
        result=subprocess.run(cmd,cwd=ROOT, stdout=f,stderr=subprocess.STDOUT)
    if result.returncode:
        print('\n'.join(log.read_text(errors='replace').splitlines()[-60:]),file=sys.stderr)
        raise SystemExit(f'Build failed ({result.returncode}). See {log}')
    if not archive.is_file():
        raise SystemExit(f'Build ended without expected archive. See {log}')
    print('Static library built:',archive)
    print('This is NOT a loadable PS3 SELF; see BUILDING.md.')

if __name__=='__main__':
    main()
