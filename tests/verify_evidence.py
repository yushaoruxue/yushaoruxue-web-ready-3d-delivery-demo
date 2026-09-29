#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "evidence" / "proof-manifest.json").read_text(encoding="utf-8"))
ACCEPT = json.loads((ROOT / "evidence" / "acceptance-summary.json").read_text(encoding="utf-8"))

RAW = ROOT / "artifacts" / "aster-no01-raw.glb"
OPT = ROOT / "artifacts" / "aster-no01-web-ready.glb"
RAW_PNG = ROOT / "assets" / "raw-browser.png"
OPT_PNG = ROOT / "assets" / "optimized-browser.png"
REJECTED_PNG = ROOT / "assets" / "rejected-181kb-browser.png"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    checks = [
        ("raw GLB exists", RAW.is_file()),
        ("optimized GLB exists", OPT.is_file()),
        ("all browser screenshots exist", RAW_PNG.is_file() and OPT_PNG.is_file() and REJECTED_PNG.is_file()),
        ("raw size matches evidence", RAW.stat().st_size == MANIFEST["source_asset"]["bytes"] == 1091916),
        ("optimized size matches evidence", OPT.stat().st_size == MANIFEST["accepted_web_asset"]["bytes"] == 270360),
        ("raw hash matches evidence", sha256(RAW) == MANIFEST["source_asset"]["sha256"]),
        ("optimized hash matches evidence", sha256(OPT) == MANIFEST["accepted_web_asset"]["sha256"]),
        ("accepted reduction recorded", MANIFEST["accepted_reduction_percent"] == 75.24),
        ("validator/browser acceptance recorded", ACCEPT["raw"]["validator_errors"] == 0 and ACCEPT["raw"]["validator_warnings"] == 0 and ACCEPT["optimized"]["validator_errors"] == 0 and ACCEPT["optimized"]["validator_warnings"] == 0 and ACCEPT["raw"]["browser_loaded"] and ACCEPT["optimized"]["browser_loaded"]),
        ("manual visual gate recorded PASS", ACCEPT["visual_review"]["status"] == "PASS"),
    ]
    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + " - " + name)
    print(f"{len(checks)-len(failed)}/{len(checks)} evidence checks PASS")
    if failed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
