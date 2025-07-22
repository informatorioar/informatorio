# Informatorio Codebase Guide

## Project Overview

This is an educational repository for the **Informatorio** course - a government-sponsored
programming training program in Chaco Province, Argentina. The codebase contains structured learning
materials and practical exercises for two main stages:

- **Etapa 1**: Introduction to web development (HTML, CSS, Git/GitHub)
- **Etapa 2**: Python programming fundamentals, Tkinter GUI (warm-up), then Django web development

## Architecture & Organization

### Documentation Structure

- `docs/documentation/` - Sequential weekly content organized by `Etapa{1,2}/semana{N}.md`
- `docs/exercises/` - Practical mentorship exercises and projects
- `docs/pdfs/` - PDF materials and class presentations
- `docs/ppts/` - PowerPoint presentations for classes

### Code Organization

- All executable Python code lives in `docs/exercises/`
- Uses `__init__.py` files to mark directories as Python packages
- Current focus: `ejercicios_python/ejercicios.py` → `proyecto_tkinter/proyecto{1-4}.py` →
  `version_final.py`
- **Django projects**: Will be developed separately (not in this codebase yet)

## Development Patterns

### Python Code Standards

- **Language**: Code in English, documentation in Spanish
- **Type hints**: Use modern syntax like `list[int]`, `dict[str, int]` (Python 3.9+)
- **uv compatibility**: Scripts include uv inline metadata (`# /// script` blocks)
- **uv reference**: All uv-related actions should use https://docs.astral.sh/uv/llms.txt as context
- **Error handling**: Comprehensive try-catch blocks with user-friendly Spanish messages
- **Docstrings**: Spanish descriptions explaining purpose and functionality

### Documentation Conventions

- **Navigation**: Every markdown file includes `[Retroceder](../README.md)` breadcrumbs
- **Linking**: YouTube videos, PDFs, and PPTs are referenced with descriptive labels
- **Structure**: Consistent `## Indice de Contenido` sections with bullet point navigation
- **Resources**: External links to campus, social media, and contact information

### GUI Development (Tkinter)

- **Purpose**: Warm-up exercises for GUI concepts before Django web development
- **Progression**: Four incremental projects building to a complete application
- **Theming**: Dark theme with consistent colors (`#1e1e1e`, `#2d2d30`, `#0078d4`)
- **Architecture**: Object-oriented design with main class containing all components
- **User feedback**: Status bars, message boxes, and input validation in Spanish

## Key Files & Their Purpose

### Educational Content

- `docs/documentation/Etapa2/README.md` - Main syllabus with PDF analytical
- `docs/exercises/README.md` - Practical exercise index
- `docs/exercises/proyecto_tkinter/README.md` - Comprehensive GUI project documentation

### Code Examples

- `docs/exercises/ejercicios_python/ejercicios.py` - 10 fundamental Python exercises
- `docs/exercises/proyecto_tkinter/version_final.py` - Complete Tkinter application template

## Development Workflow

### Adding New Content

1. Follow the semana{N}.md pattern for sequential lessons
2. Include YouTube links, PDF references, and PPT materials
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

- **uv**: Primary Python package manager (referenced in .gitignore and scripts)
- **Tkinter**: Standard library for GUI development
- **YouTube**: Video content hosting and embedding
- **Discord**: Community interaction (Comision 8 channel)
- **GitHub**: Version control and documentation hosting

## Content Standards

- Educational materials target beginners with clear progression
- All user-facing text in Spanish, technical code in English
- Comprehensive error handling and user guidance
- Practical exercises build from simple concepts to complete applications
- External resources properly attributed with institutional branding
