# /// script
# requires-python = ">=3.13"
# dependencies = ["jinja2"]
# ///

import os
import glob
import argparse
from pathlib import Path
from jinja2 import Template


def get_python_files_content(directory: str) -> list[dict[str, str]]:
    """Get content of all Python files in the specified directory."""
    python_files = []

    # Get all .py files in the directory
    py_files = glob.glob(os.path.join(directory, "*.py"))

    for file_path in py_files:
        file_name = os.path.basename(file_path)

        # Skip files that start with underscore (internal/utility files)
        if file_name.startswith("_"):
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Only include files with content (skip empty files)
            if content.strip():
                python_files.append({
                    'filename': file_name,
                    'content': content
                })
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    # Sort files by filename for consistent output
    python_files.sort(key=lambda x: x['filename'])
    return python_files


def generate_readme(python_files: list[dict[str, str]], output_directory: str, folder_name: str) -> None:
    """Generate README.md with Python file contents in the specified output directory."""

    template_content = """# Python Exercises

[Retroceder](../README.md)

This README contains all Python code files from the {{ folder_name }} folder.

{% for file in python_files %}
## {{ file.filename }}

```python
{{ file.content }}
```

{% endfor %}"""

    template = Template(template_content)
    rendered_content = template.render(python_files=python_files, folder_name=folder_name)

    # Ensure output directory exists
    output_path = Path(output_directory)
    output_path.mkdir(parents=True, exist_ok=True)

    # Create full path for README.md
    readme_file_path = output_path / "README.md"

    try:
        with open(readme_file_path, 'w', encoding='utf-8') as f:
            f.write(rendered_content)
        print(f"README.md generated successfully at: {readme_file_path}")
    except Exception as e:
        print(f"Error writing README.md: {e}")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate README.md from Python files in a directory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python _readme_template.py                           # Current folder as input and output
  python _readme_template.py /path/to/python/files     # Specified input, same as output
  python _readme_template.py /path/to/input /path/to/output  # Both paths specified
  python _readme_template.py . ./output               # Current dir input, different output
        """
    )

    parser.add_argument(
        "input_path",
        type=str,
        nargs='?',  # Make optional
        default=".",  # Default to current directory
        help="Path to the folder containing Python files to parse (default: current directory)"
    )

    parser.add_argument(
        "output_path",
        type=str,
        nargs='?',  # Make optional
        default=None,  # Will be set to input_path if not provided
        help="Path to the folder where README.md will be written (default: same as input_path)"
    )

    return parser.parse_args()


def main() -> None:
    """Main function to generate README.md with all Python files."""
    # Parse command line arguments
    args = parse_arguments()

    # Set default output path to input path if not provided
    if args.output_path is None:
        args.output_path = args.input_path

    # Convert to absolute paths
    input_dir = Path(args.input_path).resolve()
    output_dir = Path(args.output_path).resolve()

    # Validate input directory exists
    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return

    if not input_dir.is_dir():
        print(f"Error: Input path '{input_dir}' is not a directory")
        return

    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")

    # Get the folder name from the input directory
    folder_name = input_dir.name

    # Get all Python files content from input directory
    python_files = get_python_files_content(str(input_dir))

    if not python_files:
        print(f"No Python files found in directory: {input_dir}")
        return

    # Generate the README in output directory
    generate_readme(python_files, str(output_dir), folder_name)

    print(f"Found {len(python_files)} Python files:")
    for file in python_files:
        print(f"  - {file['filename']}")


if __name__ == "__main__":
    main()
