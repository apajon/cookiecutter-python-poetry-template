# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `poetry.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
poetry run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/codecov/).

## Development Commands

This project uses Poetry for dependency management and includes several useful development commands:

### Installing Dependencies

```bash
# Install project dependencies
poetry install

# Add a new dependency
poetry add <package-name>

# Add a development dependency
poetry add --group dev <package-name>
```

### Code Quality and Testing

```bash
# Run all quality checks
make check

# Run tests
make test

# Run pre-commit hooks
poetry run pre-commit run --all-files
```

### Code Formatting

This project uses Black for code formatting:

```bash
# Format code with Black
poetry run black .

# Check formatting without making changes
poetry run black --check .
```

### Version Management

This project uses tbump for automated version management:

```bash
# Bump version to 1.2.3 (automatically commits and tags)
poetry run tbump 1.2.3

# Dry run to see what would happen
poetry run tbump --dry-run 1.2.3

# Simple version bump with Poetry (no commit/tag)
poetry version patch|minor|major
```

### Custom Scripts

Example custom scripts are available in the `scripts/` directory. To enable them in pre-commit:

1. Edit `.pre-commit-config.yaml`
2. Uncomment the local hooks section
3. Run `poetry run pre-commit install`

### VSCode Integration

This project includes VSCode settings for:
- Black formatting on save
- Ruff linting
- pytest test discovery
- Python interpreter configuration

## Releasing a new version

{% if cookiecutter.publish_to_pypi == "y" -%}

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/cicd/#how-to-trigger-a-release).
{%- endif %}

---

Repository initiated with [apajon/cookiecutter-python-poetry-template](https://github.com/apajon/cookiecutter-python-poetry-template).
