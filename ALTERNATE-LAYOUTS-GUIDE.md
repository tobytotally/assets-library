# Finding & Creating Alternate Logo Layouts

## Your Question
> "Is it possible to find alternate versions of logos such as landscape or just icon or portrait if only have landscape or landscape if only have portrait?"

## Short Answer
**Yes, partially!** The system can:
1. ✓ **Detect** if you have multiple source files with different layouts
2. ✓ **Auto-generate** icon/square versions from any layout
3. ⚠️ **Cannot perfectly convert** landscape → portrait or vice versa (requires manual design)

---

## What the System Does Automatically

### ✓ Always Generated (7 variations):
When you add ANY logo (landscape, portrait, or square), the system generates:

1. **original** - Your source file, preserved
2. **trimmed** - Whitespace removed
3. **white** - White version for dark backgrounds
4. **black** - Black version for light backgrounds
5. **icon-512** - 512×512 square icon (auto-generated from any layout)
6. **icon-1024** - 1024×1024 square icon (auto-generated from any layout)
7. **layout** - The detected layout (landscape/portrait/square)

### 🔄 Smart Icon Generation
The `icon-512` and `icon-1024` variations work as **universal fallbacks**:
- **Landscape logo** → Square icon is centered with padding
- **Portrait logo** → Square icon is centered with padding
- **Square logo** → Square icon fits perfectly

So even if you only have a landscape logo, you get a usable square icon!

---

## Detecting Multiple Source Files

### New Tool: Logo Variant Detector

I've created a script that scans for multiple logo files in each client folder:

```bash
cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library
python scripts/detect-logo-variants.py
```

**What it finds:**
- Clients with multiple source PNG files
- Different layout orientations available
- Recommendations for which file to use for each layout

### Example Output:
```
[*] globalcom
   Source files: 2
   Layouts available: square
   [!] All variants are square
   Missing: landscape, portrait
```

---

## Current Status: Nikon & GlobalCom

Both have **2 source files** but **both are square layout**:

### Nikon:
- `Nikon.png` (800×800, square)
- `image57.png` (similar dimensions)
- ⚠️ No landscape or portrait versions available

### GlobalCom:
- `GlobalPR.png` (800×800, square)
- `Logo_GlobalComPR_Network_two_lines_RGB_300x332px_orange.png` (300×332, square)
- ⚠️ No landscape or portrait versions available

---

## Solutions for Missing Layouts

### Option 1: Request from Client (Best Quality)
Ask the client for:
- **Landscape version** - For website headers, email signatures
- **Portrait version** - For vertical displays, mobile apps
- **Icon/symbol only** - For favicons, social media avatars

### Option 2: Use Existing Variations (Automatic)
If you only have one layout, the system provides:

| You Have | Missing | Fallback Available |
|----------|---------|-------------------|
| Landscape | Portrait | Use `icon-512.png` (square icon) |
| Landscape | Square | Use `icon-512.png` (centered) |
| Portrait | Landscape | Use `icon-512.png` (square icon) |
| Portrait | Square | Use `icon-512.png` (centered) |
| Square | Landscape | ⚠️ Not ideal, but square works |
| Square | Portrait | ⚠️ Not ideal, but square works |

### Option 3: Manual Design Work
For perfect results:
1. Open logo in design software (Figma, Illustrator, Photoshop)
2. **Landscape → Portrait:** Stack elements vertically
3. **Portrait → Landscape:** Arrange elements horizontally
4. **Any → Icon:** Extract symbol/mark only (remove text)

### Option 4: AI-Assisted Conversion
Modern tools can help:
- **Remove.bg** - Extract logo from background
- **Figma Auto Layout** - Reflow elements
- **AI upscalers** - Improve quality before conversion

---

## Workflow for Multiple Layouts

If you obtain multiple layout versions:

### Step 1: Add All Files to Client Folder
```
clients/mycompany/
  ├── MyCompany-Landscape.png
  ├── MyCompany-Portrait.png
  └── MyCompany-Icon.png
```

### Step 2: Run Variant Detector
```bash
python scripts/detect-logo-variants.py
```

Output shows which file is best for each layout.

### Step 3: Choose Primary Version
Pick one as the source:
- **Landscape** - Best for most web use cases
- **Portrait** - Best for mobile apps
- **Square** - Universal (recommended)

### Step 4: Generate Variations
```bash
cd clients/mycompany
python -c "... (generation script) ..."
```

This generates the 7 standard variations from your chosen primary.

### Step 5: Manually Add Alternates (Optional)
If you want ALL layouts available:
```
clients/mycompany/
  ├── mycompany-landscape.png (generated)
  ├── mycompany-portrait-alt.png (manual copy)
  ├── mycompany-icon-512.png (generated)
  └── ... (other variations)
```

---

## Practical Recommendations

### For Most Clients:
**Square or Landscape is fine**
- Square icons work everywhere
- Landscape works in most contexts
- Portrait is rarely needed unless mobile-first

### Priority Order:
1. **Always get:** Primary logo (any layout)
2. **Nice to have:** Icon/symbol version (no text)
3. **Optional:** Alternate orientations

### Real-World Usage:
```html
<!-- Use landscape for headers -->
<img src=".../mycompany-landscape.png">

<!-- Use icon for avatars -->
<img src=".../mycompany-icon-512.png">

<!-- Use square as universal fallback -->
<img src=".../mycompany-square.png">
```

---

## Detection Report

The variant detector creates a JSON report:
`docs/logo-variants-report.json`

Contains:
```json
{
  "clients_with_multiple": [
    {
      "client": "globalcom",
      "source_files": 2,
      "layouts_available": ["square"],
      "recommendations": {
        "landscape": { "use": "GlobalPR.png", "reason": "..." },
        "portrait": { "use": "GlobalPR.png", "reason": "..." },
        "square": { "use": "GlobalPR.png", "reason": "800×800 (square layout, 0.64MP)" }
      }
    }
  ]
}
```

---

## Summary

✓ **What works automatically:**
- Icon/square versions from any layout
- Multiple source file detection
- Quality/dimension analysis

⚠️ **What requires manual work:**
- Perfect landscape → portrait conversion
- Perfect portrait → landscape conversion
- Symbol extraction (icon-only versions)

💡 **Best practice:**
- Request multiple layouts from clients upfront
- Use square/icon versions as universal fallbacks
- Only manually convert when client-specific layouts are critical

---

**Tools Created:**
- `scripts/detect-logo-variants.py` - Scan for alternate layouts
- `docs/logo-variants-report.json` - Detection results

**Last Updated:** 2025-10-19
