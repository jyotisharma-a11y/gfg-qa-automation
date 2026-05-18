# conftest — shared fixtures will go here
import pytest
from playwright.sync_api import sync_playwright
from utils.helpers import load_test_data

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        yield b
        b.close()

@pytest.fixture
def page(browser):
    pg = browser.new_page()
    yield pg
    pg.close()

@pytest.fixture
def test_pages():
    return load_test_data()

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield
    if request.node.rep_call.failed:
        name = request.node.name.replace("/", "_")
        page.screenshot(path=f"screenshots/FAIL_{name}.png")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_configure(config):
    config._metadata = {
        "Project": "GFG QA Automation",
        "Tester": "Jyoti Sharma",
        "Environment": "Production",
        "Base URL": "https://www.geeksforgeeks.org"
    }