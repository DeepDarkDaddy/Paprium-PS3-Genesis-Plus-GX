# Publish this completed checkout to GitHub

**Project maintainer / PS3 port lead: DeepDarkDaddy.** Suggested repository description: "Genesis Plus GX PUNCHiUM PS3 port — graphics and PCM/SFX corrections by DeepDarkDaddy (STEP1495X)."

This directory is the verified complete source checkout. It is intended to be the **repository root**, not a patch-only ZIP.

1. Run `python scripts/verify_source.py` and confirm the expected hashes.
2. Review `LICENSE.txt`, `LICENSE-AND-REDISTRIBUTION.md`, [AUTHORS.md](../AUTHORS.md), [CREDITS.md](../CREDITS.md), contributor notices and `REQUIRED_SOFTWARE.md`.
3. Review all files for ROMs, game assets, SDK binaries, keys, user data, and proprietary dependencies before publication.
4. Create an empty GitHub repository and publish this directory:

```powershell
git init
git add .
git commit -m "Publish STEP1495X Paprium PS3 graphics and PCM source"
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/Paprium-PS3-Genesis-Plus-GX.git
git push -u origin main
```

To create a ZIP of the source tree again: `python scripts/create_publication_zip.py`.

**Not a byte-for-byte SELF build**: the original finalized SELF requires a compatible PS3 RetroArch frontend and specialized link/descriptor repair materials not in this source archive. Do not bundle the game ROM, external music files, prebuilt commercial assets, proprietary SDK tools or keys. Source distribution and compiled binary licensing remain subject to upstream non-commercial and complete-source terms.
