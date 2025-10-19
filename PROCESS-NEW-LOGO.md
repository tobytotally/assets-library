# Process for Adding New Logos

Quick reference guide for adding new client logos to the assets library and updating all systems.

## Current Status: Nikon

**Location:** `assets/images/logos/clients/nikon/`

**Files:**
- ✓ `Nikon.png` (source logo added)
- ✓ `Nikon-Logo-Primary (3).svg` (SVG source)
- ✓ `image57.png` (variant)

**Status:** ⚠️ Variations NOT yet generated

---

## Complete Workflow for New Logos

### Step 1: Add Source Logo ✓

Place the original/best quality logo file in:
```
assets/images/logos/clients/{client-name}/{client-name}.png
```

**For Nikon:** Already done ✓

### Step 2: Generate Logo Variations

Run the client-centric reorganization script to generate all 7 variations:

```bash
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos
python reorganize_client_centric.py
```

This creates:
- `{client}-original.png` - Original with preserved quality
- `{client}-trimmed.png` - No whitespace, tight crop
- `{client}-white.png` - White version for dark backgrounds
- `{client}-black.png` - Black version for light backgrounds
- `{client}-icon-512.png` - Square icon (512×512)
- `{client}-icon-1024.png` - Square icon (1024×1024)
- `{client}-{layout}.png` - Layout optimized (landscape/portrait/square)

**Note:** The script automatically:
- Detects existing clients and adds new ones
- Updates `index.json` with client metadata
- Updates `by-category.json` with category mappings

### Step 3: Update Category Mapping (if needed)

If the new client needs a specific category, edit this file first:
```
assets/images/logos/reorganize_client_centric.py
```

Add to the `CATEGORY_MAP` dictionary around line 23:
```python
CATEGORY_MAP = {
    # Technology (add Nikon here)
    'nikon': 'technology',  # or 'commercial', 'charity', etc.
    # ... existing entries
}
```

### Step 4: Regenerate Documentation

After generating variations, update the documentation:

```bash
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library
python scripts\generate_docs.py
```

This regenerates:
- `docs/LOGO-REFERENCE.md` - Complete URL catalog for all clients
- `docs/logo-urls.json` - Programmatic API access

### Step 5: Update Tagging System (Optional)

If using the image library HTML viewer with tags, update:
```
totally-assets/initial-client-tags.json
```

Add tags for the new client:
```json
{
  "nikon": ["technology", "commercial", "camera", "imaging", "professional"]
}
```

### Step 6: Commit to GitHub

Stage and commit all changes:

```bash
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library
git add .
git commit -m "Add Nikon client logos with all variations

- Added Nikon source logos
- Generated 7 variations (original, trimmed, white, black, icons, layout)
- Updated index.json and by-category.json
- Regenerated LOGO-REFERENCE.md and logo-urls.json

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

### Step 7: CDN URLs Available

After pushing to GitHub, logos are immediately available via CDN:

**Base URL:**
```
https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/nikon/
```

**Available variations:**
```
nikon-original.png
nikon-trimmed.png
nikon-white.png
nikon-black.png
nikon-icon-512.png
nikon-icon-1024.png
nikon-landscape.png (or portrait/square)
```

**Full URL example:**
```
https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/nikon/nikon-white.png
```

---

## Quick Command Reference

### For Nikon (Execute Now):

```bash
# Step 1: Generate variations
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos
python reorganize_client_centric.py

# Step 2: Update documentation
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library
python scripts\generate_docs.py

# Step 3: Commit and push
git add .
git commit -m "Add Nikon client logos"
git push
```

---

## Troubleshooting

### Script doesn't find new client
- Make sure logo is in `clients/{client-name}/` folder
- Filename should be a PNG (not SVG)
- Try running with just one clean PNG file first

### Wrong category assigned
- Edit `reorganize_client_centric.py` and add to `CATEGORY_MAP`
- Re-run the script

### Variations look wrong
- Check source image has transparency (RGBA PNG)
- Ensure source is high quality
- The script auto-crops and optimizes

---

## Files Modified by This Process

When you run the complete workflow, these files are updated:

1. `assets/images/logos/clients/{client}/` - 7-8 PNG variations
2. `assets/images/logos/clients/index.json` - Client metadata
3. `assets/images/logos/clients/by-category.json` - Category mappings
4. `docs/LOGO-REFERENCE.md` - Complete URL catalog
5. `docs/logo-urls.json` - Programmatic API

---

## Usage in Proposals

Once pushed to GitHub, use in HTML:

```html
<!-- Simple usage -->
<img src="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/nikon/nikon-original.png"
     alt="Nikon Logo">

<!-- Dark/light mode responsive -->
<picture>
  <source media="(prefers-color-scheme: dark)"
          srcset="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/nikon/nikon-white.png">
  <img src="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/nikon/nikon-black.png"
       alt="Nikon Logo">
</picture>
```

---

**Last Updated:** 2025-10-19
**Status:** Nikon ready for Step 2 (generate variations)
