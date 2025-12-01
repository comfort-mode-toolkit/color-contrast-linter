# Color Contrast Linter - Automated Accessibility Testing

![License](https://img.shields.io/pypi/l/color-contrast-linter)
![Monthly Downloads](https://img.shields.io/pypi/dm/color-contrast-linter)
![Python Version](https://img.shields.io/pypi/v/color-contrast-linter)


**Color Contrast Linter** is a powerful CLI tool designed to automate **WCAG 2.1** color contrast compliance checks. It helps developers and designers ensure their color palettes meet **AA** and **AAA** accessibility standards directly within their workflow or **CI/CD pipeline**.

Built on top of `cm-colors`, this tool prevents accessibility regressions by linting your design tokens and color pairs against strict contrast ratio requirements.

## Key Features

- **Automated WCAG Compliance**: Instantly verify if your color pairs meet WCAG AA (4.5:1) or AAA (7.0:1) standards.
- **CI/CD Integration**: Seamlessly integrate with GitHub Actions, GitLab CI, and other pipelines to block inaccessible code.
- **Design System Friendly**: Perfect for linting design tokens, themes, and CSS variables.
- **Flexible Configuration**: Define custom color pairs and contrast thresholds in a simple YAML file.
- **Rich Reporting**: Get clear, color-coded output in your terminal identifying passing and failing pairs.

## Installation

Install the package via pip:

```bash
pip install color-contrast-linter
```

## Usage

### 1. Initialize Configuration

Start by creating a configuration file. Run the `init` command to generate a `.color_pairs.yml` file in your project root:

```bash
cc-lint init
```

This file allows you to define the minimum contrast standard (`AA` or `AAA`) and list the color pairs you want to test.

**Example `.color_pairs.yml`:**

```yaml
min_contrast: AA
pairs:
  - foreground: "#000000"
    background: "#ffffff"
  - foreground: "#767676" # Might fail AA for normal text
    background: "#ffffff"
```

### 2. Run the Linter

Execute the `lint` command to check your configured color pairs for accessibility issues:

```bash
cc-lint lint
```

The tool will analyze each pair and report:
- **Pass/Fail status** based on your `min_contrast` setting.
- **Actual contrast ratio** (e.g., 21.0:1).
- **WCAG Level** achieved (AA, AAA, or Fail).

## CI/CD Integration for Accessibility

Automate your accessibility testing by adding `color-contrast-linter` to your CI/CD workflow. This ensures that no new color combinations violate accessibility standards.

### GitHub Actions Example

Add the following step to your `.github/workflows/ci.yml`:

```yaml
steps:
  - uses: actions/checkout@v4
  
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.x'
      
  - name: Install Color Contrast Linter
    run: pip install color-contrast-linter
    
  - name: Run Accessibility Lint
    run: cc-lint lint
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests, report bugs, and suggest features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
