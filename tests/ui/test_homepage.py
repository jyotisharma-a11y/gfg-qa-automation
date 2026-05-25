import os
import pytest
from pages.home_page import HomePage 
from utils.helpers import load_test_data, log_result

os.makedirs("screenshots", exist_ok=True)

def test_homepage_title(page):
    home = HomePage(page)
    home.goto()
    result = "GeeksforGeeks" in home.get_title()
    log_result("test_homepage_title", result)
    assert result
    page.screenshot(path="screenshots/homepage.png")


def test_logo_visible(page):
    home = HomePage(page)
    home.goto()
    assert home.is_logo_visible()

def test_homepage_url(page):
    home = HomePage(page)
    home.goto()
    assert "geeksforgeeks.org" in page.url