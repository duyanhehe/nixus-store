"""Paths for the code-pack tests of nixus.gate, and server/ of Nixus AI on sys.path.

The Gate plugin runs INSIDE a Nixus AI server and calls its hub (`mcp_hub.tra_loi_jsonrpc(gate=...)`, Nixus
0.440.0), so its tests need a Nixus AI checkout next to this repo. CI clones it; locally point NIXUS_OS_DIR at
yours (default: ../nixusai next to this repo).

    NIXUS_OS_DIR=/path/to/nixusai python tests/nixus.gate/test_gate.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "nixus.gate"
ROOT = Path(os.environ.get("NIXUS_OS_DIR") or (STORE.parent / "nixusai")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "chat_bridge.py").is_file():
    raise SystemExit(f"Nixus AI 0.440.0+ checkout not found at {ROOT} (set NIXUS_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
