# Image Processing Functions Built into Git

This repository demonstrates various **image processing and editing functions that can be built into Git** through custom hooks and commands. These tools integrate seamlessly with Git workflows to automate image optimization, format conversion, resizing, and visual comparison.

## Overview

Git can be extended with image processing capabilities in several ways:

1. **Git Hooks** - Automatic processing triggered by Git events
2. **Custom Git Commands** - User-invoked commands following the `git-*` naming convention
3. **Git Attributes & Filters** - Custom merge and diff drivers for images

## 🪝 Git Hooks for Automatic Image Processing

### Pre-commit Hook
**Location:** `.git/hooks/pre-commit` (or `git-hooks/pre-commit` to share with team)

**Purpose:** Automatically optimize images before they are committed to reduce repository size.

**Features:**
- Optimizes PNG files using optipng or pngquant
- Optimizes JPEG files using jpegoptim or jpegtran
- Optimizes GIF files using gifsicle
- Reports size savings
- Re-stages optimized files automatically

**Installation:**
```bash
cp git-hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Post-checkout Hook
**Location:** `.git/hooks/post-checkout` (or `git-hooks/post-checkout`)

**Purpose:** Automatically convert images to modern formats (like WebP) after branch checkout.

**Features:**
- Converts changed images to WebP format
- Only runs on branch checkout
- Configurable via environment variable
- Reports conversion savings

**Installation:**
```bash
cp git-hooks/post-checkout .git/hooks/post-checkout
chmod +x .git/hooks/post-checkout
export GIT_IMAGE_CONVERT_WEBP=1  # Enable WebP conversion
```

## 🛠️ Custom Git Commands

Custom commands are executable scripts named `git-*` placed in your PATH. They can be invoked as `git <command>`.

### git image-optimize
Optimize images to reduce file size without quality loss.

**Installation:**
```bash
cp git-commands/git-image-optimize /usr/local/bin/
chmod +x /usr/local/bin/git-image-optimize
```

**Usage:**
```bash
# Optimize all images in current directory
git image-optimize

# Optimize images in specific path
git image-optimize ./images

# Dry run to preview changes
git image-optimize --dry-run

# Aggressive optimization (slower but better compression)
git image-optimize --aggressive
```

**Requirements:** optipng, jpegoptim, or gifsicle

### git image-resize
Batch resize images to specific dimensions.

**Installation:**
```bash
cp git-commands/git-image-resize /usr/local/bin/
chmod +x /usr/local/bin/git-image-resize
```

**Usage:**
```bash
# Resize all images to 800px width (maintains aspect ratio)
git image-resize . 800

# Resize to specific dimensions
git image-resize ./photos 1920 1080

# Create thumbnails with suffix
git image-resize . 400 --suffix -thumb

# Convert format while resizing
git image-resize . 800 --format webp --quality 90
```

**Requirements:** ImageMagick or GraphicsMagick

### git image-convert
Convert images between formats (PNG, JPEG, WebP, GIF).

**Installation:**
```bash
cp git-commands/git-image-convert /usr/local/bin/
chmod +x /usr/local/bin/git-image-convert
```

**Usage:**
```bash
# Convert all images to WebP
git image-convert . webp

# Convert to PNG and keep originals
git image-convert ./images png --keep

# Convert to JPEG with custom quality
git image-convert . jpg --quality 90

# Dry run
git image-convert . webp --dry-run
```

**Requirements:** 
- For WebP: cwebp/dwebp (webp package)
- For other formats: ImageMagick or GraphicsMagick

### git image-diff
Show visual differences between image versions in Git history.

**Installation:**
```bash
cp git-commands/git-image-diff /usr/local/bin/
chmod +x /usr/local/bin/git-image-diff
```

**Usage:**
```bash
# Compare current version with HEAD
git image-diff logo.png

# Compare with specific commit
git image-diff logo.png HEAD~1
git image-diff logo.png abc123

# Use different comparison tool
git image-diff icon.png --tool composite

# Save diff to specific file
git image-diff banner.png --output my-diff.png
```

**Requirements:** ImageMagick

## 📦 Installation Requirements

### macOS
```bash
brew install imagemagick
brew install webp
brew install optipng jpegoptim gifsicle
```

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install imagemagick
sudo apt-get install webp
sudo apt-get install optipng jpegoptim gifsicle
```

