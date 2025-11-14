# Render Engine FontAwesome

Adds the fontawesome iconset to render engine themes.

Converts `<i class="fas fa-home"></i>` to <i class="fas fa-home"></i>.

## How to use this theme

1. Install the theme

   ```python
   pip install render_engine_fontawesome
   ```

2. Import the theme into your project

   ```python
   from render_engine import Site
   from render_engine_fontawesome import fontawesome

   app = Site()
   app.register_theme(fontawesome)
   app.site_vars['theme'].update({fontawesome: 'your token here'})
   ```

## Required Settings

Fontawesome now requires a token to be used. You can get a free token from [fontawesome.com](https://fontawesome.com/start).

The plugin looks for the `fontawesome` key in `site_vars['theme']` key. The value should be your token.

## Development & Testing

This project uses `just` for common development tasks and `nox` for testing across multiple Python versions.

### Quick Start with Just

```bash
# Run tests
just test

# Run linting
just lint

# Run both linting and tests
just check
```

### Using Nox for Multi-Version Testing

Test the plugin across Python 3.11, 3.12, 3.13, and 3.14:

```bash
# Run tests on all Python versions
nox -s test

# Run linting on all Python versions
nox -s lint

# Run both tests and linting
nox -s check
```

### Development Setup

```bash
# Install with uv (recommended)
uv sync

# Install with pip
pip install -e ".[test]"

# Run tests
just test
```

## Available Just Commands

- `just test` - Run pytest on current Python version
- `just lint` - Run ruff linting checks
- `just check` - Run both linting and tests