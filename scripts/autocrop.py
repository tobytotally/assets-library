#!/usr/bin/env python3
"""
scripts/autocrop.py

Batch autocrop utility for logo images.

Features:
- Uses alpha channel if present; otherwise treats near-white as background.
- Skips files that haven't changed since last run (cache of input file hashes).
- Writes outputs to output-dir preserving relative paths.
- Exit code 0 even when no changes; helpful for CI usage.
"""
import argparse
import os
import sys
import json
import hashlib
from PIL import Image
import numpy as np

SUPPORTED_EXT = ('.png', '.jpg', '.jpeg', '.webp', '.tif', '.tiff', '.gif')

def sha1_of_file(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def load_cache(path):
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

def autocrop_image_pil(img, white_thresh=245, pad=0):
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

    ys, xs = np.where(mask)
    y0, y1 = ys.min(), ys.max() + 1
    x0, x1 = xs.min(), xs.max() + 1

    h, w = arr.shape[:2]
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    x1 = min(w, x1 + pad)
    y1 = min(h, y1 + pad)

    return img.crop((x0, y0, x1, y1))

def process_dir(input_dir, output_dir, white_thresh=245, pad=0, cache_file='.autocrop_cache.json'):
    cache = load_cache(cache_file)
    new_cache = {}
    changed = False

    os.makedirs(output_dir, exist_ok=True)
    for root, _, files in os.walk(input_dir):
        for fname in files:
            if not fname.lower().endswith(SUPPORTED_EXT):
                continue
            in_path = os.path.join(root, fname)
            rel = os.path.relpath(in_path, input_dir)
            out_path = os.path.join(output_dir, rel)
            out_dir = os.path.dirname(out_path)
            os.makedirs(out_dir, exist_ok=True)

            try:
                file_hash = sha1_of_file(in_path)
            except Exception as e:
                print(f"[skip] cannot read {in_path}: {e}", file=sys.stderr)
                continue

            new_cache[rel] = file_hash
            prev_hash = cache.get(rel)

            # skip if input unchanged and output exists
            if prev_hash == file_hash and os.path.exists(out_path):
                print(f"[skip] unchanged: {rel}")
                continue

            try:
                img = Image.open(in_path)
            except Exception as e:
                print(f"[skip] cannot open {in_path}: {e}", file=sys.stderr)
                continue

            cropped = autocrop_image_pil(img, white_thresh=white_thresh, pad=pad)
            if cropped is None:
                # If nothing to crop, copy original (converted to RGBA to normalize)
                print(f"[copy] nothing to crop, copying original: {rel}")
                img.convert("RGBA").save(out_path)
                changed = True
            else:
                # Only save if different or missing
                cropped.save(out_path)
                print(f"[cropped] {rel} -> {os.path.relpath(out_path)}")
                changed = True

    save_cache(cache_file, new_cache)
    return changed

def parse_args():
    p = argparse.ArgumentParser(description="Batch autocrop logos")
    p.add_argument("--input-dir", default="logos", help="Directory with input images")
    p.add_argument("--output-dir", default="cropped", help="Directory for cropped images")
    p.add_argument("--white-thresh", type=int, default=245, help="White threshold (0-255) for non-alpha images")
    p.add_argument("--pad", type=int, default=8, help="Padding in pixels to add after cropping")
    p.add_argument("--cache-file", default=".autocrop_cache.json", help="Cache file path")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    changed = process_dir(
        args.input_dir,
        args.output_dir,
        white_thresh=args.white_thresh,
        pad=args.pad,
        cache_file=args.cache_file
    )
    if changed:
        print("Processing produced changes.")
    else:
        print("No changes produced.")
    # Always exit 0 so workflow continues; PR creation step will decide if there's anything to create
    sys.exit(0)