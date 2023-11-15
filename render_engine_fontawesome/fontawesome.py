import pathlib

from jinja2 import DictLoader
from render_engine.utils.themes import Theme

# Add plugins here
fontawesome = Theme(
    loader=DictLoader(
        {
            "fontawesome.html": '<script src="https://kit.fontawesome.com/{{theme["fontawesome"]}}.js" crossorigin="anonymous"></script>',  # noqa 501
        }
    ),
    static_dir=pathlib.Path(__file__).parent / "static",
    filters=[],
    plugins={},
    template_globals={"head": "fontawesome.html"},
)
