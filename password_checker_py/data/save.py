# [ utils.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import json
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path("password_results.json")

def save_result(password: str, mode: int, score: str, result: str, keyword: str):
    """Save password check/generation result to a JSON file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "password": password,
        "mode": mode,
        "score": score,
        "result": result,
        "keyword": keyword
    }

    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            
    else:
        data = []
    
    data.append(entry)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)
    