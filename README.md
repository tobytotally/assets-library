```markdown
# Auto-crop agent for logo images

What it does
- Auto-crops images placed in `logos/` and writes cropped outputs to `cropped/`.
- Runs automatically on pushes that change `logos/**` or via manual workflow_dispatch.
- Opens a pull request containing the cropped images so changes can be reviewed.

How to use
1. Copy the files into your repository (workflow + scripts).
2. Adjust parameters in `.github/workflows/autocrop.yml` environment variables or update `.github/auto-crop.yml`.
3. Make a test change under `logos/` and push — a workflow will run and, if there are outputs, open a PR `autocrop/changes`.

Customization
- Use ImageMagick instead of Pillow by modifying the workflow to `apt-get install imagemagick` and replacing the processing step with `magick` commands.
- For heavy volumes, consider running the processor on a self-hosted runner or an external service (serverless) and only push results to the repo when ready.

Notes
- The workflow uses the repo's GITHUB_TOKEN to create the PR. If you want a dedicated bot identity, create a machine user or GitHub App with a token and use that.
- Keep originals in the repo; cropped outputs are stored under `cropped/` for easy review.

License
- The script uses Pillow and numpy (open source). Verify licenses if you plan to ship in a commercial product.
```