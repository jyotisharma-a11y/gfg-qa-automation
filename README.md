!![GFG QA Suite](https://github.com/YOUR_USERNAME/gfg-qa-automation/actions/workflows/tests.yml/badge.svg)

# GFG QA Automation Suite

Automated test suite for GeeksforGeeks web app.
Built with Python, Playwright, Pytest, and GitHub Actions.

## What this tests
- Homepage load and title validation
- Search functionality
- Navigation elements
- All 8 GFG pages — data driven
- API health — status 200
- API performance — response under 5s

## Tech stack
- Python 3.12
- Playwright
- Pytest
- GitHub Actions CI/CD
- requests library

## Setup
    git clone https://github.com/YOUR_USERNAME/gfg-qa-automation
    cd gfg-qa-automation
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium

## Run tests
    pytest tests/ -v                    # full suite
    pytest -m smoke -v                  # smoke only
    pytest -m ui -v                     # UI only
    pytest -m api -v                    # API only

## Project structure
    pages/          Page Object Model classes
    tests/ui/       Playwright browser tests
    tests/api/      API tests
    utils/          Helper functions
    test_data/      JSON test data
    conftest.py     Shared fixtures