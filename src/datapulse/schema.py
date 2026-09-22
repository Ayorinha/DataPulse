"""Data quality schema contracts."""
from dataclasses import dataclass

@dataclass(frozen=True)
class FieldRule:
    name: str
    required: bool = False
    unique: bool = False

def validate_schema(rules: list[FieldRule]) -> None:
    names = [r.name for r in rules]
    if any(not n.strip() for n in names):
        raise ValueError("field names must not be empty")
    if len(names) != len(set(names)):
        raise ValueError("field names must be unique")
