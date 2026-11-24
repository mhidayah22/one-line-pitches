"""A Day of One-Line Pitches — entry program.

Writes the one-sentence pitch to entry.txt. The grader runs this program
with `python3 -P -s main.py` in a sandbox whose working directory is
read-only, so the output directory is resolved in this order and never
defaults to a bare relative path:

1. an explicit first argument (a directory),
2. the MAKEFUN_OUTPUT_DIR environment variable,
3. /output when that directory exists,
4. the current working directory, for a local run.
"""

import os
import sys
from pathlib import Path

PITCH = (
    "Don't take my word for it: describe your app idea in plain words, "
    "let an AI agent on make.fun build the first version, and judge it "
    "yourself by tapping on it today for free, no code needed."
)

FILE_NAME = "entry.txt"
MAX_CHARS = 240


def pick_output_dir(argv):
    """Return the directory the pitch file goes in."""
    if len(argv) > 1 and argv[1]:
        return Path(argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path.cwd()


def main(argv):
    if not 1 <= len(PITCH) <= MAX_CHARS:
        raise SystemExit(
            "pitch must be 1 to 240 characters, got %d" % len(PITCH)
        )
    out_dir = pick_output_dir(argv)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / FILE_NAME
    target.write_text(PITCH + "\n", encoding="utf-8")
    print("wrote %s (%d characters)" % (target, len(PITCH)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
