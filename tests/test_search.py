import pytest
from utils.helpers import load_test_data, log_result
from conftest import page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_python(page):
    # 1. create HomePage object
    # 2. call goto()
    # 3. call search() with "python"
    # 4. create SearchResultsPage object
    # 5. assert "python" in results url OR has_results() is True
    # 6. take screenshot — save to screenshots/search_python.png
    home = HomePage(page)
    home.goto()
    home.search("python")
    search_results = SearchResultsPage(page)
    try:
        assert "python" in search_results.get_url().lower() or search_results.has_results()
        page.screenshot(path="screenshots/search_python.png")
        log_result("test_search_python", True)
    except AssertionError as e:
        log_result("test_search_python", False, str(e))
        raise

def test_search_java(page):
    # same flow but search for "java"
    # screenshot — search_java.png
    home = HomePage(page)
    home.goto()
    home.search("java")
    search_results = SearchResultsPage(page)
    try:
        assert search_results.has_results()
        page.screenshot(path="screenshots/search_java.png")
        log_result("test_search_java", True)
    except AssertionError as e:
        log_result("test_search_java", False, str(e))
        raise
    