from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site

from render_engine_fontawesome.fontawesome import fontawesome


class app(Site):
    template_path = "docs/templates"
    output_path = "docs/output"


app = app()
app.site_vars.update(
    {
        "SITE_TITLE": "Render Engine FontAwesome",
        "SITE_URL": "https://kjaymiller.github.io/render_engine_fontawesome/",
        "OWNER": {
            "name": "kjaymiller",
            "email": "kjaymiller@gmail.com",
        },
        "NAVIGATION": [
            {
                "text": "Docs",
                "url": "/docs.html",
            },
            {
                "test": "GitHub",
                "url": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
            },
        ],
        "theme": {"fontawesome": "94d9a219ee"},
    }
)
app.register_themes(fontawesome)


@app.page
class Index(Page):
    template = "index.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite"]}
