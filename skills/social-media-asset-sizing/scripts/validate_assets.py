#!/usr/bin/env python3
"""Check raster pixel dimensions and metadata. Requires Pillow: pip install pillow.

Example: python scripts/validate_assets.py artwork.png --width 1080 --height 1920
Not a safe-zone, readability, accessibility or platform-upload validator.
"""
import argparse
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    parser.add_argument('--width', type=int, required=True)
    parser.add_argument('--height', type=int, required=True)
    args = parser.parse_args()
    try:
        from PIL import Image
    except ImportError:
        parser.error('Pillow is required: pip install pillow')
    if args.width <= 0 or args.height <= 0:
        parser.error('Expected width and height must be positive')
    divisor = math.gcd(args.width, args.height)
    print(f'Target {args.width}x{args.height} ({args.width//divisor}:{args.height//divisor})')
    failed = False
    for file in args.files:
        try:
            with Image.open(file) as im:
                w, h = im.size
                good = (w, h) == (args.width, args.height)
                failed |= not good
                ratio_divisor = math.gcd(w, h)
                print(f'{"PASS" if good else "FAIL"} | {file} | {w}x{h} | '
                      f'{w//ratio_divisor}:{h//ratio_divisor} | {im.format} | {im.mode}')
        except Exception as exc:
            failed = True
            print(f'FAIL | {file} | {type(exc).__name__}: {exc}')
    raise SystemExit(1 if failed else 0)


if __name__ == '__main__':
    main()
