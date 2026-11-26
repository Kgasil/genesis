"""Verify the existing Genesis Mini release without executing its contents."""
from pathlib import Path
from hashlib import sha256
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ZIP = ROOT / "downloads/Genesis-Mini-v0.1.0-install.zip"
EXPECTED = {"manifest.json", "popup.html", "style.css", "core.js", "ui.js"}
EXPECTED_SHA256 = "654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4"

def require(condition, message):
    if not condition:
        raise SystemExit(message)

def main():
    require(sha256(ZIP.read_bytes()).hexdigest() == EXPECTED_SHA256,
            "Unexpected archive SHA-256; stop and investigate.")
    with zipfile.ZipFile(ZIP) as archive:
        infos = archive.infolist()
        require(len(infos) == len(EXPECTED) and set(archive.namelist()) == EXPECTED,
                "Unexpected, duplicate or missing archive entries.")
        require(all(not i.is_dir() and not (i.flag_bits & 1) for i in infos),
                "Unexpected directory or encrypted entry.")
        require(archive.testzip() is None, "Archive CRC failed.")
        for name in sorted(EXPECTED):
            require(archive.read(name) == (ROOT / "extension" / name).read_bytes(),
                    f"Source mismatch: {name}")
        manifest = json.loads(archive.read("manifest.json"))
        require(manifest["manifest_version"] == 3 and manifest["version"] == "0.1.0",
                "Unexpected manifest version.")
        require(set(manifest) == {"manifest_version", "name", "version", "description", "action"},
                "Unexpected manifest capability; review before distribution.")
        require(manifest["action"]["default_popup"] == "popup.html", "Unexpected entry point.")
    print("Genesis Mini 0.1.0: SHA-256, exact entries, CRC, source parity and manifest verified.")
    print("Integrity check only; this is not an antivirus scan or installation approval.")

if __name__ == "__main__":
    main()
