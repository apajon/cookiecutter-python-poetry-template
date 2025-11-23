# Version Management with tbump

The generated repository includes [tbump](https://github.com/your-tools/tbump) for automated version management, including version bumping, git commits, and tag creation.

## Configuration

tbump is configured in `pyproject.toml`:

```toml
[tool.tbump]
# tbump configuration for automated version bumping
github_url = "https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}"

[tool.tbump.version]
current = "0.0.1"
regex = '''
  (?P<major>\d+)
  \.
  (?P<minor>\d+)
  \.
  (?P<patch>\d+)
  '''

[tool.tbump.git]
message_template = "Bump to {new_version}"
tag_template = "v{new_version}"
push = true

[[tool.tbump.file]]
src = "pyproject.toml"
search = 'version = "{current_version}"'
```

## Usage

### Basic Version Bumping

```bash
# Bump to a specific version
poetry run tbump 1.2.3

# This will:
# 1. Update version in pyproject.toml
# 2. Create a git commit with message "Bump to 1.2.3"
# 3. Create a git tag "v1.2.3"
# 4. Push the commit and tag to origin
```

### Dry Run

Always test your version bump first:

```bash
# See what would happen without making changes
poetry run tbump --dry-run 1.2.3
```

### Semantic Versioning

tbump works well with semantic versioning:

```bash
# For bug fixes
poetry run tbump 1.2.4

# For new features
poetry run tbump 1.3.0

# For breaking changes
poetry run tbump 2.0.0
```

## Comparison with Poetry Version

| Command | Effect | Git Actions |
|---------|--------|-------------|
| `poetry version patch` | Updates pyproject.toml | None |
| `poetry run tbump 1.2.4` | Updates pyproject.toml | Commits, tags, pushes |

## Workflow Integration

tbump integrates well with CI/CD workflows:

1. **Development**: Use `poetry version` for local development
2. **Release**: Use `tbump` to create official releases
3. **Automation**: CI/CD can detect new tags and trigger release workflows

## Advanced Configuration

You can customize tbump behavior:

```toml
[tool.tbump.git]
message_template = "Release version {new_version}"
tag_template = "release-{new_version}"
push = true

# Update multiple files
[[tool.tbump.file]]
src = "pyproject.toml"
search = 'version = "{current_version}"'

[[tool.tbump.file]]
src = "src/mypackage/__init__.py"
search = '__version__ = "{current_version}"'
```
