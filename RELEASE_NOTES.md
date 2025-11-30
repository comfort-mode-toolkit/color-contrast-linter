# Release Notes - v0.1.0

## Initial Release

We are excited to announce the first release of **Color Contrast Linter**, a CLI tool designed to automate WCAG color contrast compliance checks in your development workflow.

### Key Features

- **Automated Linting**: Check color pairs against WCAG AA and AAA standards.
- **Configurable**: Define your color pairs and contrast requirements in a simple `.color_pairs.yml` file.
- **CLI Commands**:
  - `cc-lint init`: Generate a starter configuration file.
  - `cc-lint lint`: Run the contrast check on your configured pairs.
- **CI/CD Ready**: Easily integrate into GitHub Actions or other CI pipelines to prevent accessibility regressions.
- **Rich Output**: Clear, color-coded terminal output powered by `rich`.

### Installation

```bash
pip install color-contrast-linter
```

### Quick Start

1.  Initialize configuration:
    ```bash
    cc-lint init
    ```
2.  Run the linter:
    ```bash
    cc-lint lint
    ```

### Dependencies

- `cm-colors >= 0.5.0`
- `click`
- `rich`
- `pyyaml`
