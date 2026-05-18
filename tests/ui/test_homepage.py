import os
import pytest
from pages.home_page import HomePage

os.makedirs("screenshots", exist_ok=True)

def test_homepage_title(page):
    home = HomePage(page)
    home.goto()
    assert "GeeksforGeeks" in home.get_title()
    # assert "WRONGTEXT" in home.get_title()
    page.screenshot(path="screenshots/homepage.png")

def test_logo_visible(page):
    home = HomePage(page)
    home.goto()
    assert home.is_logo_visible()

def test_homepage_url(page):
    home = HomePage(page)
    home.goto()
    assert "geeksforgeeks.org" in page.url