import pytest
from utils.helpers import load_test_data, log_result

from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.ui
def test_courses_link_visible(page):
    home = HomePage(page)
    home.goto()
    # 1. create HomePage object
    # 2. call goto()
    # 3. assert nav_courses is visible
    try:
        assert home.nav_courses.is_visible()
        log_result("test_courses_link_visible", True)
    except AssertionError as e:
        log_result("test_courses_link_visible", False, str(e))
        raise

@pytest.mark.smoke
@pytest.mark.ui
def test_page_has_no_console_errors(page):
    errors = []
    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    home = HomePage(page)
    home.goto()
    try:
        assert len(errors) == 0
        log_result("test_page_has_no_console_errors", True)
    except AssertionError as e:
        log_result("test_page_has_no_console_errors", False, str(e))
        raise
    # 1. create an empty list called errors
    # 2. add this line exactly:
    #    page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)
    # 3. create HomePage object
    # 4. call goto()
    # 5. assert len(errors) == 0 