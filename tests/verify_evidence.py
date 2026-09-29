#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "evidence" / "proof-manifest.json").read_text(encoding="utf-8"))
ACCEPT = json.loads((ROOT / "evidence" / "acceptance-summary.json").read_text(encoding="utf-8"))

OPT = ROOT / "artifacts" / "aster-no01-web-ready.glb"
RAW_IMG = ROOT / "assets" / "raw-browser.jpg"
OPT_IMG = ROOT / "assets" / "optimized-browser.jpg"
REJECTED_IMG = ROOT / "assets" / "rejected-181kb-browser.jpg"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    checks = [
        ("accepted web-ready GLB exists", OPT.is_file()),
        ("raw browser screenshot exists", RAW_IMG.is_file() and RAW_IMG.stat().st_size > 0),
        ("optimized browser screenshot exists", OPT_IMG.is_file() and OPT_IMG.stat().st_size > 0),
        ("rejected-candidate screenshot exists", REJECTED_IMG.is_file() and REJECTED_IMG.stat().st_size > 0),
        ("optimized size matches evidence", OPT.stat().st_size == MANIFEST["accepted_web_asset"]["bytes"] == 270360),
        ("optimized hash matches evidence", sha256(OPT) == MANIFEST["accepted_web_asset"]["sha256"]),
        ("source baseline metadata is frozen", MANIFEST["source_asset"]["bytes"] == 1091916 and MANIFEST["source_asset"]["sha256"] == "e30e4c13d8be5516e8437080d05b46a3c51bfc4fea06233f19e7723443c79a1f"),
        ("accepted reduction is frozen", MANIFEST["accepted_reduction_percent"] == 75.24 and MANIFEST["accepted_size_ratio"] == 4.04),
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
