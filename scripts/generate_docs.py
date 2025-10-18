#!/usr/bin/env python3
"""
Generate comprehensive documentation for logo assets
Creates LOGO-REFERENCE.md and logo-urls.json
"""

import json
from pathlib import Path

# Configuration
CLIENTS_DIR = Path(r"C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos\clients")
DOCS_DIR = Path(r"C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\docs")
BASE_URL = "https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/"

def load_metadata():
    """Load index.json and by-category.json"""
    with open(CLIENTS_DIR / "index.json", 'r', encoding='utf-8') as f:
        index = json.load(f)

    with open(CLIENTS_DIR / "by-category.json", 'r', encoding='utf-8') as f:
        by_category = json.load(f)

    return index, by_category

def generate_logo_reference_md(index, by_category):
    """Generate comprehensive LOGO-REFERENCE.md"""

    md = []
    md.append("# Logo Assets Reference - GitHub CDN URLs\n")
    md.append(f"**Base URL:** `{BASE_URL}`\n")
    md.append(f"**Total Clients:** {len(index)}\n")
    md.append("**Variations per Client:** 7 (original, trimmed, white, black, icon-512, icon-1024, layout)\n\n")

    md.append("## URL Pattern\n\n")
    md.append("```\n")
    md.append(f"{BASE_URL}{{client-name}}/{{client-name}}-{{variation}}.png\n")
    md.append("```\n\n")

    md.append("**Variations:** `original`, `trimmed`, `white`, `black`, `icon-512`, `icon-1024`, `landscape|portrait|square`\n\n")

    md.append("## Quick Copy URLs\n\n")

    # Group by category
    for category in ['accreditations', 'charity', 'commercial', 'technology', 'tools', 'uncategorized']:
        if category not in by_category:
            continue

        clients = sorted(by_category[category])
        if not clients:
            continue

        md.append(f"### {category.title()} ({len(clients)} clients)\n\n")

        for client_name in clients:
            if client_name not in index:
                continue

            client_data = index[client_name]
            display_name = client_data['name']
            layout = client_data.get('layout_type', 'landscape')

            md.append(f"#### {display_name}\n\n")
            md.append(f"**Client ID:** `{client_name}`\n\n")

            # Generate URLs for each variation
            variations = [
                ('Original', 'original'),
                ('Trimmed (no whitespace)', 'trimmed'),
                ('White (dark mode)', 'white'),
                ('Black (light mode)', 'black'),
                ('Icon 512×512', 'icon-512'),
                ('Icon 1024×1024', 'icon-1024'),
                (f'Layout ({layout})', layout)
            ]

            for label, variation in variations:
                url = f"{BASE_URL}{client_name}/{client_name}-{variation}.png"
                md.append(f"- **{label}:** `{url}`\n")

            md.append("\n")

    md.append("## Usage Examples\n\n")
    md.append("### HTML\n")
    md.append("```html\n")
    md.append(f'<img src="{BASE_URL}crisis/crisis-original.png" alt="Crisis Logo">\n')
    md.append(f'<img src="{BASE_URL}crisis/crisis-white.png" alt="Crisis Logo (White)">\n')
    md.append("```\n\n")

    md.append("### Markdown\n")
    md.append("```markdown\n")
    md.append(f"![Crisis Logo]({BASE_URL}crisis/crisis-original.png)\n")
    md.append("```\n\n")

    md.append("### Responsive Dark/Light Mode\n")
    md.append("```html\n")
    md.append("<picture>\n")
    md.append("  <source media=\"(prefers-color-scheme: dark)\"\n")
    md.append(f"          srcset=\"{BASE_URL}crisis/crisis-white.png\">\n")
    md.append(f"  <img src=\"{BASE_URL}crisis/crisis-black.png\" alt=\"Crisis Logo\">\n")
    md.append("</picture>\n")
    md.append("```\n\n")

    md.append("## Categories Reference\n\n")
    for category, clients in sorted(by_category.items()):
        md.append(f"### {category.title()}\n")
        md.append(", ".join(f"`{c}`" for c in sorted(clients)))
        md.append("\n\n")

    return "".join(md)

def generate_logo_urls_json(index, by_category):
    """Generate logo-urls.json for programmatic access"""

    output = {
        "baseUrl": BASE_URL,
        "totalClients": len(index),
        "categories": {},
        "clients": {}
    }

    # Add category counts
    for category, clients in by_category.items():
        output["categories"][category] = {
            "count": len(clients),
            "clients": sorted(clients)
        }

    # Add full client data
    for client_name, client_data in sorted(index.items()):
        layout = client_data.get('layout_type', 'landscape')

        output["clients"][client_name] = {
            "name": client_data['name'],
            "category": client_data['category'],
            "layout": layout,
            "urls": {
                "original": f"{BASE_URL}{client_name}/{client_name}-original.png",
                "trimmed": f"{BASE_URL}{client_name}/{client_name}-trimmed.png",
                "white": f"{BASE_URL}{client_name}/{client_name}-white.png",
                "black": f"{BASE_URL}{client_name}/{client_name}-black.png",
                "icon512": f"{BASE_URL}{client_name}/{client_name}-icon-512.png",
                "icon1024": f"{BASE_URL}{client_name}/{client_name}-icon-1024.png",
                "layout": f"{BASE_URL}{client_name}/{client_name}-{layout}.png"
            }
        }

    return json.dumps(output, indent=2, ensure_ascii=False)

def main():
    print("=" * 70)
    print("GENERATING LOGO DOCUMENTATION")
    print("=" * 70)
    print()

    # Create docs directory
    DOCS_DIR.mkdir(exist_ok=True, parents=True)

    # Load metadata
    print("Loading metadata...")
    index, by_category = load_metadata()
    print(f"[OK] Loaded {len(index)} clients across {len(by_category)} categories")
    print()

    # Generate LOGO-REFERENCE.md
    print("Generating LOGO-REFERENCE.md...")
    md_content = generate_logo_reference_md(index, by_category)
    md_file = DOCS_DIR / "LOGO-REFERENCE.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"[OK] Created: {md_file}")
    print()

    # Generate logo-urls.json
    print("Generating logo-urls.json...")
    json_content = generate_logo_urls_json(index, by_category)
    json_file = DOCS_DIR / "logo-urls.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json_content)
    print(f"[OK] Created: {json_file}")
    print()

    print("=" * 70)
    print("DOCUMENTATION GENERATION COMPLETE")
    print("=" * 70)
    print()
    print(f"Files created in: {DOCS_DIR}")
    print("  - LOGO-REFERENCE.md (comprehensive URL catalog)")
    print("  - logo-urls.json (programmatic access)")
    print()
    print("Base URL for all assets:")
    print(f"  {BASE_URL}")
    print()

if __name__ == "__main__":
    main()
