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