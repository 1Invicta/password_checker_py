# [ save.py ] #


# ======== Setup ======== #

# [ Libraries ] #
import json

from datetime   import datetime
from pathlib    import     Path

# [ Information ] #
OUTPUT_FILE = Path(__file__).parent / "results" / "results.json"


# ======== Save ========= #

def save_result( password: str, mode: int, score: str, result: str, keyword: str ):
    """Apend a password check/generation result to a JSON (JSONL) file."""
    
    entry = {
        "timestamp":    datetime.now().isoformat(),
        "password":                       password,
        "mode":                               mode,
        "score":                             score,
        "result":                           result,
        "keyword":                          keyword
    }

    with open(OUTPUT_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")


def save_result_iter( passwords: list[str], mode_iter: int, score_iter: str, result_iter: str, keyword_iter: str ):
    """Append a password check/generation result to a JSON (JSONL) file with iterative object."""
    
    for p in passwords:
        save_result(p, mode_iter, p[2], result_iter, keyword_iter)
