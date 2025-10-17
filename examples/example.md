# Example Markdown File

This file demonstrates how to reference assets from the assets library in a markdown document.

## Images

Here's an example image from the assets library:

![Example Image](../assets/images/example.svg)

## Icons

You can also use icons in your markdown:

![Checkmark Icon](../assets/icons/checkmark.svg)

## Inline Images

Images can be used inline with text. Here's a checkmark: ![checkmark](../assets/icons/checkmark.svg) embedded in a sentence.

## Links to Documents

You can link to other documents stored in the assets library:

[View Sample Document](../assets/documents/sample.md)

## Image with Custom Size (HTML in Markdown)

<img src="../assets/images/example.svg" alt="Example Image" width="100" height="100">

## Multiple Images

You can display multiple images:

| Image 1 | Image 2 |
|---------|---------|
| ![Example](../assets/images/example.svg) | ![Checkmark](../assets/icons/checkmark.svg) |

## Best Practices

1. Always use descriptive alt text for accessibility
2. Use relative paths for portability
3. Consider image sizes for page load performance
4. Organize assets logically in the appropriate directories

## Reference Types

### Relative Path (Recommended for local use)
```markdown
![Alt text](../assets/images/example.svg)
```

### Absolute GitHub URL (For external references)
```markdown
![Alt text](https://raw.githubusercontent.com/tobytotally/assets-library/main/assets/images/example.svg)
```
