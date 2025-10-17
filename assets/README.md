# Assets Directory

This directory contains all static assets used across the project.

## Directory Structure

- **`images/`** - Image files (PNG, JPG, GIF, SVG, etc.)
- **`documents/`** - Document files (PDF, DOCX, TXT, etc.)
- **`videos/`** - Video files (MP4, WEBM, etc.)
- **`icons/`** - Icon files (SVG, PNG favicons, etc.)

## Usage

### Referencing Assets in Markdown

You can reference assets in markdown files using relative paths:

```markdown
![Alt text](./assets/images/example.png)
```

Or for files in subdirectories:

```markdown
![Logo](./assets/icons/logo.svg)
```

### Referencing Assets in HTML

In HTML files, use relative paths:

```html
<img src="./assets/images/example.png" alt="Example image">
```

Or for nested directories:

```html
<img src="../assets/images/example.png" alt="Example image">
```

## Best Practices

1. **Use descriptive filenames** - Name files clearly to indicate their content
2. **Organize by type** - Keep similar assets together in the appropriate directory
3. **Optimize images** - Compress images before uploading to reduce file sizes
4. **Use appropriate formats** - SVG for icons/logos, PNG for graphics with transparency, JPG for photos
5. **Include alt text** - Always provide descriptive alt text for accessibility
