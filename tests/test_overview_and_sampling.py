import os
import sys
from pathlib import Path

def sha256sum(fn: Path) -> str:
    import hashlib
    m = hashlib.sha256()
    m.update(fn.read_text().encode("utf-8"))
    return m.hexdigest()

HASH = "b5bd6188b33e451f9a50e3e55fece457ae45352928357b371e0b71a44452f533"
CACHED_DATA = Path("cache/processed_data.csv")

def test_overview_and_sampling():
    os.environ["RSE_SURVEY_YEAR"] = "2018"
    sys.path.insert(1, str(Path(__file__).parent.parent))
    import survey.overview_and_sampling
    survey.overview_and_sampling.run()
    assert sha256sum(CACHED_DATA) == HASH
