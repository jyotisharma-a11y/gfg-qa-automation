import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.ui
def test_courses_link_visible(page):
    home = HomePage(page)
    home.goto()
    assert home.nav_courses.is_visible()
    # 1. create HomePage object
    # 2. call goto()
    # 3. assert nav_courses is visible

@pytest.mark.smoke
@pytest.mark.ui
def test_page_has_no_console_errors(page):
    errors = []
    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    home = HomePage(page)
    home.goto()
    assert len(errors) == 0
    # 1. create an empty list called errors
    # 2. add this line exactly:
    #    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    # 3. create HomePage object
    # 4. call goto()
    # 5. assert len(errors) == 0