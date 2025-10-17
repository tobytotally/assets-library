#!/bin/bash
# Example: Setup image processing in a new repository

echo "Setting up image processing for Git repository..."
echo ""

# 1. Install git hooks
echo "1. Installing Git hooks..."
if [ -d ".git/hooks" ]; then
    cp ../git-hooks/pre-commit .git/hooks/
    cp ../git-hooks/post-checkout .git/hooks/
    chmod +x .git/hooks/pre-commit
    chmod +x .git/hooks/post-checkout
    echo "   ✓ Hooks installed"
else
    echo "   ✗ Not a Git repository"
fi

echo ""

# 2. Install custom commands (optional)
echo "2. Installing custom Git commands (requires sudo)..."
read -p "   Install git-image-* commands to /usr/local/bin? [y/N] " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo cp ../git-commands/git-image-* /usr/local/bin/
    sudo chmod +x /usr/local/bin/git-image-*
    echo "   ✓ Commands installed"
else
    echo "   → Skipped. Add git-commands/ to your PATH manually if needed"
fi

echo ""

# 3. Configure Git attributes
echo "3. Configuring Git attributes for image diff..."
if [ ! -f ".gitattributes" ]; then
    cat > .gitattributes << 'EOF'
# Image processing attributes
*.png diff=image
*.jpg diff=image
*.jpeg diff=image
*.gif diff=image
*.webp diff=image
EOF
    echo "   ✓ .gitattributes created"
else
    echo "   → .gitattributes already exists"
fi

echo ""

# 4. Set up environment variables
echo "4. Setting up environment variables..."
echo "   Add these to your shell profile (~/.bashrc or ~/.zshrc):"
echo ""
echo "   export GIT_IMAGE_CONVERT_WEBP=1  # Enable WebP conversion"
echo ""

# 5. Verify installation
echo "5. Verifying dependencies..."
echo ""

check_command() {
    if command -v $1 &> /dev/null; then
        echo "   ✓ $1 installed"
        return 0
    else
        echo "   ✗ $1 not installed"
        return 1
    fi
}

check_command "optipng"
check_command "jpegoptim"
check_command "gifsicle"
check_command "convert"
check_command "cwebp"

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Review IMAGE_PROCESSING.md for detailed documentation"
echo "  2. Install any missing dependencies"
echo "  3. Test with: git image-optimize --help"
