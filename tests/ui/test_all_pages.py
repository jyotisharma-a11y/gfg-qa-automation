import pytest
from utils.helpers import load_test_data

pages_data = load_test_data()

@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize("page_data", pages_data, ids=[p["id"] for p in pages_data])
def test_page_loads(page, page_data):
    page.goto(page_data["url"])
    page.wait_for_load_state("domcontentloaded")
    assert page.title() != ""
    assert page_data["title"].lower() in page.title().lower()
    page.screenshot(path=f"screenshots/{page_data['id']}.png")
    # 1. go to page_data["url"]
    # 2. wait_for_load_state "domcontentloaded"
    # 3. assert page title is not empty
    # 4. assert page_data["title"].lower() is in page.title().lower()
    # 5. take screenshot — save to screenshots/{page_data["id"]}.png