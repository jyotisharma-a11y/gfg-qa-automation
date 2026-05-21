import pytest
import logging
from utils.api_helpers import api_check
from utils.helpers import load_test_data

@pytest.mark.api
@pytest.mark.parametrize("page_data", load_test_data(), ids=[p["id"] for p in load_test_data()])
def test_page_response_time(page_data):
    # 1. call api_check with page_data["url"]
    result = api_check(page_data["url"])    
    # 2. if result["time_ms"] exists and is greater than 2000
    #    log a warning: f"SLOW: {page_data['url']} — {result['time_ms']}ms"
    if result.get("time_ms") and result["time_ms"] > 2000:
        logging.warning(f"SLOW: {page_data['url']} — {result['time_ms']}ms")

    # 3. assert result["time_ms"] is not None
    assert result["time_ms"] is not None, f"FAIL: {result}"
    # 4. assert result["time_ms"] < 5000
    assert result["time_ms"] < 5000, f"FAIL: {result}"
    #    message: f"Too slow: {result['time_ms']}ms"
    # 5. if the test fails, the message should include the entire result dictionary for debugging