# Assets Library - GitHub-Hosted CDN for Logo Assets

Centralized, version-controlled repository for logo assets with automatic GitHub CDN hosting.

## 📂 Repository Structure

```
assets-library/
├── assets/
│   └── images/
│       └── logos/
│           └── clients/              ← Main asset folder
│               ├── against-breast-cancer/
│               ├── aws/
│               ├── crisis/
│               ├── ... (100 clients)
│               ├── index.json        (metadata)
│               ├── by-category.json  (category index)
│               └── README.md
├── docs/
│   ├── LOGO-REFERENCE.md            ← Complete URL catalog
│   ├── logo-urls.json               ← Programmatic access
│   └── logo-catalog.html            (coming soon)
├── scripts/
│   ├── generate_docs.py             (regenerate documentation)
│   ├── reorganize_client_centric.py (add new clients)
│   └── logo-helper.js               ← Proposal integration
└── README.md                        ← You are here
```

## 🚀 Quick Start - Using Logos in Proposals

### Direct URL Pattern

```
https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/{client-name}/{client-name}-{variation}.png
```

**Example:**
```
https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-white.png
```

### Available Variations

Every client has **7 pre-generated variations**:

| Variation | Filename | Use Case |
|-----------|----------|----------|
| Original | `-original.png` | Source quality with original colors |
| Trimmed | `-trimmed.png` | No whitespace, precise placement |
| White | `-white.png` | Dark backgrounds, dark mode |
| Black | `-black.png` | Light backgrounds, print |
| Icon 512 | `-icon-512.png` | Social media, avatars |
| Icon 1024 | `-icon-1024.png` | High-res social icons |
| Layout | `-landscape.png`<br>`-portrait.png`<br>`-square.png` | Layout-optimized |

## 📋 Complete Documentation

- **[LOGO-REFERENCE.md](docs/LOGO-REFERENCE.md)** - Complete URL catalog for all 100 clients
- **[logo-urls.json](docs/logo-urls.json)** - Programmatic access with metadata
- **[Logo Helper JS](scripts/logo-helper.js)** - JavaScript utilities for proposals

## 💻 Usage Examples

### HTML

```html
<!-- Simple usage -->
<img src="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-original.png"
     alt="Crisis Logo">

<!-- Responsive dark/light mode -->
<picture>
  <source media="(prefers-color-scheme: dark)"
          srcset="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-white.png">
  <img src="https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-black.png"
       alt="Crisis Logo">
</picture>
```

### JavaScript (with logo-helper.js)

```javascript
// Load helper
import { getLogoUrl, createResponsiveLogo } from './scripts/logo-helper.js';

// Get specific variation
const whiteUrl = getLogoUrl('crisis', 'white');
// → https://raw.githubusercontent.com/.../crisis/crisis-white.png

// Create responsive HTML
const html = createResponsiveLogo('crisis', 'Crisis Logo', 'proposal-logo');
```

### Markdown

```markdown
![Crisis Logo](https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/crisis/crisis-original.png)
```

## 🏷️ Browse by Category

**100 clients** organized across **6 categories**:

- **Charity** (35 clients) - Crisis, Against Breast Cancer, GamCare, Save the Rhino, etc.
- **Commercial** (32 clients) - JP Morgan, Galliard Homes, British Business Bank, etc.
- **Technology** (13 clients) - AWS, BBC, Figma, Slack, NHS, etc.
- **Tools** (7 clients) - Slack, Jira, ActiveCollab, Toggl, etc.
- **Accreditations** (5 clients) - Cyber Essentials Plus, Google Partner, G-Cloud, etc.
- **Uncategorized** (8 clients) - Extracted variants and artwork

See [by-category.json](assets/images/logos/clients/by-category.json) for complete category mappings.

## 📊 Asset Statistics

- **Total Clients:** 100
- **Total Files:** 700+ (7 variations per client)
- **Total Size:** ~23MB
- **Format:** PNG with transparency (RGBA)
- **Icon Sizes:** 512×512, 1024×1024 (square with 10% padding)

## ➕ Adding New Clients

### Option 1: Manual Addition

1. Add source logo to `assets/images/logos/clients/{new-client}/`
2. Run variation generator:
   ```bash
   cd assets/images/logos
   python3 reorganize_client_centric.py
   ```
3. Regenerate documentation:
   ```bash
   cd ../../..
   python3 scripts/generate_docs.py
   ```
4. Commit and push

### Option 2: Automated with GitHub Actions

(Coming soon: Drop logos in `logos/` folder, GitHub Actions automatically processes and opens PR)

## 🔄 Regenerate Documentation

After adding new clients or updating metadata:

```bash
# From repository root
python3 scripts/generate_docs.py
```

This regenerates:
- `docs/LOGO-REFERENCE.md`
- `docs/logo-urls.json`

## 🌐 CDN Considerations

### GitHub Rate Limits

- **Unauthenticated:** 60 requests/hour per IP
- **Authenticated:** 5,000 requests/hour
- **Caching:** Browsers cache images automatically

### For High-Traffic Sites

If rate limits become an issue, add a proxy layer (Netlify/Vercel/CloudFlare) with aggressive caching:

```javascript
// netlify/functions/logo.js
export async function handler(event) {
  const { client, variation = 'original' } = event.queryStringParameters;
  const url = `https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/logos/clients/${client}/${client}-${variation}.png`;

  const response = await fetch(url);
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'image/png',
      'Cache-Control': 'public, max-age=31536000' // 1 year
    },
    body: await response.buffer().toString('base64'),
    isBase64Encoded: true
  };
}
```

## 🛠️ Scripts & Utilities

- **[generate_docs.py](scripts/generate_docs.py)** - Generate documentation from metadata
- **[reorganize_client_centric.py](assets/images/logos/reorganize_client_centric.py)** - Process new logos
- **[logo-helper.js](scripts/logo-helper.js)** - JavaScript utilities for proposals

## 📖 API Reference

See [logo-urls.json](docs/logo-urls.json) for complete API structure:

```json
{
  "baseUrl": "https://raw.githubusercontent.com/...",
  "totalClients": 100,
  "categories": { ... },
  "clients": {
    "crisis": {
      "name": "Crisis",
      "category": "charity",
      "layout": "landscape",
      "urls": {
        "original": "...",
        "white": "...",
        "black": "...",
        ...
      }
    }
  }
}
```

## ⚙️ Legacy: Auto-crop Workflow

The repository includes an auto-crop GitHub Actions workflow (legacy):

- Auto-crops images in `logos/` folder
- Creates PR with processed images
- See `.github/workflows/autocrop.yml`

This is **separate** from the main client-centric logo library and can be ignored for general use.

## 🤝 Contributing

1. Add new logos to appropriate category
2. Run `reorganize_client_centric.py`
3. Run `generate_docs.py`
4. Commit and push
5. Submit PR

## 📄 License

Logo assets are property of their respective owners. This repository provides hosting and organization only.

Scripts use Pillow and NumPy (open source). Verify licenses for commercial use.

---

**Need help?** See [LOGO-REFERENCE.md](docs/LOGO-REFERENCE.md) for complete URL catalog or [logo-helper.js](scripts/logo-helper.js) for programmatic access.
