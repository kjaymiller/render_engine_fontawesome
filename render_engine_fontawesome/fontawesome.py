import pathlib

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
# Add plugins here

fontawesome = Theme(
    loader=PackageLoader(f"render_engine_fontawesome", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [],
    filters = {},
)