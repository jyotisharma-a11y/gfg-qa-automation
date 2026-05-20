import requests

def api_check(url, expected_status=200, max_ms=3000):
    try:
        r = requests.get(url, timeout=10)
        elapsed = round(r.elapsed.total_seconds() * 1000)
        return {
            "url": url,
            "status": r.status_code,
            "time_ms": elapsed,
            "passed": r.status_code == expected_status and elapsed < max_ms
        }
    except Exception as e:
        return {
            "url": url,
            "status": None,
            "time_ms": None,
            "passed": False,
            "error": str(e)
        }