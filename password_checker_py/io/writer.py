# [ writer.py ] #

# ======== Setup ======== #

from pathlib import Path


def write_jsonl( path: Path, obj ):
    """Appends a JSONL object to file."""

    import json
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj) + "\n")

