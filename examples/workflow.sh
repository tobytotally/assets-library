#!/bin/bash
# Example workflow: Optimizing images for a web project

echo "Image Optimization Workflow Example"
echo "===================================="
echo ""

# Sample workflow directory
WORKFLOW_DIR="/tmp/image-workflow-demo"
mkdir -p "$WORKFLOW_DIR"
cd "$WORKFLOW_DIR"

echo "This example demonstrates a complete workflow for:"
echo "  1. Setting up a repository with image processing"
echo "  2. Adding and optimizing images"
echo "  3. Converting to web-friendly formats"
echo "  4. Generating responsive image sizes"
echo ""

# Initialize a demo repository
echo "Step 1: Initialize repository"
git init
echo "  ✓ Repository initialized"
echo ""

# Install hooks from the assets-library
HOOKS_DIR="/home/runner/work/assets-library/assets-library/git-hooks"
if [ -d "$HOOKS_DIR" ]; then
    echo "Step 2: Install image processing hooks"
    cp "$HOOKS_DIR/pre-commit" .git/hooks/
    chmod +x .git/hooks/pre-commit
    echo "  ✓ Pre-commit hook installed (auto-optimize images)"
    echo ""
fi

# Create sample images (placeholders)
echo "Step 3: Create sample images"
mkdir -p images

# Note: In a real scenario, you'd have actual images
# For this demo, we'll show the commands that would be used
echo "  In a real workflow, you would:"
echo "    - Add your images to the repository"
echo "    - Commit them (pre-commit hook optimizes automatically)"
echo ""

# Show optimization workflow
echo "Step 4: Manual optimization workflow"
echo "  # Optimize all images"
echo "  git image-optimize ./images"
echo ""
echo "  # Optimize with aggressive compression"
echo "  git image-optimize ./images --aggressive"
echo ""
echo "  # Dry run to preview changes"
echo "  git image-optimize ./images --dry-run"
echo ""

# Show format conversion workflow
echo "Step 5: Convert to modern formats"
echo "  # Convert all images to WebP for web"
echo "  git image-convert ./images webp --keep"
echo ""
echo "  # This creates .webp versions alongside originals"
echo "  # HTML can use <picture> with fallbacks:"
echo '  <picture>'
echo '    <source srcset="image.webp" type="image/webp">'
echo '    <img src="image.jpg" alt="...">'
echo '  </picture>'
echo ""

# Show responsive images workflow
echo "Step 6: Generate responsive image sizes"
echo "  # Create thumbnail versions"
echo "  git image-resize ./images 300 --suffix -thumb"
echo ""
echo "  # Create medium size for tablets"
echo "  git image-resize ./images 768 --suffix -md"
echo ""
echo "  # Create large size for desktop"
echo "  git image-resize ./images 1920 --suffix -lg"
echo ""
echo "  # Result:"
echo "    image.jpg          # Original"
echo "    image-thumb.jpg    # 300px wide"
echo "    image-md.jpg       # 768px wide"
echo "    image-lg.jpg       # 1920px wide"
echo ""

# Show diff workflow
echo "Step 7: Review image changes"
echo "  # When images change, use visual diff"
echo "  git image-diff logo.png"
echo ""
echo "  # Compare with specific commit"
echo "  git image-diff banner.jpg HEAD~3"
echo ""
echo "  # Creates a visual diff highlighting changes"
echo ""

# Show CI/CD integration
echo "Step 8: CI/CD Integration"
echo "  # Example GitHub Actions workflow:"
echo ""
cat << 'EOF'
  # .github/workflows/images.yml
  name: Optimize Images
  on:
    pull_request:
      paths:
        - '**.png'
        - '**.jpg'
        - '**.jpeg'
        - '**.gif'
  
  jobs:
    optimize:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        
        - name: Install tools
          run: |
            sudo apt-get update
            sudo apt-get install -y optipng jpegoptim gifsicle
        
        - name: Optimize images
          run: |
            chmod +x git-commands/git-image-optimize
            ./git-commands/git-image-optimize . --aggressive
        
        - name: Commit optimized images
          run: |
            git config user.name "Image Bot"
            git config user.email "bot@example.com"
            git add -A
            git diff --quiet && git diff --staged --quiet || \
              git commit -m "Optimize images"
            git push
EOF

echo ""
echo ""

# Summary
echo "Workflow Summary"
echo "================"
echo ""
echo "This workflow demonstrates:"
echo "  ✓ Automatic optimization via pre-commit hooks"
echo "  ✓ Manual batch optimization with git image-optimize"
echo "  ✓ Format conversion to WebP with git image-convert"
echo "  ✓ Responsive image generation with git image-resize"
echo "  ✓ Visual diff for reviewing changes with git image-diff"
echo "  ✓ CI/CD integration for automated processing"
echo ""
echo "For more details, see IMAGE_PROCESSING.md"
echo ""

# Cleanup
echo "Demo directory created at: $WORKFLOW_DIR"
echo "You can explore it or delete it with: rm -rf $WORKFLOW_DIR"
