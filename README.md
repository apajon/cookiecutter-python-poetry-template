<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/apajon/cookiecutter-python-poetry-template/main/docs/static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/apajon/cookiecutter-python-poetry-template/main.yml?branch=main)](https://github.com/apajon/cookiecutter-python-poetry-template/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/apajon/cookiecutter-python-poetry-template/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://apajon.github.io/cookiecutter-python-poetry-template/)
[![License](https://img.shields.io/github/license/apajon/cookiecutter-python-poetry-template)](https://img.shields.io/github/license/apajon/cookiecutter-python-poetry-template)

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- [Black](https://black.readthedocs.io/) for code formatting
- [tbump](https://github.com/your-tools/tbump) for automated version bumping and tagging
- Custom scripts directory with examples for local pre-commit hooks
- Supports both [src and flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/)/[ty](https://docs.astral.sh/ty/) and [deptry](https://github.com/fpgmaas/deptry/).
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Containerization with [Docker](https://www.docker.com/) or [Podman](https://podman.io/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)
- VSCode settings for optimal development experience

---

<p align="center">
  <a href="https://apajon.github.io/cookiecutter-python-poetry-template/">Documentation</a> - <a href="https://github.com/apajon/cookiecutter-python-poetry-example">Example</a>
</p>

---

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
pip install cookiecutter
cookiecutter https://github.com/apajon/cookiecutter-python-poetry-template.git
```

or with pipx:

```bash
pipx run cookiecutter https://github.com/apajon/cookiecutter-python-poetry-template.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

## Key Features

### Poetry Integration
- Modern dependency management with `poetry install` and `poetry add`
- Poetry virtual environment management
- Poetry build system for packaging

### Black Code Formatting
- Automatic code formatting with Black
- Pre-commit hook integration
- VSCode integration for format-on-save

### Version Management with tbump
- Automated version bumping: `tbump 1.2.3`
- Automatic git commit and tag creation
- Configurable version pattern matching

### Custom Scripts Support
- `scripts/` directory with example bash and python scripts
- Template for local pre-commit hooks (disabled by default)
- Easy integration with your development workflow

### Enhanced Developer Experience
- VSCode settings for Black, Ruff, and pytest
- Pre-commit hooks with Black, Ruff, and optional mypy
- Docker/Podman containerization support

## Acknowledgements

This project is partially based on [Audrey
Feldroy\'s](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository and [fpgmaas](https://github.com/fpgmaas)'s [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) template.
