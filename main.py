"""Write the Agent Motto Battle entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry is a single original motto line, written with no
trailing newline.
"""

import os

ENTRY = "Powered by your prompts, haunted by your typos."


def main():
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
