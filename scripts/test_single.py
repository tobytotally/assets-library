#!/usr/bin/env python3
"""
Simple single-file tester for the autocrop algorithm.
Usage:
  python scripts/test_single.py input.png output.png --white-thresh 245 --pad 8
"""
import argparse
from PIL import Image
import numpy as np
import sys

def autocrop_image(img, white_thresh=245, pad=0):
    img = img.convert("RGBA")
    arr = np.array(img)
    alpha = arr[..., 3]
    if alpha.max() > 0:
        mask = alpha > 0
    else:
        rgb = arr[..., :3]
        mask = np.any(rgb < white_thresh, axis=-1)

    if not mask.any():
        return None

    ys, xs = mask.nonzero()
    y0, y1 = ys.min(), ys.max() + 1
    x0, x1 = xs.min(), xs.max() + 1

    h, w = arr.shape[:2]
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(w, x1 + pad)
    y1 = min(h, y1 + pad)

    return img.crop((x0, y0, x1, y1))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--white-thresh", type=int, default=245)
    p.add_argument("--pad", type=int, default=8)
    args = p.parse_args()

    try:
        img = Image.open(args.input)
    except Exception as e:
        print("Cannot open input:", e, file=sys.stderr)
        sys.exit(2)

    cropped = autocrop_image(img, white_thresh=args.white_thresh, pad=args.pad)
    if cropped is None:
        print("Nothing to crop; copying original to output.")
        img.convert("RGBA").save(args.output)
    else:
        cropped.save(args.output)
        print(f"Cropped saved to {args.output}")

if __name__ == "__main__":
    main()