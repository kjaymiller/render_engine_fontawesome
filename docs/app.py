from render_engine.collection import Collection
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site

from render_engine_fontawesome.fontawesome import fontawesome

app = Site()
app.output_path = "docs/output"
app.site_vars.update ({
    "SITE_TITLE": f"Render Engine FontAwesome",
    "SITE_URL": "https://kjaymiller.github.io/render_engine_fontawesome/",
    "OWNER": {
        "name": f"kjaymiller",
        "email": f"kjaymiller@gmail.com",
    },
    "NAVIGATION": [
        {
            "text": "Docs",
            "url": "/docs.html",
        },
        {
            "test": "GitHub",
            "url": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
        }    
    ],
    "theme": {"fontawesome": "94d9a219ee"},
})
app.register_themes(fontawesome)

@app.page
class Index(Page):
    template = "content.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite"]}
