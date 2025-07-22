# Informatorio Codebase Guide

## Project Overview

This is an educational repository for ### Adding New Content

1. Follow the `semana{N}.md` pattern for sequential lessons with YouTube video thumbnails
2. Include YouTube links using
   `[![Title](https://img.youtube.com/vi/VIDEO_ID/default.jpg)](https://youtu.be/VIDEO_ID)` format
3. Reference PDF and PPT materials with descriptive labels and correct file paths
4. Add navigation breadcrumbs `[Retroceder](../README.md)` to all markdown files
5. Use Spanish for explanations, English for code
6. For Etapa 2: Use collapsible `<details><summary>` sections for weekly content

### Python Scripts

1. Include uv inline script metadata (`# /// script` blocks) for dependency management
2. Add comprehensive docstrings in Spanish explaining purpose and functionality
3. Use modern type hints (`list[int]`, `dict[str, int]`) for Python 3.9+
4. Implement robust error handling with Spanish user messages
5. Test with `uv run script_name.py`
6. Follow the pattern: skip files starting with `_` for internal/utility scripts

### Documentation Generation

1. Use `scripts/_readme_template.py` to auto-generate README files from Python code
2. Run manually: `uv run scripts/_readme_template.py path/to/folder`
3. GitHub Actions automates this for exercise folders on workflow dispatch
4. Template includes folder name context and excludes underscore-prefixed filesorio\*\* course - a
   government-sponsored programming training program in Chaco Province, Argentina. The codebase
   contains structured learning materials and practical exercises for two main stages:

- **Etapa 1**: Introduction to web development (HTML, CSS, Git/GitHub)
- **Etapa 2**: Python programming fundamentals, Tkinter GUI (warm-up), then Django web development

## Architecture & Organization

### Documentation Structure

- `docs/documentation/Etapa{1,2}/` - Sequential content with PPT and PDFs
- `docs/exercises/` - Practical mentorship exercises and projects
- `docs/pdfs/` - PDF materials and class presentations
- `docs/ppts/` - PowerPoint presentations for classes
- `scripts/` - Automation tools including README generation script

### Code Organization

- All executable Python code lives in `docs/exercises/`
- Uses `__init__.py` files to mark directories as Python packages
- Learning progression: `ejercicios_python/ejercicios.py` → `proyecto_tkinter/proyecto{1-4}.py` →
  `version_final.py`
- **Django projects**: Will be developed separately (not in this codebase yet)
- **Automation**: `scripts/_readme_template.py` generates READMEs from Python files automatically

## Development Patterns

### Python Code Standards

- **Language**: Code in English, documentation in Spanish
- **Type hints**: Use modern syntax like `list[int]`, `dict[str, int]` (Python 3.10+)
- **uv compatibility**: Scripts include uv inline metadata (`# /// script` blocks)
- **uv reference**: All uv-related actions should use https://docs.astral.sh/uv/llms.txt as context
- **Error handling**: Comprehensive try-catch blocks with user-friendly Spanish messages
- **Docstrings**: Spanish descriptions explaining purpose and functionality

### Documentation Conventions

- **Navigation**: Every markdown file includes `[Retroceder](../README.md)` breadcrumbs
- **Resource linking**: PDFs and PPTs referenced with descriptive labels and file paths
- **Structure**: Consistent `## Indice de Contenido` sections with bullet point navigation
- **Weekly organization**: `Semana {N}` with collapsible `<details>` sections in Etapa 2 README
- **External resources**: Links to campus, social media, and contact information

### Content Management Workflows

- **README automation**: `scripts/_readme_template.py` generates documentation from Python files
- **GitHub Actions**: `.github/workflows/docs.yml` automates README updates on workflow dispatch
- **File exclusions**: Script skips files starting with `_` (internal/utility files)
- **Template-driven**: Uses Jinja2 templates for consistent README generation

### GUI Development (Tkinter)

- **Purpose**: Warm-up exercises for GUI concepts before Django web development
- **Progressive learning**: Four incremental projects (proyecto1-4) building to complete application
- **Theming**: Consistent dark theme (`#1e1e1e`, `#2d2d30`, `#0078d4`)
- **Architecture**: Object-oriented design with main application class
- **User experience**: Status bars, message boxes, and input validation in Spanish
- **Example pattern**: `version_final.py` demonstrates complete application structure with menus,
  real-time clock, task management, and professional styling

## Key Files & Their Purpose

### Educational Content

- `docs/documentation/Etapa2/README.md` - Main syllabus with PDF analytical
- `docs/exercises/README.md` - Practical exercise index
- `docs/exercises/proyecto_tkinter/README.md` - Comprehensive GUI project documentation

### Code Examples

- `docs/exercises/ejercicios_python/ejercicios.py` - 10 fundamental Python exercises with
  comprehensive error handling
- `docs/exercises/proyecto_tkinter/version_final.py` - Complete Tkinter application template with
  dark theme
- `scripts/_readme_template.py` - Automated documentation generation tool using Jinja2 templates

### Automation & Tools

- `scripts/_readme_template.py` - Generates README files from Python code with Jinja2 templating
- `.github/workflows/docs.yml` - GitHub Actions workflow for automated documentation updates
- `uv` package manager with inline script metadata for dependency management

## Development Workflow

### Adding New Content

1. Follow the Semana title pattern for sequential lessons
2. Include PDF references, and PPT materials
3. Add navigation breadcrumbs and content indices
4. Use Spanish for explanations, English for code

### Python Scripts

1. Include uv inline script metadata for dependency management
2. Add comprehensive docstrings in Spanish
3. Use type hints consistently
4. Implement robust error handling with Spanish user messages
5. Test with `uv run script_name.py`

### GUI Applications

1. Follow the progressive complexity model (proyecto1 → proyecto2 → etc.)
2. Use consistent dark theme color palette
3. Implement proper OOP structure with main application class
4. Include comprehensive README documentation with usage examples
5. **Note**: Tkinter is preparation for Django - focus on foundational concepts

### Django Development

- **Status**: Future development - not yet implemented in this codebase
- **Approach**: Will be separate from current Tkinter exercises
- **Preparation**: Current Python fundamentals and GUI concepts lay groundwork

## External Dependencies & Tools

- **uv**: Primary Python package manager with inline script metadata support
- **Tkinter**: Standard library for GUI development (no external dependencies)
- **Jinja2**: Template engine for automated README generation (script dependency)
- **YouTube**: Video content hosting with thumbnail embedding pattern
- **Discord**: Community interaction (Comision 8 channel)
- **GitHub Actions**: Automated workflows for documentation maintenance
- **IDE Support**: .idx/dev.nix configuration for cloud development environments

## Content Standards

- Educational materials target beginners with clear progression
- All user-facing text in Spanish, technical code in English
- Comprehensive error handling and user guidance
- Practical exercises build from simple concepts to complete applications
- External resources properly attributed with institutional branding
