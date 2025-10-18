# Logo Assets Library - Client-Centric Structure

## Overview
Organized logo library with **100 unique clients**, each with 7 pre-generated variations ready for any design context.

## Directory Structure

```
clients/
├── against-breast-cancer/
│   ├── against-breast-cancer-original.png
│   ├── against-breast-cancer-trimmed.png
│   ├── against-breast-cancer-white.png
│   ├── against-breast-cancer-black.png
│   ├── against-breast-cancer-icon-512.png
│   ├── against-breast-cancer-icon-1024.png
│   └── against-breast-cancer-landscape.png
├── aws/
├── crisis/
├── [98 more clients...]
├── index.json              (searchable metadata)
└── by-category.json        (category reference)
```

## File Naming Convention

**Format:** `{client-name}-{variation}.png`

### Variations Available

1. **`-original.png`** - Source file with original colors
2. **`-trimmed.png`** - Whitespace/transparent borders removed
3. **`-white.png`** - White silhouette on transparent background
4. **`-black.png`** - Black silhouette on transparent background
5. **`-icon-512.png`** - 512×512 square icon (social media ready)
6. **`-icon-1024.png`** - 1024×1024 high-res square icon
7. **`-landscape.png` / `-portrait.png` / `-square.png`** - Layout-optimized

## Quick Access by Category

Use `by-category.json` to find clients by category:

```json
{
  "charity": ["against-breast-cancer", "crisis", "gamcare", ...],
  "commercial": ["jp-morgan", "galliard-homes", ...],
  "technology": ["aws", "bbc", "figma", ...],
  "tools": ["slack", "jira-software", ...],
  "accreditations": ["cyber-essentials-plus", ...]
}
```

## Usage Examples

### 1. Get All Variations for One Client

```bash
# All Crisis logos
clients/crisis/crisis-*.png

# Results:
# - crisis-original.png
# - crisis-trimmed.png
# - crisis-white.png
# - crisis-black.png
# - crisis-icon-512.png
# - crisis-icon-1024.png
# - crisis-landscape.png
```

### 2. Get Specific Variation Across Clients

```bash
# All white logos
clients/*/\*-white.png

# All social media icons (512)
clients/*/\*-icon-512.png
```

### 3. Search by Category

```python
import json

# Load category index
with open('by-category.json') as f:
    categories = json.load(f)

# Get all charity client logos
charity_clients = categories['charity']
for client in charity_clients:
    logo_path = f"clients/{client}/{client}-original.png"
```

### 4. Search by Metadata

```python
import json

# Load metadata index
with open('index.json') as f:
    index = json.load(f)

# Find all landscape-oriented logos
landscape_clients = [
    client for client, data in index.items()
    if data['layout_type'] == 'landscape'
]

# Find all charity clients
charity_clients = [
    client for client, data in index.items()
    if data['category'] == 'charity'
]
```

## Statistics

- **Total Clients:** 100
- **Total Files:** 700
- **Files per Client:** 7 variations
- **Categories:**
  - Charity: 35 clients
  - Commercial: 32 clients
  - Technology: 13 clients
  - Tools: 7 clients
  - Accreditations: 5 clients
  - Uncategorized: 8 clients

## Layout Distribution

- **Landscape:** 79 clients (horizontal orientation)
- **Square:** 19 clients (equal dimensions)
- **Portrait:** 2 clients (vertical orientation)

## Use Cases

### White Logos (`-white.png`)
- Dark backgrounds
- Presentation slides with dark themes
- Dark mode websites
- Video overlays

### Black Logos (`-black.png`)
- Light backgrounds
- Print materials
- Document headers
- Light mode websites

### Trimmed Logos (`-trimmed.png`)
- Precise placement without margins
- Email signatures
- Business cards
- Dense layouts

### Icons (`-icon-*.png`)
- Social media profiles
- App icons
- Favicons
- Avatar placeholders

### Layout-Optimized
- **Landscape:** Website headers, email banners
- **Portrait:** Sidebar placements, mobile views
- **Square:** Profile images, grid layouts

## Adding New Clients

1. Add source logo to one of the category folders
2. Run regeneration script:

```bash
cd "C:\Users\toby\Documents\document-cloud\totally-assets\assets-library\assets\images\logos"
python3 reorganize_client_centric.py
```

3. New client folder with all variations will be created automatically

## API Reference (index.json)

```json
{
  "client-name": {
    "name": "Client Name",
    "category": "charity|commercial|technology|tools|accreditations",
    "source_category": "original category folder",
    "layout_type": "landscape|portrait|square",
    "variations": [
      "original", "trimmed", "white", "black",
      "icon-512", "icon-1024", "landscape|portrait|square"
    ]
  }
}
```

## Integration Examples

### HTML/Web
```html
<!-- Responsive logo with fallbacks -->
<picture>
  <source media="(prefers-color-scheme: dark)"
          srcset="clients/crisis/crisis-white.png">
  <img src="clients/crisis/crisis-original.png"
       alt="Crisis Logo">
</picture>
```

### React/JSX
```jsx
import crisisWhite from './clients/crisis/crisis-white.png';
import crisisBlack from './clients/crisis/crisis-black.png';

function Logo({ darkMode }) {
  return (
    <img
      src={darkMode ? crisisWhite : crisisBlack}
      alt="Crisis Logo"
    />
  );
}
```

### Node.js
```javascript
const fs = require('fs');
const path = require('path');

// Get all logos for a client
function getClientLogos(clientName) {
  const clientDir = path.join(__dirname, 'clients', clientName);
  return fs.readdirSync(clientDir)
    .filter(f => f.endsWith('.png'))
    .map(f => path.join(clientDir, f));
}

// Get specific variation
function getClientLogo(clientName, variation = 'original') {
  return path.join(
    __dirname,
    'clients',
    clientName,
    `${clientName}-${variation}.png`
  );
}
```

## Maintenance

### Regenerate All Variations
If source logos are updated:
```bash
python3 reorganize_client_centric.py
```

### Clean Old Structure
After verifying new structure works:
```bash
# Backup first!
# Then remove old category folders if needed
```

## File Formats

- **Format:** PNG with transparency (RGBA)
- **Icon Sizes:** 512×512, 1024×1024 (square)
- **Padding:** Icons have 10% padding from edges
- **Trimming:** Automatic removal of transparent borders

## Notes

- All variations maintain transparency where applicable
- Original aspect ratios preserved (except icons)
- High-quality resampling (Lanczos) for scaling
- Consistent naming for easy scripting
- No category duplication - one source of truth per client

## Support

For issues or questions:
1. Check `index.json` for client availability
2. Verify file paths match naming convention
3. Re-run script if variations are missing
4. Check source logo quality in original category folders

---

Last updated: October 2025
Total assets: 700+ logo files ready for production use
