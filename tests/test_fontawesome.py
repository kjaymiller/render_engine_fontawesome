import pytest
from render_engine import Page, Site

from render_engine_fontawesome.fontawesome import fontawesome


@pytest.fixture
def test_site(tmp_path_factory):
    site = Site()
    site.output_path = tmp_path_factory.getbasetemp() / "output"

    site.register_theme(fontawesome)
    site.site_vars["theme"].update({"fontawesome": "1234567890"})

    return site


def test_page_has_fontawesome_script(test_site):
    class TestPage(Page):
        template = "base.html"

    test_site._render_output("./", TestPage())
    assert "https://kit.fontawesome.com/1234567890.js" in test_site.output_path.joinpath("testpage.html").read_text()
