# IMGenius v0.7.9 Beta

**Release assets:** Native Windows, Arch Linux, and Debian/Ubuntu installers, plus publisher-signed update metadata and SHA-256 checksums.

IMGenius v0.7.9 focuses on more reliable local character chats, character-card editing/import, optional image backends, and clear separation between development and signed release builds.

**Reviewed source commit:** `a3ec67c8993573f587a35c25e04b7b4c99dc0753` ([development PR #26](https://github.com/IMGenius-Dev/IMGenius/pull/26)).

## v0.7.9 features and fixes

- **Character cards:** The Character tab shows **Description**, not Personality. Downloaded Character Card V2/V3 and Chub profiles keep description and personality in separate editor inputs. Additional PNG metadata chunk variants are recognized. Images with no embedded card data offer portrait-only attachment instead of overwriting profile fields.
- **AI-assisted character creation:** The editor’s **Generate with AI** button opens an on-demand name/gender/description dialog and uses the selected local Ollama model to draft profile text, persona, scenario, greetings, prompts and tags. Review edits before saving.
- **Chat reliability:** Stopping an Ollama stream or encountering a transport error keeps already generated text where possible. Failed regeneration preserves the previous message and successful replacement uses an atomic database update.
- **Alternative greetings:** Author, import and export alternative first messages. Switch between them beneath the initial bubble without inserting sequential roleplay responses.
- **Responsive chat:** Better narrow-window Chat Controls, wrapped settings, and a compact one-row layout for Regenerate, Continue, Scene image and Stop.
- **Optional ComfyUI:** Detect common local installations, reuse running ComfyUI or start/wait for an installed one; bypass startup when it is absent so chat-only use remains possible.
- **Personalization:** Additional dark, pastel, Catppuccin, galaxy, and Pride-inspired themes.
- **Issue reporting:** An explicit **Report an issue** action collects a subject, description, optional remembered username and selected screenshots. Email delivery is available **only after** the operator deploys the separate private HTTPS/SMTP issue relay.
- **Release tracking:** Developer packages and source checkouts visibly show development status; a signed public package with the same base version is considered a newer release than its development counterpart.

## Supported installers

| System | Asset filename |
| --- | --- |
| Windows | `IMGenius-Setup-v0.7.9.exe` |
| Arch Linux | `imgenius-0.7.9-1-x86_64.pkg.tar.zst` |
| Debian / Ubuntu | `imgenius_0.7.9_amd64.deb` |

No Ollama models, ComfyUI weights, personal characters, logs, or user images are bundled. A separately installed Ollama model is required for chat; ComfyUI is optional for image generation. Back up important application data before upgrading.

## Release integrity

The development repo's `native-tester-installers.yml` builds both development-marked and release-marked installers from the reviewed source. This release distributes **release-marked installers** with checksums and a detached Ed25519 manifest signature. The signing private key stays offline; the corresponding trusted public key is pinned in the app.

The publishing workflow validates the signed manifest, exact asset filenames, and all file hashes before publication. Use the installers attached to the official GitHub Release; verified native updates are available through the app's update system.
