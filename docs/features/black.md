# Code Formatting with Black

The generated repository includes [Black](https://black.readthedocs.io/) for automatic Python code formatting. Black provides uncompromising, consistent code formatting with minimal configuration.

## Configuration

Black is configured in `pyproject.toml`:

```toml
[tool.black]
line-length = 120
target-version = ["py39", "py310", "py311", "py312", "py313"]
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
```

## Usage

### Command Line

```bash
# Format all Python files
poetry run black .

# Check formatting without making changes
poetry run black --check .

# See what changes would be made
poetry run black --diff .
```

### VSCode Integration

The template includes VSCode settings that automatically format code with Black when you save files:

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length=120"
    ],
    "editor.formatOnSave": true
}
```

### Pre-commit Integration

Black is automatically included in the pre-commit hooks, so code is formatted before each commit:

```yaml
- repo: https://github.com/psf/black
  rev: "24.1.1"
  hooks:
    - id: black
```

## Benefits

- **Consistent formatting**: No more debates about code style
- **Reduced cognitive load**: Developers can focus on logic, not formatting
- **Automatic fixing**: Formatting issues are fixed automatically
- **Fast**: Black is designed to be very fast
- **Integration**: Works with editors, pre-commit hooks, and CI/CD