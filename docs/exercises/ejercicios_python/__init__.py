"""
Modulo de ejercicios Python del Informatorio.

Este modulo genera automaticamente un README.md con todo el codigo Python
del directorio cuando se ejecuta como modulo principal.
"""

import os
import glob


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

            # Only include files with content
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

    # Simple template without Jinja2 dependency for __init__.py
    readme_content = ["# Python Exercises\n"]
    readme_content.append("This README contains all Python code files from the ejercicios_python folder.\n\n")

    for file in python_files:
        readme_content.append(f"## {file['filename']}\n\n")
        readme_content.append("```python\n")
        readme_content.append(file['content'])
        readme_content.append("\n```\n\n")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(readme_content))
        print(f"📝 README.md generated successfully at: {output_path}")
    except Exception as e:
        print(f"❌ Error writing README.md: {e}")


def update_readme() -> None:
    """Main function to generate README.md with all Python files."""
    # Get the current directory where this __init__.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all Python files content
    python_files = get_python_files_content(current_dir)

    if not python_files:
        print("⚠️  No Python files found to include in README.md")
        return

    # Output path for README.md in the same directory
    readme_path = os.path.join(current_dir, "README.md")

    # Generate the README
    generate_readme(python_files, readme_path)

    print(f"✅ Found {len(python_files)} Python files:")
    for file in python_files:
        print(f"   - {file['filename']}")


# Auto-generate README when module is run directly
if __name__ == "__main__":
    print("🚀 Updating README.md with all Python exercises...")
    update_readme()