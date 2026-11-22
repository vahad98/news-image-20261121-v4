"""Entry point: render the front page and write entry.png.

Reads $MAKEFUN_OUTPUT_DIR; falls back to the current working directory
when the variable is unset or empty.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from compose import render, total_stories


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    img = render()
    img.save(path, optimize=True)
    print(f"wrote {path} ({img.size[0]}x{img.size[1]}, {total_stories()} stories)")


if __name__ == "__main__":
    main()
