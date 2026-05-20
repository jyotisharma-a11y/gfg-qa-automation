import pytest
from utils.api_helpers import api_check
from utils.helpers import load_test_data

@pytest.mark.api
@pytest.mark.parametrize("page_data", load_test_data(), ids=[p["id"] for p in load_test_data()])
def test_page_returns_200(page_data):
    # 1. call api_check with page_data["url"]
    result = api_check(page_data["url"])

    # 2. assert result["passed"] is True
    assert result["passed"], f"FAIL: {result}"

    # 3.use this format: assert result["passed"], f"FAIL: {result}
    # 4. if the test fails, the message should include the entire result dictionary for debugging
    




