# Quick Start - Adding New Logos (e.g., Nikon)

## Visual Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Add Logo Files                                     │
│  📁 assets/images/logos/clients/nikon/Nikon.png            │
│  ✓ Already done for Nikon                                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Open IMAGE-LIBRARY.html in Browser                 │
│  🌐 C:\Users\toby\Documents\...\IMAGE-LIBRARY.html         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Click "▶ Generate Logo Variations" Button          │
│  • Modal pops up with command to run                        │
│  • Copy command and run in terminal                         │
│  • Generates 7 variations per new client                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Click "📄 Update Documentation" Button             │
│  • Modal pops up with command to run                        │
│  • Copy command and run in terminal                         │
│  • Updates LOGO-REFERENCE.md and logo-urls.json            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Click "Reload Library" in Browser                  │
│  • See Nikon appear with all 7 variations                   │
│  • Add tags using the + button                              │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Commit & Push to GitHub                            │
│  git add .                                                   │
│  git commit -m "Add Nikon client logos"                     │
│  git push                                                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  ✓ Done! Logos available on GitHub CDN                      │
│  https://raw.githubusercontent.com/tobytotally/             │
│    assets-library/main/assets/images/logos/clients/         │
│    nikon/nikon-white.png                                    │
└─────────────────────────────────────────────────────────────┘
```

## New UI Buttons in IMAGE-LIBRARY.html

### 🔧 Logo Management Section

The info box now has 3 new buttons:

1. **▶ Generate Logo Variations** (Orange)
   - Shows modal with command to run
   - Command: `python reorganize_client_centric.py`
   - Generates all 7 variations for new logos

2. **📄 Update Documentation** (Purple)
   - Shows modal with command to run
   - Command: `python scripts\generate_docs.py`
   - Updates LOGO-REFERENCE.md and logo-urls.json

3. **📖 View Process Guide** (Gray)
   - Opens PROCESS-NEW-LOGO.md
   - Full detailed instructions

### How the Buttons Work

**Browser → Terminal Workflow:**

1. Click button in browser
2. Confirmation dialog explains what will happen
3. Modal shows command to copy
4. Copy command, run in terminal
5. Click "Reload Library" to see results

**Why not automatic?**
- Python scripts need file system access
- Safer to show what's happening
- User maintains control

### Button Appearance

```
🔧 Logo Management: Add new client logos to generate variations and update documentation.
[▶ Generate Logo Variations] [📄 Update Documentation] [📖 View Process Guide]
      (Orange)                      (Purple)                  (Gray Link)
```

## For Nikon Specifically

### Current Status
- ✓ Source files added to `clients/nikon/`
- ⚠️ Variations NOT generated yet
- ⚠️ Not in index.json
- ⚠️ Not in documentation

### Next Steps

1. **Open IMAGE-LIBRARY.html** in your browser
2. **Click "▶ Generate Logo Variations"**
3. **Copy the command** shown in the modal:
   ```bash
   cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos
   python reorganize_client_centric.py
   ```
4. **Run it in your terminal**
5. **Click "📄 Update Documentation"**
6. **Copy the command** shown in the modal:
   ```bash
   cd C:\Users\toby\Documents\document-cloud\totally-assets\assets-library
   python scripts\generate_docs.py
   ```
7. **Run it in your terminal**
8. **Click "Reload Library"** in the browser
9. **Find Nikon** in the list and verify it has 7 variations
10. **Commit and push** to GitHub

### Expected Output

After running the scripts, you should see:
```
assets/images/logos/clients/nikon/
  ├── Nikon.png (original source)
  ├── nikon-original.png
  ├── nikon-trimmed.png
  ├── nikon-white.png
  ├── nikon-black.png
  ├── nikon-icon-512.png
  ├── nikon-icon-1024.png
  └── nikon-landscape.png (or portrait/square)
```

## Related Files

- **IMAGE-LIBRARY.html** - Main UI with new buttons
- **PROCESS-NEW-LOGO.md** - Detailed process guide
- **reorganize_client_centric.py** - Generates variations
- **scripts/generate_docs.py** - Updates documentation

---

**Last Updated:** 2025-10-19
**Status:** UI updated with trigger buttons
