# [ stats.py ] #

import          json
import      tempfile
import       logging

logger = logging.getLogger(__name__)

from pathlib import Path
from typing import Dict

STATS_FILE = Path(__file__).parent / "stats" / "stats.json"

DEFAULT_STATS = {
    "first_used":                None,
    "last_used":                 None,
    "starts":                       0,
    "total_sessions_seconds":       0,
    "real_usage_time":              0,
    "passwords_tested":             0,
    "passwords_generated":          0,
    "total_length_sum":             0
}


def load_stats() -> Dict[str, int | float | None]:
    """Loads default statistics unless user statistics exist."""

    if not STATS_FILE.exists():
        return DEFAULT_STATS.copy()
    
    try:
        with STATS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            
            # fill with missing keys with defaults
            for k, v in DEFAULT_STATS.items():
                data.setdefault(k, v)
            
            return data
        
    except (json.JSONDecodeError, OSError):
        logger.warning("Stats reset due to corrupt file")
        input("\n\tWarning: Stats file corrupted. Starting fresh...")
        
        return DEFAULT_STATS.copy()


def atomic_save_stats( stats: Dict[str, int | float | None] ):
    """Gracefullly updates any changes made to user statistics."""

    logger.info("Saving stats...")
    
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # write temp file and rename
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False,
        dir=STATS_FILE.parent,
    ) as temp:
        json.dump(stats, temp, indent=2, sort_keys=True)
        temp_path = Path(temp.name)
    
    # atomic move
    temp_path.replace(STATS_FILE)
    logger.info("Stats saved.")

