from dataclasses import dataclass
from collections import Counter
from typing import Iterable

@dataclass(frozen=True)
class QualityReport:
    rows: int
    nulls: int
    duplicate_rate: float

def assess(rows: Iterable[dict]) -> QualityReport:
    data=list(rows)
    if not data: return QualityReport(0,0,0.0)
    nulls=sum(v is None for row in data for v in row.values())
    keys=[tuple(sorted(row.items())) for row in data]
    duplicates=len(keys)-len(Counter(keys))
    return QualityReport(len(data),nulls,duplicates/len(data))
