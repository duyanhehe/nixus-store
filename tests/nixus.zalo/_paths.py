"""Paths for the code-pack tests of nixus.zalo, and server/ of Nixus AI on sys.path.

The plugins in this pack run INSIDE a Nixus AI server and import its modules (`zalo_cli`, `image_gen`,
`image_vision`, `conversations`), so their tests need a Nixus AI checkout next to this repo. CI clones it;
locally point NIXUS_OS_DIR at yours (default: ../nixusai next to this repo).

    NIXUS_OS_DIR=/path/to/nixusai python tests/nixus.zalo/test_zalo_read_images.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "nixus.zalo"
ROOT = Path(os.environ.get("NIXUS_OS_DIR") or (STORE.parent / "nixusai")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "zalo_cli.py").is_file():
    raise SystemExit(f"Nixus AI checkout not found at {ROOT} (set NIXUS_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
