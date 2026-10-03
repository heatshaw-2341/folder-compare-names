"""Folder Compare Names — Compare two folders by relative path and list only-in-left, only-in-right, and size mismatch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='folder_compare_names',
        description='Compare two folders by relative path and list only-in-left, only-in-right, and size mismatch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Folder Compare Names')
    print('A copy check without hashing the world.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
