# How STEP1495X was reached

**PS3 port project led, tested, and maintained by DeepDarkDaddy (2026).** These STEP designations describe collaborative PS3 compatibility work, not authorship of the original Genesis Plus GX or PUNCHiUM emulator code.

The PS3 big-endian port initially ran with malformed sprites, stray tile graphics, and some broken sprite animations. Multiple targeted investigations isolated different layers:

- **STEP1489A**: best previous core after PUNCHiUM decoding and graphics byte-order fixes.
- **STEP1493A**: scaler byte-address experiment, **rejected** after visual regression. Preserve the original `out^1` behavior.
- **STEP1494**: DMA diagnostics; no split-boundary issue confirmed.
- **STEP1495G/H**: DMA command-list guard, visually unchanged; **not promoted**.
- **STEP1495J/K**: mapping traces; 640 samples, no changing checksums for identical exact sprite-record inputs.
- **STEP1495L/M**: corrected `punchium_sprite_stop()` last-sprite link byte, **all previously observed visual issues reported fixed**.
- **STEP1495N**: new core installed and hash verified; previous STEP1489A protected.

- **STEP1495V/W**: telemetry showed hundreds of sound commands and nonzero PCM but implausible sample lengths and `type=00` entries.
- **STEP1495X/Y**: corrected PCM sample-table high-length/type fields in three reads (including looping samples); testers reported normal voices/effects and no high-pitched tone.
- **STEP1495Z**: protected STEP1495X and permanently installed the audio+graphics-fixed SELF; SHA256 verified while STEP1495L and STEP1489A remained protected.

The final public source carries **STEP1495X** (including STEP1495L graphics correction), without temporary tracing/guard/rejected experiments.

The expanded sprite-list termination branch was deliberately *not* modified in STEP1495L, since it was not exercised in the sampled cases. Further alterations should be separately tested.