### Fedora/RHEL
```bash
sudo dnf install ImageMagick
sudo dnf install libwebp-tools
sudo dnf install optipng jpegoptim gifsicle
```

## 🎯 Use Cases

### 1. Automatic Repository Size Management
Use the pre-commit hook to ensure all images are optimized before they enter the repository:
```bash
cp git-hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 2. Batch Optimization of Existing Images
Optimize all images in your repository:
```bash
git image-optimize . --aggressive
git add .
git commit -m "Optimize all images"
```

### 3. Generate Thumbnails for Web
Create thumbnail versions of all product images:
```bash
git image-resize ./products 300 --suffix -thumb
```

### 4. Modernize Image Formats
Convert all images to WebP for better web performance:
```bash
git image-convert . webp --keep
```

### 5. Review Image Changes
Visually compare what changed in an image:
```bash
git image-diff screenshot.png HEAD~1
```

### 6. CI/CD Integration
Add image optimization to your CI pipeline:
```yaml
# .github/workflows/optimize-images.yml
name: Optimize Images
on: [pull_request]
jobs:
  optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install tools
        run: sudo apt-get install -y optipng jpegoptim
      - name: Optimize images
        run: |
          chmod +x git-commands/git-image-optimize
          ./git-commands/git-image-optimize .
```

## 🔧 Advanced Configurations

### Git Attributes for Image Diffs
Add to `.gitattributes`:
```
*.png diff=image
*.jpg diff=image
*.gif diff=image
```

Then configure Git to use the image diff command:
```bash
git config diff.image.command 'git-image-diff'
```

### Smart JPEG Compression
For lossy optimization of JPEGs, configure quality levels:
```bash
# Set aggressive quality (higher compression)
git image-convert . jpg --quality 75

# Set high quality (lower compression)
git image-convert . jpg --quality 95
```

### Automated WebP Generation
Set up post-checkout hook to auto-generate WebP versions:
```bash
cp git-hooks/post-checkout .git/hooks/post-checkout
chmod +x .git/hooks/post-checkout
echo "export GIT_IMAGE_CONVERT_WEBP=1" >> ~/.bashrc
```

## 📊 Image Format Comparison

| Format | Best For | Compression | Browser Support | Tool |
|--------|----------|-------------|-----------------|------|
| JPEG | Photos | Lossy | Universal | jpegoptim |
| PNG | Graphics, transparency | Lossless | Universal | optipng |
| WebP | Web images | Both | Modern browsers | cwebp |
| GIF | Animations | Lossless | Universal | gifsicle |

## 🚀 Performance Tips

1. **Use hooks judiciously** - Image processing can slow down Git operations
2. **Optimize before committing** - Run `git image-optimize` on new images
3. **Use dry-run first** - Preview changes with `--dry-run` flag
4. **Batch operations** - Process multiple images at once for efficiency
5. **Choose appropriate quality** - Balance between file size and visual quality

## 🔍 Troubleshooting

### Hook not executing
```bash
# Make sure hook is executable
chmod +x .git/hooks/pre-commit

# Check hook output
GIT_TRACE=1 git commit
```

### Command not found
```bash
# Verify command is in PATH
which git-image-optimize

# Or use full path
/usr/local/bin/git-image-optimize
```

### Missing dependencies
```bash
# Check what's installed
command -v optipng
command -v jpegoptim
command -v convert

# Install missing tools (see Installation Requirements)
```

## 📝 Best Practices

1. **Version control your hooks** - Keep hooks in `git-hooks/` directory and document setup
2. **Test before deployment** - Always use `--dry-run` flag first
3. **Keep originals** - Use `--keep` flag when converting formats
4. **Document your workflow** - Add instructions to your project README
5. **Set quality standards** - Define compression levels for your team
6. **Monitor repository size** - Track the impact of image optimization

## 🤝 Contributing

To add new image processing functions:

1. Create a new `git-*` script in `git-commands/`
2. Follow the existing pattern for argument parsing and help text
3. Include error handling and dry-run mode
4. Test with various image types and edge cases
5. Document in this README

## 📚 Additional Resources

- [Git Hooks Documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [Git Attributes](https://git-scm.com/docs/gitattributes)
- [ImageMagick Documentation](https://imagemagick.org/)
- [WebP Documentation](https://developers.google.com/speed/webp)

## 📄 License

These tools are provided as examples and can be freely used and modified for your projects.
