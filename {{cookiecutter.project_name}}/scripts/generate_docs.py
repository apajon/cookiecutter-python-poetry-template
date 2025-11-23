#!/usr/bin/env python3
"""Auto-generate mkdocs documentation from package structure.

This script discovers Python modules in the project and generates
markdown documentation files for mkdocs with mkdocstrings.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Set


def find_package_root() -> Path:
    """Find the root directory of the Python package.

    Returns:
        Path to the package root directory.

    Raises:
        RuntimeError: If no package structure is found.
    """
    current_dir = Path.cwd()

    # Check for src layout first
    src_dir = current_dir / "src"
    if src_dir.exists():
        for item in src_dir.iterdir():
            if item.is_dir() and (item / "__init__.py").exists():
                return item

    # Check for flat layout
    for item in current_dir.iterdir():
        if (item.is_dir() and
            (item / "__init__.py").exists() and
            item.name not in {"tests", "docs", ".git", ".venv", "__pycache__"}):
            return item

    raise RuntimeError("No Python package found in current directory")


def discover_modules(package_root: Path) -> List[str]:
    """Discover all Python modules in the package.

    Args:
        package_root: Root directory of the package.

    Returns:
        List of module paths suitable for mkdocstrings.
    """
    modules = []
    package_name = package_root.name

    def _scan_directory(directory: Path, module_prefix: str = ""):
        """Recursively scan directory for Python modules."""
        current_prefix = f"{package_name}.{module_prefix}" if module_prefix else package_name

        # Add the package/subpackage itself if it has __init__.py
        if (directory / "__init__.py").exists():
            modules.append(current_prefix)

        # Scan for Python files and subdirectories
        for item in sorted(directory.iterdir()):
            if item.is_file() and item.suffix == ".py" and item.name != "__init__.py":
                module_name = item.stem
                full_module = f"{current_prefix}.{module_name}"
                modules.append(full_module)
            elif (item.is_dir() and
                  not item.name.startswith(".") and
                  not item.name.startswith("__pycache__")):
                submodule_prefix = f"{module_prefix}.{item.name}" if module_prefix else item.name
                _scan_directory(item, submodule_prefix)

    _scan_directory(package_root)
    return sorted(modules)


def generate_modules_md(modules: List[str], output_path: Path) -> None:
    """Generate modules.md file with mkdocstrings references.

    Args:
        modules: List of module paths.
        output_path: Path to write the modules.md file.
    """
    content = []
    content.append("# API Reference")
    content.append("")
    content.append("This page contains the API reference for all modules in the project.")
    content.append("")

    for module in modules:
        # Create a section header
        module_title = module.replace(".", " → ").title()
        content.append(f"## {module_title}")
        content.append("")
        content.append(f"::: {module}")
        content.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))


def generate_individual_docs(modules: List[str], docs_dir: Path) -> None:
    """Generate individual documentation files for each module.

    Args:
        modules: List of module paths.
        docs_dir: Documentation directory.
    """
    api_dir = docs_dir / "api"
    api_dir.mkdir(exist_ok=True)

    for module in modules:
        # Create filename from module path
        filename = module.replace(".", "_") + ".md"
        filepath = api_dir / filename

        content = []
        content.append(f"# {module}")
        content.append("")
        content.append(f"::: {module}")
        content.append("")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(content))


def update_mkdocs_nav(modules: List[str], mkdocs_path: Path) -> None:
    """Update mkdocs.yml navigation to include all modules.

    Args:
        modules: List of module paths.
        mkdocs_path: Path to mkdocs.yml file.
    """
    if not mkdocs_path.exists():
        return

    # Read current mkdocs.yml
    with open(mkdocs_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find nav section and update it
    lines = content.split("\n")
    nav_start = None
    nav_end = None
    indent_level = None

    for i, line in enumerate(lines):
        if line.strip().startswith("nav:"):
            nav_start = i
            # Find the indentation level of nav items
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and not lines[j].startswith(" "):
                    nav_end = j
                    break
                elif lines[j].strip() and lines[j].startswith("  - "):
                    if indent_level is None:
                        indent_level = len(lines[j]) - len(lines[j].lstrip())
            break

    if nav_start is not None:
        if nav_end is None:
            nav_end = len(lines)

        # Create new nav section
        new_nav = [lines[nav_start]]
        new_nav.append("  - Home: index.md")
        new_nav.append("  - API Reference: modules.md")

        # Add individual module pages if they exist
        api_dir = Path("docs/api")
        if api_dir.exists() and any(api_dir.iterdir()):
            new_nav.append("  - Modules:")
            for module in modules:
                filename = module.replace(".", "_") + ".md"
                module_title = module.split(".")[-1].title()
                new_nav.append(f"    - {module_title}: api/{filename}")

        # Replace the nav section
        new_content = lines[:nav_start] + new_nav + lines[nav_end:]

        with open(mkdocs_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_content))


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Generate mkdocs documentation from package structure")
    parser.add_argument("--individual", action="store_true",
                       help="Generate individual documentation files for each module")
    parser.add_argument("--update-nav", action="store_true",
                       help="Update mkdocs.yml navigation")
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"),
                       help="Documentation directory (default: docs)")

    args = parser.parse_args()

    try:
        # Find package root
        package_root = find_package_root()
        print(f"Found package: {package_root.name}")

        # Discover modules
        modules = discover_modules(package_root)
        print(f"Discovered {len(modules)} modules:")
        for module in modules:
            print(f"  - {module}")

        # Ensure docs directory exists
        args.docs_dir.mkdir(exist_ok=True)

        # Generate modules.md
        modules_path = args.docs_dir / "modules.md"
        generate_modules_md(modules, modules_path)
        print(f"Generated: {modules_path}")

        # Generate individual documentation files if requested
        if args.individual:
            generate_individual_docs(modules, args.docs_dir)
            print(f"Generated individual docs in: {args.docs_dir / 'api'}")

        # Update mkdocs.yml navigation if requested
        if args.update_nav:
            mkdocs_path = Path("mkdocs.yml")
            update_mkdocs_nav(modules, mkdocs_path)
            print(f"Updated navigation in: {mkdocs_path}")

    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
