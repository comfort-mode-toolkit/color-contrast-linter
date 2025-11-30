from setuptools import setup, find_packages

setup(
    name="color_contrast_linter",
    version="0.1.1",
    description="Automated WCAG color contrast linter for accessibility compliance in CI/CD pipelines.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Lalitha Kanha", # Assuming user name from path, can be updated
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    keywords=["accessibility", "wcag", "color-contrast", "linter", "ci-cd", "design-system", "a11y"],
    install_requires=[
        "cm-colors>=0.5.0",
        "click",
        "rich",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "cc-lint=color_contrast_linter.cli:main",
        ],
    },
)
