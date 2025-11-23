# Custom Scripts and Local Hooks

The generated repository includes a `scripts/` directory with example scripts that can be integrated into your development workflow via local pre-commit hooks.

## Scripts Directory Structure

```
scripts/
├── myscript.sh     # Example bash script
└── myscript.py     # Example Python script
```

## Example Scripts

### Bash Script (myscript.sh)

```bash
#!/bin/bash

# Example bash script for local pre-commit hooks
# This script is not enabled by default but can be integrated via a local hook

echo "[myscript.sh] Script Bash exécuté"

# Add your custom bash logic here
# For example: code formatting, linting, or file validation
```

### Python Script (myscript.py)

```python
#!/usr/bin/env python3

"""
Example Python script for local pre-commit hooks
This script is not enabled by default but can be integrated via a local hook
"""

import sys

def main():
    """Main function that prints script execution and arguments."""
    print("[myscript.py] Script Python exécuté")

    if len(sys.argv) > 1:
        print(f"Arguments reçus: {sys.argv[1:]}")
    else:
        print("Aucun argument fourni")

    # Add your custom Python logic here
    # For example: code analysis, custom linting, or file processing

    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Enabling Custom Scripts in Pre-commit

The scripts are disabled by default. To enable them, edit `.pre-commit-config.yaml` and uncomment the local hooks section:

```yaml
# Example of local hooks for custom scripts (disabled by default)
# Uncomment the following section to enable custom hooks:

- repo: local
  hooks:
    - id: custom-bash-script
      name: Custom Bash Script
      entry: ./scripts/myscript.sh
      language: system
      files: \.py$
      # pass_filenames: false  # Uncomment if script doesn't need filenames

    - id: custom-python-script
      name: Custom Python Script
      entry: python ./scripts/myscript.py
      language: python
      files: \.py$
      # pass_filenames: false  # Uncomment if script doesn't need filenames
```

After uncommenting, reinstall the pre-commit hooks:

```bash
poetry run pre-commit install
```

## Use Cases for Custom Scripts

### Code Quality Checks
- Custom linting rules specific to your project
- Code complexity analysis
- Documentation coverage checks

### File Validation
- Check for required file headers
- Validate configuration files
- Ensure proper file naming conventions

### Project-Specific Rules
- Database migration validation
- API contract validation
- Custom security checks

### Integration Testing
- Quick smoke tests before commit
- Integration with external tools
- Custom build validation

## Script Configuration Options

### Language Options

```yaml
# For bash/shell scripts
- id: my-script
  language: system
  entry: ./scripts/myscript.sh

# For Python scripts
- id: my-script
  language: python
  entry: python ./scripts/myscript.py

# For any executable
- id: my-script
  language: system
  entry: ./scripts/myscript
```

### File Filtering

```yaml
# Run only on Python files
files: \.py$

# Run only on specific directories
files: ^src/

# Exclude certain files
exclude: ^tests/

# Run on all files
files: .*
```

### Argument Handling

```yaml
# Pass filenames to the script
pass_filenames: true  # default

# Don't pass filenames (useful for project-wide checks)
pass_filenames: false

# Always run, even if no files match
always_run: true
```

## Best Practices

1. **Make scripts executable**: `chmod +x scripts/myscript.sh`
2. **Include clear documentation**: Add comments explaining what each script does
3. **Handle errors gracefully**: Use proper exit codes (0 for success, non-zero for failure)
4. **Keep scripts focused**: Each script should have a single, clear purpose
5. **Test scripts independently**: Ensure scripts work outside of pre-commit context
6. **Use consistent naming**: Follow a naming convention for your scripts
