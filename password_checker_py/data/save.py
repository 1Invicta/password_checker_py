# [ save.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import json
from datetime import datetime
from pathlib import Path

# [ Information ] #
OUTPUT_FILE = Path("password_results.json")


# ======== Save ========= #

def save_result(password: str, mode: int, score: str, result: str, keyword: str):
    """Apend a  password check/generation result to a JSON (JSONL) file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "password": password,
        "mode": mode,
        "score": score,
        "result": result,
        "keyword": keyword
    }

    with open(OUTPUT_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")
    