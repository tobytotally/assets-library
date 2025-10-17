# Assets Library

A structured repository for hosting and managing static assets such as images, documents, videos, and icons that can be easily referenced in markdown files and HTML.

## 📁 Directory Structure

```
assets-library/
├── assets/
│   ├── images/       # Image files (PNG, JPG, GIF, SVG, etc.)
│   ├── documents/    # Document files (PDF, DOCX, TXT, MD, etc.)
│   ├── videos/       # Video files (MP4, WEBM, etc.)
│   └── icons/        # Icon files (SVG, PNG favicons, etc.)
├── examples/         # Example files demonstrating asset usage
└── README.md         # This file
```

## 🚀 Quick Start

### Using Assets in Markdown

Reference assets using relative paths:

```markdown
# Example with image
![Example Image](./assets/images/example.svg)

# Example with icon
![Checkmark](./assets/icons/checkmark.svg)

# Example with document link
[Read the Sample Document](./assets/documents/sample.md)
```

### Using Assets in HTML

Use relative paths in your HTML files:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Asset Example</title>
</head>
<body>
    <h1>Asset Examples</h1>
    
    <!-- Image -->
    <img src="./assets/images/example.svg" alt="Example Image">
    
    <!-- Icon -->
    <img src="./assets/icons/checkmark.svg" alt="Checkmark" width="24" height="24">
    
    <!-- Document Link -->
    <a href="./assets/documents/sample.md">View Sample Document</a>
</body>
</html>
```

## 📝 Examples

Check out the `examples/` directory for:
- `example.md` - Markdown file with asset references
- `example.html` - HTML file with asset references

## 📋 Best Practices

1. **Descriptive Naming**: Use clear, descriptive filenames (e.g., `user-profile-icon.svg` instead of `icon1.svg`)
2. **Organize by Type**: Keep assets organized in their respective directories
3. **Optimize Files**: 
   - Compress images before uploading
   - Use appropriate formats (SVG for scalable graphics, PNG for transparency, JPG for photos)
4. **Accessibility**: Always include alt text for images
5. **Documentation**: Document any special assets in the appropriate README files

## 🔗 Referencing Assets

### From Root Directory
```markdown
![Image](./assets/images/example.svg)
```

### From Subdirectories
If your markdown/HTML file is in a subdirectory, adjust the path:
```markdown
![Image](../assets/images/example.svg)
```

### Absolute GitHub URLs
For use in external sites or documentation:
```markdown
![Image](https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/example.svg)
```

## 📦 Asset Types

### Images (`assets/images/`)
- Photographs
- Graphics
- Diagrams
- Screenshots

### Documents (`assets/documents/`)
- PDF files
- Text documents
- Markdown files
- Templates

### Videos (`assets/videos/`)
- Tutorial videos
- Demos
- Presentations

### Icons (`assets/icons/`)
- UI icons
- Logos
- Favicons
- SVG graphics

## 🤝 Contributing

To add new assets:

1. Place files in the appropriate directory under `assets/`
2. Use descriptive filenames
3. Optimize files before committing
4. Update documentation if needed

## 📄 License

This repository is for asset hosting and management.