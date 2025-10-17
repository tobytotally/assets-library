# assets-library

A comprehensive collection of image processing and editing functions built into Git through custom hooks and commands.

## 📋 Overview

This repository demonstrates how to integrate powerful image processing capabilities directly into Git workflows. It includes:

- **Git Hooks** for automatic image optimization and format conversion
- **Custom Git Commands** for batch image processing
- **Visual diff tools** for comparing image changes

## 🚀 Quick Start

### What Can Be Built Into Git?

Git can be extended with various image processing functions:

1. **Automatic Image Optimization** (pre-commit hook)
2. **Format Conversion** (post-checkout hook, custom commands)
3. **Batch Resizing** (custom commands)
4. **Visual Diff** (custom commands)
5. **Quality Control** (CI/CD integration)

See **[IMAGE_PROCESSING.md](IMAGE_PROCESSING.md)** for complete documentation.

### Available Tools

#### Git Hooks
- `git-hooks/pre-commit` - Automatically optimize images before commit
- `git-hooks/post-checkout` - Auto-convert images to WebP after checkout

#### Custom Git Commands
- `git image-optimize` - Optimize images to reduce file size
- `git image-resize` - Batch resize images
- `git image-convert` - Convert between image formats
- `git image-diff` - Visual diff for images

### Installation

1. **Install dependencies:**
   ```bash
   # macOS
   brew install imagemagick webp optipng jpegoptim gifsicle
   
   # Ubuntu/Debian
   sudo apt-get install imagemagick webp optipng jpegoptim gifsicle
   ```

2. **Install hooks (optional):**
   ```bash
   cp git-hooks/pre-commit .git/hooks/
   chmod +x .git/hooks/pre-commit
   ```

3. **Install commands (optional):**
   ```bash
   cp git-commands/* /usr/local/bin/
   chmod +x /usr/local/bin/git-image-*
   ```

### Usage Examples

```bash
# Optimize all images in repository
git image-optimize .

# Resize images to 800px width
git image-resize ./images 800

# Convert all images to WebP
git image-convert . webp

# Compare image with previous version
git image-diff logo.png HEAD~1
```

## 📖 Documentation

For complete documentation on all image processing functions, see **[IMAGE_PROCESSING.md](IMAGE_PROCESSING.md)**.

## 🎯 Use Cases

- **Repository Size Management** - Automatically optimize images to keep repo size small
- **Web Performance** - Convert images to modern formats like WebP
- **Asset Generation** - Batch create thumbnails and different sizes
- **Code Reviews** - Visual diff to review image changes
- **CI/CD Integration** - Automated image processing in pipelines

## 📝 License

These tools are provided as examples and can be freely used and modified for your projects.
