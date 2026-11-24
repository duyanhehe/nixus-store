"""Paths for the code-pack tests of nixus.facebook-monitor, and server/ of Nixus AI on sys.path.

The plugin in this pack runs INSIDE a Nixus AI server and imports its modules (`mcp_store`), so its tests need a
Nixus AI checkout next to this repo. CI clones it; locally point NIXUS_OS_DIR at yours (default: ../nixusai next
to this repo).

    NIXUS_OS_DIR=/path/to/nixusai python tests/nixus.facebook-monitor/test_fb_monitor.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "nixus.facebook-monitor"
ROOT = Path(os.environ.get("NIXUS_OS_DIR") or (STORE.parent / "nixusai")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "mcp_store.py").is_file():
    raise SystemExit(f"Nixus AI checkout not found at {ROOT} (set NIXUS_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
