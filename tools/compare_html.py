#!/usr/bin/env python3
"""Offline-only static decoder/comparator for the two observed HTML wrappers.

Does not evaluate JavaScript, execute HTML, or perform network requests.
"""
import argparse
import base64
import codecs
import difflib
import hashlib
import re
from pathlib import Path
from urllib.parse import unquote


def decode_capture(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    wrapper = re.search(r"const\s+\w+\s*=\s*`(.*?)`;", raw, re.S)
    if not wrapper:
        raise ValueError(f"Expected wrapper not found: {path}")
    rot13 = codecs.decode(wrapper.group(1), "rot_13")
    payload = re.search(r"atob\(['\"]([^'\"]+)['\"]\)", rot13)
    if not payload:
        raise ValueError(f"Expected atob payload not found: {path}")
    return unquote(base64.b64decode(payload.group(1), validate=True).decode("utf-8"))


def values(html: str, key: str) -> list[str]:
    return sorted(set(re.findall(r"(?:[?&]|&amp;)" + re.escape(key) + r"=([^&\"\s]+)", html)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sample_a", type=Path)
    parser.add_argument("sample_b", type=Path)
    args = parser.parse_args()
    a, b = decode_capture(args.sample_a), decode_capture(args.sample_b)
    for name, content in (("A", a), ("B", b)):
        print(f"Sample {name}: {len(content)} characters; SHA-256={hashlib.sha256(content.encode()).hexdigest()}")
        print("  Provider paths:", sorted(set(re.findall(r"/provider/([A-Z]+)", content))))
    print(f"Character-sequence similarity: {difflib.SequenceMatcher(None, a, b, autojunk=False).ratio():.2%}")
    for key in ("conversation", "tid", "pid", "tag"):
        av, bv = values(a, key), values(b, key)
        print(f"{key}: matching={av == bv}; count_A={len(av)}; count_B={len(bv)}")
    print("No scripts or HTML were executed.")


if __name__ == "__main__":
    main()
