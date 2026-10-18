# IMGenius v0.7.2 (Closed Beta)

This is an **unsigned tester release** of IMGenius, a desktop AI chat and image-generation app for Windows and Linux. Do not treat it as a production-stable build. Windows, Arch, Debian and portable Linux package structures have been checked, and the private development repository passed cross-platform automated tests. Clean-machine installation, GPU initialization and live Civitai downloads require hands-on verification.

## What's new

- **Models → Civitai · SDXL / Illustrious**: browse and download compatible checkpoint and LoRA versions only.
- Model-version base architecture restrictions: `SDXL 1.0` and `Illustrious`. Pony, Flux, SD 1.5 and other models are excluded.
- Startup splash now **checks this public GitHub release feed** and waits for ComfyUI readiness.
- If ComfyUI fails to start, choose **Retry**, **Continue without images** or **Exit**.

## Download and install

- Windows: **IMGenius-Setup-v0.7.2.exe**. This is a bootstrap installer that may download required Python, ComfyUI and Ollama dependencies; it is not a self-contained frozen application.
- Arch: **imgenius-0.7.2-1-x86_64.pkg.tar.zst** (install with `sudo pacman -U ./imgenius-0.7.2-1-x86_64.pkg.tar.zst`).
- Debian/Ubuntu: **imgenius_0.7.2_amd64.deb** (install with `sudo apt install ./imgenius_0.7.2_amd64.deb`).
- Other Linux: **IMGenius-v0.7.2-linux-portable.tar.gz**.

Installer updates are intended to preserve user-created characters, conversations, settings, and generated images stored outside the application folder. Back up important data before beta updates.

## Update-check test

Launch an **existing v0.7.1 installation** with internet access and update channel `beta`. On startup it should report v0.7.2 and offer to open this release page. **This version only notifies. It does not automatically download or install an update.** When you're ready, download the matching installer and update through your platform's normal installation process.

## Integrity and security

Download only from this GitHub release. Compare each installer's SHA-256 digest with `SHA256SUMS.txt`. Binaries are **not yet code-signed**; checksums detect accidental mismatch but do not provide independent publisher authentication. Never disable antivirus/security protections merely to install an unexpected binary. Report installer, model-browser, startup or backend errors to the project developer.

Source development remains private; this public repository contains only distribution assets and release metadata.
