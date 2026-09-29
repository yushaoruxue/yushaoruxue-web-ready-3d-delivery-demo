#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "evidence" / "proof-manifest.json").read_text(encoding="utf-8"))
ACCEPT = json.loads((ROOT / "evidence" / "acceptance-summary.json").read_text(encoding="utf-8"))
PUBLIC = json.loads((ROOT / "evidence" / "public-assets.json").read_text(encoding="utf-8"))

RAW_JPG = ROOT / "assets" / "raw-browser.jpg"
OPT_JPG = ROOT / "assets" / "optimized-browser.jpg"
REJECTED_JPG = ROOT / "assets" / "rejected-181kb-browser.jpg"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    checks = [
        ("all public browser images exist", RAW_JPG.is_file() and OPT_JPG.is_file() and REJECTED_JPG.is_file()),
        ("raw browser image hash matches", sha256(RAW_JPG) == PUBLIC["raw_browser"]["sha256"]),
        ("optimized browser image hash matches", sha256(OPT_JPG) == PUBLIC["optimized_browser"]["sha256"]),
        ("rejected browser image hash matches", sha256(REJECTED_JPG) == PUBLIC["rejected_browser"]["sha256"]),
        ("frozen GLB sizes match accepted evidence", MANIFEST["source_asset"]["bytes"] == 1091916 and MANIFEST["accepted_web_asset"]["bytes"] == 270360),
        ("accepted reduction and ratio recorded", MANIFEST["accepted_reduction_percent"] == 75.24 and MANIFEST["accepted_size_ratio"] == 4.04),
        ("smaller rejected candidate is recorded", MANIFEST["rejected_smaller_candidate"]["bytes"] == 181616 and bool(MANIFEST["rejected_smaller_candidate"]["reason"])),
        ("validator acceptance recorded", ACCEPT["raw"]["validator_errors"] == 0 and ACCEPT["raw"]["validator_warnings"] == 0 and ACCEPT["optimized"]["validator_errors"] == 0 and ACCEPT["optimized"]["validator_warnings"] == 0),
        ("browser acceptance recorded", ACCEPT["raw"]["browser_loaded"] and ACCEPT["raw"]["capture_ready"] and not ACCEPT["raw"]["model_error"] and ACCEPT["optimized"]["browser_loaded"] and ACCEPT["optimized"]["capture_ready"] and not ACCEPT["optimized"]["model_error"]),
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
