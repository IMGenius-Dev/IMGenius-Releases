"""CI verifier for IMGenius signed release packages (v0.7.3 and newer)."""
import base64
import hashlib
import json
import os
from pathlib import Path
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

root, tag = Path(sys.argv[1]), sys.argv[2]
pub = os.environ.get('IMGENIUS_SIGNING_PUBLIC_KEY', '').strip()
if not pub:
    raise SystemExit('No publisher signing public key is configured; rejecting unsigned release.')
key = base64.b64decode(pub, validate=True)
if len(key) != 32:
    raise SystemExit('Invalid publisher public key size')
manifest = (root / 'release-manifest.json').read_bytes()
signature = base64.b64decode((root / 'release-manifest.sig').read_bytes().strip(), validate=True)
Ed25519PublicKey.from_public_bytes(key).verify(signature, manifest)
data = json.loads(manifest.decode('utf-8'))
if data.get('schema') != 1 or data.get('version') != tag[1:] or data.get('channel') not in ('stable', 'beta'):
    raise SystemExit('Signed release manifest is invalid')
assets = data.get('assets')
if not isinstance(assets, dict) or not assets:
    raise SystemExit('Signed installer list missing')
for platform, entry in assets.items():
    if platform not in ('windows', 'arch', 'debian') or not isinstance(entry, dict):
        raise SystemExit('Unknown signed platform')
    expected = {
        'windows': f'IMGenius-Setup-{tag}.exe',
        'arch': f'imgenius-{tag[1:]}-1-x86_64.pkg.tar.zst',
        'debian': f'imgenius_{tag[1:]}_amd64.deb',
    }[platform]
    if entry.get('name') != expected:
        raise SystemExit('Signed filename mismatch')
    source = root / expected
    raw = source.read_bytes()
    if entry.get('size') != len(raw) or entry.get('sha256') != hashlib.sha256(raw).hexdigest():
        raise SystemExit('Signed file hash or size mismatch')
print('Signed release manifest verified for', tag, 'with', len(assets), 'native installers')
