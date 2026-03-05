# [ reader.py ] #


# ======== Setup ======== #

# [ Libraries ] #
from pathlib import Path


# ======== Main ======== #

def read_file( path: Path ):
    """Safely reads a file depending on its format. Accepted formats: .txt, .json and .jsonl"""
    
    extension = Path(path).suffix

    assert extension == ".txt" or extension == ".json" or extension == ".jsonl", "Invalid file format!"

    if extension == ".txt":
        read_txt(path)
        return
    
    read_jsonl(path)


def read_txt( path: Path ):
    """Reads text file, yields each line."""

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line.rstrip("\n")


def read_jsonl( path: Path, key: str="password" ):
    """Reads json or jsonl file, yields each line."""

    import json
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue
            
            # assume 'password' key exists
            yield json.loads(line)[key]

