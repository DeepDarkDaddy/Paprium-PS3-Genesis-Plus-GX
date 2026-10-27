# STEP1495X: corrected PUNCHiUM PCM SFX sample table

**PS3 port and runtime testing led by DeepDarkDaddy.** This describes the PS3-specific compatibility correction; the underlying sound emulation work is credited to the PUNCHiUM/Genesis Plus GX upstream projects.

## Symptom

With STEP1495L, graphics and external music were working, but voices and fighting effects were very faint beneath a continuous high-pitched tone during main gameplay.

## Diagnostic evidence

STEP1495V/W instrumentation recorded 743 SFX play commands, 116 sampled active-voice frames with nonzero PCM, and no observed out-of-ROM sample records. The sampled sound-table entries all showed playback `type=00` while sample lengths were implausibly large (often over a megabyte). This suggested the two adjacent metadata bytes were reversed.

## Correction relative to STEP1495L

For each 8-byte ROM SFX table entry:

- Byte `+4` is the sample playback type (containing depth and rate information).
- Byte `+5` is the high byte of the sample length.
- The low two sample-length bytes at `+6` and `+7` are unchanged.

Three source changes in `core/cart_hw/punchium.h` implement this in initial playback and loop restart. See `../patches/STEP1495X_PCM_sample_table_fields.patch`.

For example, recorded sound #120 changed from interpreted `type=0x00`, `size=0x210220` (2,163,232 bytes) to `type=0x21`, `size=0x0220` (544 bytes). The corresponding data is the same; only metadata interpretation changed.

## Validation

STEP1495X compiled, passed strict link/descriptor repair and packaging, and was tested in RPCS3. The tester reported the PCM issue was fixed in-game. STEP1495Z subsequently installed the known-good candidate while preserving STEP1495L and STEP1489A rollback cores.

Reference PS3 SELF SHA256: `D97AE11C92C59D3570DA1B9BBEF85BE484EB9CEE213F69F1F22B88FFAEEBB1D6`.

**No gain increase, CD music change, FM/PSG adjustment, or SAT correction reversal is included.** This is not a patch to the Paprium ROM, and no commercial audio data is redistributed.
