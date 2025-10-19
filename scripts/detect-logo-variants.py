#!/usr/bin/env python3
"""
Logo Variant Detector
Scans client folders for multiple logo files and suggests which to use for different layouts
Helps identify landscape/portrait/icon variations when multiple source files exist
"""

import os
from pathlib import Path
from PIL import Image
import json

CLIENTS_DIR = Path(r"C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos\clients")

def analyze_image(image_path):
    """Analyze an image and return its characteristics"""
    try:
        img = Image.open(image_path)

        # Get dimensions
        width, height = img.size
        ratio = width / height

        # Determine layout
        if ratio > 1.3:
            layout = 'landscape'
        elif ratio < 0.75:
            layout = 'portrait'
        else:
            layout = 'square'

        # Calculate complexity (number of unique colors)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        colors = len(set(img.getdata()))

        # Check if it has transparency
        has_transparency = img.mode == 'RGBA'

        # Get file size
        file_size = os.path.getsize(image_path)

        return {
            'path': str(image_path),
            'filename': image_path.name,
            'width': width,
            'height': height,
            'ratio': round(ratio, 2),
            'layout': layout,
            'colors': colors,
            'has_transparency': has_transparency,
            'file_size': file_size,
            'megapixels': round((width * height) / 1_000_000, 2)
        }
    except Exception as e:
        return None

def suggest_best_variant(variants, target_layout):
    """Suggest the best variant for a target layout"""
    # Filter by target layout
    matching = [v for v in variants if v['layout'] == target_layout]

    if matching:
        # Pick the highest quality (most pixels)
        return max(matching, key=lambda x: x['width'] * x['height'])

    # If no exact match, find closest
    if target_layout == 'landscape':
        # Pick widest ratio
        return max(variants, key=lambda x: x['ratio'])
    elif target_layout == 'portrait':
        # Pick tallest ratio
        return min(variants, key=lambda x: x['ratio'])
    else:
        # Pick most square
        return min(variants, key=lambda x: abs(x['ratio'] - 1.0))

def scan_client_folder(client_path):
    """Scan a client folder for logo variants"""
    # Find all PNG files (exclude generated variants)
    source_files = []
    for file in client_path.glob('*.png'):
        # Skip already-generated variants
        if any(suffix in file.stem for suffix in ['-original', '-trimmed', '-white', '-black', '-icon-', '-landscape', '-portrait', '-square']):
            continue
        source_files.append(file)

    # Also check for SVG
    svg_files = list(client_path.glob('*.svg'))

    if not source_files:
        return None

    # Analyze each source file
    variants = []
    for file in source_files:
        analysis = analyze_image(file)
        if analysis:
            variants.append(analysis)

    if not variants:
        return None

    # Determine what's available
    layouts_available = set(v['layout'] for v in variants)

    # Make suggestions
    suggestions = {
        'client': client_path.name,
        'source_files': len(source_files),
        'svg_files': len(svg_files),
        'variants_found': variants,
        'layouts_available': list(layouts_available),
        'recommendations': {}
    }

    # Recommend best file for each layout
    for target in ['landscape', 'portrait', 'square']:
        best = suggest_best_variant(variants, target)
        suggestions['recommendations'][target] = {
            'use': best['filename'],
            'reason': f"{best['width']}×{best['height']} ({best['layout']} layout, {best['megapixels']}MP)"
        }

    # Overall recommendation
    if len(variants) > 1:
        suggestions['has_multiple_variants'] = True
        suggestions['primary_recommendation'] = max(variants, key=lambda x: x['megapixels'])['filename']
    else:
        suggestions['has_multiple_variants'] = False
        suggestions['primary_recommendation'] = variants[0]['filename']

    return suggestions

def main():
    """Scan all client folders and report findings"""
    print("=" * 70)
    print("LOGO VARIANT DETECTOR")
    print("=" * 70)
    print()

    clients_with_multiple = []
    clients_missing_layouts = []

    for client_folder in sorted(CLIENTS_DIR.iterdir()):
        if not client_folder.is_dir():
            continue

        if client_folder.name in ['README.md', 'index.json', 'by-category.json']:
            continue

        analysis = scan_client_folder(client_folder)

        if not analysis:
            continue

        # Report interesting cases
        if analysis['has_multiple_variants']:
            clients_with_multiple.append(analysis)
            print(f"[*] {analysis['client']}")
            print(f"   Source files: {analysis['source_files']}")
            print(f"   Layouts available: {', '.join(analysis['layouts_available'])}")

            if len(analysis['layouts_available']) > 1:
                print(f"   [OK] Multiple layouts detected!")
                for layout, rec in analysis['recommendations'].items():
                    if layout in analysis['layouts_available']:
                        print(f"      {layout}: {rec['use']}")
            else:
                print(f"   [!] All variants are {analysis['layouts_available'][0]}")
                missing = set(['landscape', 'portrait', 'square']) - set(analysis['layouts_available'])
                if missing:
                    print(f"   Missing: {', '.join(missing)}")
                    clients_missing_layouts.append(analysis)
            print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Clients with multiple source files: {len(clients_with_multiple)}")
    print(f"Clients missing layout variants: {len(clients_missing_layouts)}")
    print()

    if clients_missing_layouts:
        print("SUGGESTIONS:")
        print("For clients with only one layout, consider:")
        print("  • Landscape-only: Create square icon version for social media")
        print("  • Portrait-only: Create landscape version for headers/banners")
        print("  • Square-only: Can work for all layouts (recommended default)")
        print()
        print("To create alternate layouts, you can:")
        print("  1. Request alternate logo files from the client")
        print("  2. Use design tools to adapt existing logo")
        print("  3. Use square/icon versions as fallback")

    # Save report
    report_path = Path(r"C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\docs") / 'logo-variants-report.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'clients_with_multiple': clients_with_multiple,
            'clients_missing_layouts': clients_missing_layouts
        }, f, indent=2)

    print(f"\nDetailed report saved to: {report_path}")

if __name__ == '__main__':
    main()
