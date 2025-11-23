# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Quick Start

This project uses **Poetry** for dependency management and includes essential development tools to help you get started quickly.

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Install Dependencies

Install the project and pre-commit hooks:

```bash
make install
```

This installs all dependencies and sets up pre-commit hooks (Black, Ruff, {{cookiecutter.type_checker}}).

### 3. Fix Initial Formatting

Run formatting and checks to prepare for CI/CD:

```bash
poetry run pre-commit run -a
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development! The CI/CD pipeline will run on pull requests, merges to main, and new releases.

{% if cookiecutter.publish_to_pypi == "y" -%}
To finalize publishing to PyPI, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/publishing/#set-up-for-pypi).
{%- endif %}
{% if cookiecutter.mkdocs == "y" -%}
To enable automatic documentation with MkDocs, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/mkdocs/#enabling-the-documentation-on-github).
{%- endif %}
{% if cookiecutter.codecov == "y" -%}
To enable code coverage reports, see [here](https://apajon.github.io/cookiecutter-python-poetry-template/features/codecov/).
{%- endif %}

## Essential Development Tools

This project includes essential tools for professional Python development:

- **Poetry** - Dependency management
- **Black** - Code formatting
- **Ruff** - Fast linting
- **{{cookiecutter.type_checker}}** - Type checking
- **pytest** - Testing framework
- **pre-commit** - Automated code quality checks
- **tbump** - Version management
{% if cookiecutter.mkdocs == "y" -%}
- **MkDocs** - Documentation
{%- endif %}

### Daily Development Commands

```bash
# Install dependencies
poetry install

# Add a new dependency
poetry add <package-name>

# Run tests
make test

# Run all quality checks (linting, type checking)
make check

# Format code
poetry run black .

# Run pre-commit hooks manually
poetry run pre-commit run -a
```

{% if cookiecutter.mkdocs == "y" -%}
### Documentation

```bash
# Serve documentation locally
make docs

# Build documentation
poetry run mkdocs build
```
{%- endif %}

### Version Bumping

Use tbump for automated version management:

```bash
# Bump to specific version (commits and tags automatically)
poetry run tbump 1.2.3

# Dry run to preview changes
poetry run tbump --dry-run 1.2.3
```

**Using the tbump.sh helper script:**

```bash
# Bump patch version (0.1.0 → 0.1.1)
./scripts/tbump.sh patch

# Bump minor version (0.1.1 → 0.2.0)
./scripts/tbump.sh minor --push

# Dry-run a major version bump
./scripts/tbump.sh major --dry-run
```

## Optional Tools

The following tools are available but not required for basic development. Enable them during project creation or configure them later as needed.

{% if cookiecutter.deptry == 'y' -%}
### Dependency Management (Deptry)

[Deptry](https://github.com/fpgmaas/deptry) detects unused and missing dependencies. Useful for keeping your dependencies clean.

```bash
# Check for dependency issues
{% if cookiecutter.layout == "src" -%}
poetry run deptry src
{%- else -%}
poetry run deptry .
{%- endif %}
```

Configure in `pyproject.toml`:
```toml
[tool.deptry]
ignore_missing = []
ignore_obsolete = []
```
{%- endif %}

{% if cookiecutter.codecov == 'y' -%}
### Code Coverage (Codecov)

[Codecov](https://about.codecov.io/) provides detailed code coverage reports. Useful for tracking test coverage over time and in pull requests.

**Setup required:** Add `CODECOV_TOKEN` to your GitHub repository secrets. See [setup guide](https://apajon.github.io/cookiecutter-python-poetry-template/features/codecov/).

Coverage runs automatically in CI/CD. View reports at `https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}`.
{%- endif %}

{% if cookiecutter.dockerfile == 'y' -%}
### Containerization (Docker)

A `Dockerfile` is included for containerized deployments. Useful for production deployment or ensuring consistent environments.

```bash
# Build the image
docker build -t {{cookiecutter.project_name}} .

# Run the container
docker run {{cookiecutter.project_name}}
```

The Dockerfile uses Poetry for dependency management with multi-stage builds for smaller images, includes a non-root user for security, and optimizes caching of dependencies.
{%- endif %}

{% if cookiecutter.devcontainer == 'y' -%}
### Development Container (VS Code)

A `.devcontainer` configuration is included for use with VS Code, GitHub Codespaces, or other Dev Container-compatible tools. Useful for consistent development environments without local setup.

**Usage:**
- Open in GitHub Codespaces, or
- In VS Code: "Reopen in Container"

**Features:** Pre-configured Python, Poetry, and all extensions.
{%- endif %}

### Additional Development Options

**Custom Scripts:** Example scripts are in `scripts/`. To enable in pre-commit, uncomment the local hooks section in `.pre-commit-config.yaml`.

**VS Code Settings:** Included settings provide Black formatting on save, Ruff linting, and pytest integration.

**Tox:** Multi-version testing is available via `poetry run tox`. See `tox.ini` for configuration.

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
