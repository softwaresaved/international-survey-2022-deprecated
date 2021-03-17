import os
import sys
from pathlib import Path

def sha256sum(fn: Path) -> str:
    import hashlib
    m = hashlib.sha256()
    m.update(fn.read_text().encode("utf-8"))
    return m.hexdigest()

HASH = "aff0bdfa0d01ffad9b2f2af3aa049271ca89e8248cb3c704c8f8cfc2d0096ab7"
CACHED_DATA = Path("cache/processed_data.csv")

def test_overview_and_sampling():
    os.environ["RSE_SURVEY_YEAR"] = "2018"
    sys.path.insert(1, str(Path(__file__).parent.parent))
    import overview_and_sampling
    overview_and_sampling.run()
    assert sha256sum(CACHED_DATA) == HASH
