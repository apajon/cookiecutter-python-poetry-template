# Dependency management with Poetry

The generated repository uses [Poetry](https://python-poetry.org/)
for its dependency management. When you have created your repository
using this cookiecutter template, a Poetry environment is pre-configured
in `pyproject.toml`. All you need to do is add your
project-specific dependencies with

```bash
poetry add <package>
```

For development dependencies:

```bash
poetry add --group dev <package>
```

and then install the environment with

```bash
poetry install
```

You can then run commands within your virtual environment, for example:

```bash
poetry run python -m pytest
```

## Poetry Commands

Here are some useful Poetry commands:

### Managing Dependencies

```bash
# Add a production dependency
poetry add requests

# Add a development dependency
poetry add --group dev pytest

# Remove a dependency
poetry remove requests

# Update all dependencies
poetry update

# Update a specific dependency
poetry update requests
```

### Environment Management

```bash
# Install dependencies from pyproject.toml
poetry install

# Install only production dependencies
poetry install --without dev

# Show virtual environment info
poetry env info

# Activate shell with virtual environment
poetry shell
```

### Building and Publishing

```bash
# Build the package
poetry build

# Publish to PyPI
poetry publish

# Build and publish
poetry publish --build
```
