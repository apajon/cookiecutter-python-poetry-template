.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using Poetry"
	@poetry install
	@poetry run pre-commit install

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running {{ cookiecutter.type_checker }}"
	@poetry run {% if cookiecutter.type_checker == "mypy" %}mypy{% else %}ty check{% endif %}
{%- if cookiecutter.deptry == 'y' %}
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry {% if cookiecutter.layout == "src" %}src{% else %}.{% endif %}
{%- endif %}

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@poetry run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml
{%- else %}
	@poetry run python -m pytest --doctest-modules
{%- endif%}

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "🚀 Removing build artifacts"
	@poetry run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

{%- if cookiecutter.publish_to_pypi == "y"%}

.PHONY: publish
publish: ## Publish a release to PyPI.
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.
{%- endif%}

{%- if cookiecutter.mkdocs == "y" %}

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

{%- endif %}

.PHONY: help
help:
	@poetry run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
