# IMGenius v0.7.8 Beta — Release Notes (Awaiting Publication)

**Release source:** [IMGenius development commit `0d97ffc505763b4579c16b6ea9f4c72b3221cd4a`](https://github.com/IMGenius-Dev/IMGenius/commit/0d97ffc505763b4579c16b6ea9f4c72b3221cd4a)

This document describes the **v0.7.8 beta release candidate**, not an already-published installer. Official downloads will appear under this repository's [GitHub Releases](https://github.com/IMGenius-Dev/IMGenius-Releases/releases) page only after the approved native packages, checksums, and signed manifest are staged and the publishing workflow succeeds.

## Changes since v0.7.7

- **Improved Character Editor:** choose **Generate with AI** to open a brief name/gender/description dialog. A selected local Ollama model drafts an editable character card with personality, scenario, example dialogue, initial message, alternate greetings, system prompt, and tags. Generated drafts are **not saved automatically**.
- **Alternative chat openings:** Character Card V2/V3 PNG and JSON imports preserve alternative first messages, which can be added, edited, removed, and switched using arrows below the first chat bubble.
- **More reliable chat history:** stopping Ollama generation or losing a streaming connection retains generated text; interrupted regeneration does not delete the previous message, and successful regeneration updates the reply transactionally.
- **Fixed responsive chat layout:** Chat Controls remain accessible in a narrow window. Regenerate, Continue, Scene image, and Stop use compact, left-aligned buttons above the message input.
- **Character descriptions kept separate from personality:** card previews show Description, not Personality. Chub/Character Card imports populate the distinct Description and Personality editor inputs. V2/V3 PNG import now recognizes additional metadata chunk variants and explains when an image has lost its embedded character data.
- **Optional ComfyUI startup:** detect installed local ComfyUI in configured/common directories, wait for a newly started backend to become ready, or skip the backend when absent. Local Ollama chats remain available without ComfyUI.
- **More visual themes and browsing refinements:** expanded color schemes, Pride and galaxy page backgrounds, local/native file picker integration, and model browsing refinements.
- **Issue reports:** a **Report an issue** button opens a user-controlled issue form with title, description, remembered optional username (`anon` by default), and selected image attachments. **Email delivery requires separately deployed HTTPS support relay and operator SMTP configuration; the relay is not deployed or included with the application.**
- **Development build labeling:** development/tester builds now identify themselves as such. The signed public release of the same base version takes precedence, allowing a supported native development installation to use `imgenius -U` when a newer signed public release becomes available.

## Installation

When published, choose the matching attachment from the v0.7.8 release:

| System | Installer |
| --- | --- |
| Windows 10/11 | `IMGenius-Setup-v0.7.8.exe` |
| Arch Linux | `imgenius-0.7.8-1-x86_64.pkg.tar.zst` |
| Debian / Ubuntu | `imgenius_0.7.8_amd64.deb` |

Native packages do not bundle Ollama model weights, ComfyUI checkpoints, user data, generated images, or personal character cards. Ollama and a locally available chat model are required for local chat. ComfyUI is optional for images.

Back up important application data before updating. Data is stored separately from the application package. Older imported cards may need to be re-imported to recover descriptions that an earlier importer put in Personality; the updater does not rewrite existing characters.

## Release verification and provenance

The successful [native installer CI run](https://github.com/IMGenius-Dev/IMGenius/actions/runs/39158738414) produced **development** Windows/Arch/Debian artifacts for source commit `0d97ffc505763b4579c16b6ea9f4c72b3221cd4a`.

**Do not publish those development-marked packages unchanged.** Approved public installers must be built from the reviewed source with `IMGENIUS_PACKAGE_CHANNEL=release`, tested as release packages, and hashed *after* packaging. The release packager must then generate `SHA256SUMS.txt` and sign `release-manifest.json` with the existing offline Ed25519 publisher private key. The matching `release-manifest.sig` and all verified installer assets must be staged before adding the `release-assets/v0.7.8/PUBLISH` marker. The publishing workflow fails closed if checksums, assets, signature, or trusted public key are missing or incorrect.

The public GitHub Release, not this staged note or an Actions artifact, is authoritative for which versions are actually downloadable.
