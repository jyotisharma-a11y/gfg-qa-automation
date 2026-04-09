import json
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/run.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-5s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def load_test_data(path="test_data/pages.json"):
    with open(path) as f:
        return json.load(f)

def log_result(test_name, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    msg = f"{status} | {test_name}"
    if detail:
        msg += f" | {detail}"
    if passed:
        logging.info(msg)
    else:
        logging.error(msg)
    print(f"  {msg}")

if __name__ == "__main__":
    pages = load_test_data()
    for p in pages:
        print(p["url"])