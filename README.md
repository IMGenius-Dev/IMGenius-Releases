# IMGenius — AI Character Chat & Roleplay for Windows and Linux

**IMGenius** is a local-first AI roleplay and character-chat desktop application. Create original characters, have companion-style conversations, and build interactive stories using local **Ollama** language models. Optional **ComfyUI** integration adds image-generation features.

**[Explore the IMGenius website](https://imgenius-dev.github.io/IMGenius-Releases/)** · **[View features](https://imgenius-dev.github.io/IMGenius-Releases/features.html)** · **[Get official beta downloads](https://github.com/IMGenius-Dev/IMGenius-Releases/releases)**

Search topics: AI character chat, roleplay chatbot, character creator, AI companion chat, local AI, AI storytelling, Ollama, Windows, Linux.

## Official beta downloads

This is the **public releases and update-feed repository** for **IMGenius**, a local AI character-chat and optional image-generation desktop studio for Windows and Linux.

**[Download the latest published beta](https://github.com/IMGenius-Dev/IMGenius-Releases/releases)**

> **Release status:** **v0.7.9 beta is published** with verified Windows, Arch Linux, and Debian/Ubuntu installers. [Download v0.7.9](https://github.com/IMGenius-Dev/IMGenius-Releases/releases/tag/v0.7.9). This GitHub Releases page is the source of truth for official downloads.

## Choose your platform

Download files **from a release's Assets list**. Use the version printed on that specific release page.

| Platform | Published asset pattern | Install |
|---|---|---|
| Windows 10/11 | `IMGenius-Setup-vVERSION.exe` | Run the native Windows bootstrap installer |
| Arch Linux | `imgenius-VERSION-1-x86_64.pkg.tar.zst` | `sudo pacman -U ./imgenius-VERSION-1-x86_64.pkg.tar.zst` |
| Debian / Ubuntu | `imgenius_VERSION_amd64.deb` | `sudo apt install ./imgenius_VERSION_amd64.deb` |
| Other Linux | `IMGenius-vVERSION-linux-portable.tar.gz`, **only if attached** | Extract and follow that release's instructions |

The Windows bootstrapper is a native executable that prepares the IMGenius app and its Python/Qt runtime; it is **not** a pre-bundled standalone Qt executable. Linux packages use the system package manager for the application and separate user-local setup for optional AI dependencies.

**No Ollama language models, ComfyUI image checkpoints, character cards, chat logs, custom artwork, or private user data are included in a release.** You install the models you wish to use. Chat requires local Ollama and a model. ComfyUI is optional for image generation.

## What's new in v0.7.9

The development branch contains:

- More reliable Chat Controls layout on narrow windows, plus compact, single-row **Regenerate / Continue / Scene image / Stop** controls.
- Support for multiple **alternative first messages** in character cards and in the editor; arrows under the first chat message switch between choices without adding additional messages.
- Improved optional ComfyUI detection and startup: reuse running local instances, launch detected installations, wait on the splash for readiness, or skip ComfyUI startup when none is installed.
- Expanded dark, light, Catppuccin, galaxy, and Pride theme choices.
- Improved message preservation when chat generation stops or errors.
- AI-assisted character-card drafting from name, gender and a short description.
- Separate imported Description and Personality fields, improved V2 PNG metadata handling, and on-demand support issue reporting (relay deployment required).
- Developer builds clearly labeled separately from signed release builds, including same-version update precedence.
- Additional model browsing and general UI refinements.

See the [v0.7.9 release notes](https://github.com/IMGenius-Dev/IMGenius-Releases/releases/tag/v0.7.9) for the complete release contents and signed installer attachments.

## Updates and security

IMGenius checks the published GitHub Releases feed to notify users of newer beta versions. For supported installed Windows, Arch, and Debian systems, **automatic downloads and installation on exit are allowed only for properly Ed25519-signed releases** that match the trusted publisher public key embedded in the client.

A valid automatic update needs `release-manifest.json`, `release-manifest.sig`, and installer binaries whose SHA-256 and sizes match the signed manifest. Unsigned releases—including older releases published before that mechanism—can only be handled manually; a checksums file alone does **not** prove publisher identity. Development clones and portable/source installations do not receive automatic package-manager upgrades.

Before installing, verify that the release comes from this repository and review any security warnings. Do not bypass unexpected OS protections merely because a file has an IMGenius filename.

## For maintainers: publishing a beta safely

The **private** development repository is `IMGenius-Dev/IMGenius`. Development CI runs Windows/Linux tests and produces developer and release-marked candidate artifacts. Public beta packages are published separately, after cryptographic verification and approval.

For a new version (for example, `v0.7.9`):

1. Verify the intended development commit, application version, CI results, and release notes. Download the matching **release-marked** Windows, Arch, and Debian candidate artifacts from the private development workflow (not the separate development-marked packages).
2. Smoke-test the packages on their supported target systems and scan packages for user files/secrets. Verify asset names and create `SHA256SUMS.txt` for the final installer bytes.
3. On a trusted offline machine holding the project's existing Ed25519 **private** publisher key, sign the release manifest using the development repository's `scripts/sign-release.py`. Never generate a replacement key casually, never commit the private key, and never upload it to GitHub.
4. Stage the actual reviewed installers under `release-assets/vVERSION/`, alongside `RELEASE_NOTES.md`, `SHA256SUMS.txt`, `release-manifest.json`, and `release-manifest.sig`. The Windows installer can be staged in numbered binary parts where required by the connector's blob-size limit.
5. Verify the pinned publisher public key used by clients matches the key used to sign. Only after everything passes, commit the `release-assets/vVERSION/PUBLISH` marker to `main`. The `publish.yml` workflow validates the hashes and signature before creating the public prerelease and uploading the referenced assets.
6. Verify the resulting GitHub Release page, **all** attachment names and download checksums, signed metadata, and the updater's published feed response. Never advertise the new version before this check passes.

Release publishing is deliberately fail-closed: missing assets, mismatched hashes, wrong signing keys, and invalid manifests must prevent promotion to a public download.

## Privacy and support

This public repository distributes approved installers and the update feed **only**. Never upload local characters, conversations, private images, model weights, API credentials, signing keys, development databases, or other user content.

If you encounter a problem, include the IMGenius version, OS, installer type, reproducible steps, and sanitized logs/screenshots. For ComfyUI startup problems, check the local application's `logs/comfyui.log`; chat-only installations do not require ComfyUI.

The public **[Releases](https://github.com/IMGenius-Dev/IMGenius-Releases/releases)** page is the authoritative location for actual available versions and downloads.
