# Quick Reference: Image Processing in Git

## 🪝 Git Hooks

### Pre-commit Hook (Auto-optimize)
```bash
# Install
cp git-hooks/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit

# Now images are automatically optimized on commit!
```

### Post-checkout Hook (Auto-convert to WebP)
```bash
# Install
cp git-hooks/post-checkout .git/hooks/
chmod +x .git/hooks/post-checkout

# Enable WebP conversion
export GIT_IMAGE_CONVERT_WEBP=1

# Now images are converted to WebP on branch checkout!
```

## 🛠️ Custom Commands

### git image-optimize
```bash
git image-optimize [path] [options]

# Examples
git image-optimize .                    # Optimize all images
git image-optimize ./images             # Optimize specific directory
git image-optimize . --dry-run          # Preview changes
git image-optimize . --aggressive       # Maximum compression
```

**Optimizes:** PNG (optipng/pngquant), JPEG (jpegoptim), GIF (gifsicle)

### git image-resize
```bash
git image-resize [path] <width> [height] [options]

# Examples
git image-resize . 800                  # Resize to 800px width
git image-resize ./photos 1920 1080    # Resize to 1920x1080
git image-resize . 400 --suffix -thumb # Create thumbnails
git image-resize . 800 --format webp   # Resize and convert
```

**Requires:** ImageMagick or GraphicsMagick

### git image-convert
```bash
git image-convert [path] <format> [options]

# Examples
git image-convert . webp                # Convert all to WebP
git image-convert ./images png --keep   # Convert to PNG, keep originals
git image-convert . jpg --quality 90    # Convert to JPEG
git image-convert . webp --dry-run      # Preview conversion
```

**Formats:** jpg, png, webp, gif

### git image-diff
```bash
git image-diff <file> [commit] [options]

# Examples
git image-diff logo.png                 # Compare with HEAD
git image-diff logo.png HEAD~1          # Compare with previous commit
git image-diff icon.png --tool composite
git image-diff banner.png --output diff.png
```

**Requires:** ImageMagick

## 📦 Installation Cheat Sheet

### macOS
```bash
brew install imagemagick webp optipng jpegoptim gifsicle
```

### Ubuntu/Debian
```bash
sudo apt-get install imagemagick webp optipng jpegoptim gifsicle
```

### Fedora/RHEL
```bash
sudo dnf install ImageMagick libwebp-tools optipng jpegoptim gifsicle
```

## 🎯 Common Workflows

### 1. New Project Setup
```bash
# Install hooks
cp git-hooks/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit

# Install commands
sudo cp git-commands/* /usr/local/bin/
sudo chmod +x /usr/local/bin/git-image-*

# Configure Git attributes
cat >> .gitattributes << EOF
*.png diff=image
*.jpg diff=image
*.gif diff=image
*.webp diff=image
EOF
```

### 2. Optimize Existing Repository
```bash
# Optimize all images
git image-optimize . --aggressive

# Commit optimized images
git add .
git commit -m "Optimize all images"
```

### 3. Web Performance
```bash
# Convert to WebP (keep originals for fallback)
git image-convert . webp --keep

# Create responsive sizes
git image-resize . 300 --suffix -sm
git image-resize . 768 --suffix -md
git image-resize . 1920 --suffix -lg
```

### 4. Code Review
```bash
# Visual diff of changed image
git image-diff screenshot.png HEAD~1

# View the diff
open /tmp/image-diff.png
```

## 🔧 Configuration

### Git Config
```bash
# Set image diff command
git config diff.image.command 'git-image-diff'

# Set default quality for conversions
git config image.quality 85
```

### Environment Variables
```bash
# Enable WebP conversion in post-checkout hook
export GIT_IMAGE_CONVERT_WEBP=1
```

## 📊 File Size Impact

| Format | Use Case | Typical Savings |
|--------|----------|-----------------|
| PNG → Optimized PNG | Graphics | 20-40% |
| JPEG → Optimized JPEG | Photos | 10-30% |
| PNG/JPEG → WebP | Web | 25-50% |
| GIF → Optimized GIF | Animations | 10-30% |

## 🚨 Troubleshooting

```bash
# Check if hooks are executable
ls -la .git/hooks/pre-commit

# Make hook executable
chmod +x .git/hooks/pre-commit

# Test hook manually
.git/hooks/pre-commit

# Verify commands are in PATH
which git-image-optimize

# Check for required tools
command -v optipng && echo "optipng installed"
command -v jpegoptim && echo "jpegoptim installed"
command -v convert && echo "ImageMagick installed"
command -v cwebp && echo "WebP tools installed"
```

## 📚 Learn More

- Full documentation: [IMAGE_PROCESSING.md](IMAGE_PROCESSING.md)
- Examples: [examples/](examples/)
- Git Hooks: [git-hooks/](git-hooks/)
- Commands: [git-commands/](git-commands/)
