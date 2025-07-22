# /// script
# requires-python = ">=3.13"
# dependencies = ["jinja2"]
# ///

import os
import glob
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


def generate_readme(python_files: list[dict[str, str]], output_path: str) -> None:
    """Generate README.md with Python file contents."""

    template_content = """# Python Exercises

This README contains all Python code files from the ejercicios_python folder.

{% for file in python_files %}
## {{ file.filename }}

```python
{{ file.content }}
```

{% endfor %}"""

    template = Template(template_content)
    rendered_content = template.render(python_files=python_files)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_content)
        print(f"README.md generated successfully at: {output_path}")
    except Exception as e:
        print(f"Error writing README.md: {e}")


def main() -> None:
    """Main function to generate README.md with all Python files."""
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all Python files content
    python_files = get_python_files_content(current_dir)

    if not python_files:
        print("No Python files found to include in README.md")
        return

    # Output path for README.md in the same directory
    readme_path = os.path.join(current_dir, "README.md")

    # Generate the README
    generate_readme(python_files, readme_path)

    print(f"Found {len(python_files)} Python files:")
    for file in python_files:
        print(f"  - {file['filename']}")


if __name__ == "__main__":
    main()
