# IMGenius v0.8.0 Beta

IMGenius v0.8.0 is a desktop beta for locally hosted AI character chat, story creation, character-card editing and optional image generation through separately installed Ollama and ComfyUI.

**Reviewed source commit:** `94f7d655507cec91f5bb9b67b079de257397ad23` ([development repository](https://github.com/IMGenius-Dev/IMGenius), private to authorized developers).  
**Release channel:** Beta (prerelease).  
**Platforms:** Windows 10/11 (x64), Arch Linux (x86_64), Debian/Ubuntu (amd64).

## Changes since v0.7.9

- **Report an Issue:** The app's header contains an explicit support-report form. A report sends only the entered title, description and up to three *selected* PNG/JPEG/WebP images to IMGenius's hosted support service over HTTPS. The service generates a ticket and a sequential anonymous identifier (`anon0001`, `anon0002`, etc.) and delivers the report to a dedicated Gmail support inbox. No editable username or application account is required. Sending a report requires Internet access. The receiving address and email-delivery credentials are not embedded in the desktop application.
- **AI-assisted character creation:** The on-demand **Generate with AI** dialog accepts a character name, gender, and brief description. The selected local Ollama model first attempts structured JSON. Models that cannot produce a complete card get a fallback that requests personality, scenario, sample dialogue and a greeting as shorter text responses. Existing editor fields are preserved if generation fails or is cancelled; completed drafts are for review and are not automatically saved. Results depend on the selected model.
- **Chat layout:** More reliable Conversations, chat and character-control panels across window widths. Controls can move into dedicated compact views, composer buttons fit narrower widths, and message bubbles/headers wrap instead of hiding behind controls.
- **Image storage and cleanup:** ComfyUI jobs use temporary preview output rather than creating duplicate permanent images. IMGenius retains generated images in its own gallery. A red, confirmation-protected **Delete all generated images** action also cleans qualifying older IMGenius-prefixed copies within the verified configured ComfyUI output folder, without deleting unrelated ComfyUI outputs.
- **Model settings:** Redundant ComfyUI model tab removed. ComfyUI configuration is available elsewhere in the app. The unreliable **Civitai.red** catalog is temporarily disabled until authenticated browsing and downloading can be supported.
- **Native desktop dialogs:** Image, portrait, character-card and other file-selection workflows use desktop-integrated file choosers where available. For KDE Plasma, `kdialog` is recommended.
- **Character library and cleanup:** Description is distinct from personality; imported character-card descriptions populate the correct editor field. Protected-card counts are derived from the local installation, without assuming users have a built-in 202-card catalog.
- **Version tracking:** Development builds are clearly marked. Release packages contain a release-channel marker, enabling signed public updates to supersede development packages of the same semantic version.

## Installers

| Platform | Asset |
| --- | --- |
| Windows 10/11 | `IMGenius-Setup-v0.8.0.exe` |
| Arch Linux | `imgenius-0.8.0-1-x86_64.pkg.tar.zst` |
| Debian / Ubuntu | `imgenius_0.8.0_amd64.deb` |

The Windows bootstrap installer sets up the Python/Qt runtime on first use. Linux packages install the application using their native package managers. A separately installed Ollama runtime and downloaded local language model are required for chat. ComfyUI and image models are optional.

No local chat databases, user portraits, conversation histories, custom character packs, downloaded models, or private keys are included in the release.

## Known limitations

- This is a beta. AI character generation quality and reliability vary by installed Ollama model; some models may still return no usable character text.
- Civitai.red model browsing is disabled for this release.
- Sending issue reports depends on the availability of the support backend and Gmail authorization. If submission fails, IMGenius displays an error instead of claiming successful delivery. The service operator must maintain its production OAuth authorization.
- Image generation requires a compatible running or installable local ComfyUI service.
- Installed user-created data should be backed up before upgrading. Destructive Settings actions require explicit confirmation.

## Release verification

The public release contains SHA-256 checksums, `release-manifest.json`, and a detached Ed25519 `release-manifest.sig`. They must correspond **exactly** to the release-marked Windows, Arch and Debian installers. The signing private key is held offline; its public verification key is pinned in IMGenius.

Only install assets attached to this official GitHub Release. A GitHub Actions development artifact, source commit, or file whose publisher signature has not been verified is **not** a signed public release.
