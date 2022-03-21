import os
import sys
from pathlib import Path

def sha256sum(fn: Path) -> str:
    import hashlib
    m = hashlib.sha256()
    m.update(fn.read_text().encode("utf-8"))
    return m.hexdigest()

HASH = "6fbc60cee4b175976e81e03c1c1107982246ace34afa5619380628d1a536c151"
CACHED_DATA = Path("cache/processed_data.csv")

def test_overview_and_sampling():
    os.environ["RSE_SURVEY_YEAR"] = "2022"
    os.environ["RSE_SURVEY_YEAR_PREV"] = "2018"
    sys.path.insert(1, str(Path(__file__).parent.parent))
    import survey.overview_and_sampling
    survey.overview_and_sampling.run()
    assert sha256sum(CACHED_DATA) == HASH
