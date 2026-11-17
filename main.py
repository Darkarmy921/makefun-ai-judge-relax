# Weak Tea Light — ai-judge-relax-01 entry (Python 3.13, standard library only).
# Reads entry.txt from beside this script, checks it against its known
# sha256, and copies the exact bytes to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output), creating the output directory if needed. The copy's
# hash is checked again before exiting, so a run either writes the exact
# entry or fails loudly. No network, no randomness, no other input:
# two runs write identical bytes.
#
# Run it with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import sys

EXPECTED_SHA256 = "6f9b8e54af624f15c688756212ad08e0c333a901adc2d9ca25b9b5b9f7953940"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.txt")

    try:
        with open(source_path, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        return 1

    if sha256_hex(data) != EXPECTED_SHA256:
        print(
            "error: entry.txt sha256 mismatch: expected "
            f"{EXPECTED_SHA256}, got {sha256_hex(data)}",
            file=sys.stderr,
        )
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "entry.txt")

    try:
        with open(output_path, "wb") as f:
            f.write(data)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1

    try:
        with open(output_path, "rb") as f:
            written = f.read()
    except OSError as exc:
        print(f"error: cannot re-read {output_path}: {exc}", file=sys.stderr)
        return 1

    if sha256_hex(written) != EXPECTED_SHA256:
        print(
            "error: written entry.txt sha256 mismatch: expected "
            f"{EXPECTED_SHA256}, got {sha256_hex(written)}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
