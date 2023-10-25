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
   ```