```markdown
# Auto-crop agent for logo images (PR-based)

What it does
- Auto-crops images placed in `logos/` and writes cropped outputs to `cropped/`.
- Runs automatically on pushes that change `logos/**` or via manual workflow_dispatch.
- Opens a pull request containing the cropped images so changes can be reviewed.

How it works
- The workflow runs the autocrop script, writes outputs to `cropped/`, and uses the create-pull-request action to open a PR with only the generated files.
- The PR contains a standard title and body and is labeled `automated, autocrop`.

Notes
- Workflow permissions include contents: write so the PR action can create branches/PRs.
- The job includes a guard to avoid re-running when the actor is the workflow bot.
- Tweak `white_thresh` and `pad` via workflow_dispatch inputs or by adding `.github/auto-crop.yml`.

Testing locally
- Install dependencies: `pip install pillow numpy`
- Run: `python scripts/autocrop.py --input-dir logos_test --output-dir cropped_test --white-thresh 245 --pad 8`
```