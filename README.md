![GFG QA Suite](https://github.com/jyotisharma-a11y/gfg-qa-automation/actions/workflows/tests.yml/badge.svg)# GFG QA Automation Suite

Automated test suite for GeeksforGeeks web app.
Built with Python, Playwright, Pytest, and GitHub Actions.

## What this tests
- Homepage load and title validation
- Search functionality
- Navigation elements
- All key GFG pages (data-driven)
- API health and response time

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/gfg-qa-automation.git
cd gfg-qa-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests
```bash
pytest tests/ -v
```

## Project status
Day 1 — project skeleton created

## Changelog

### Week 3
- Added API health tests (8 tests)
- Added API performance tests (8 tests)
- Added api_session fixture in conftest
- Wired log_result to all tests
- Logs writing to logs/run.log on every test run

