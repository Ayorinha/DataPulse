from datapulse.schema import FieldRule,validate_schema

def test_schema_rejects_duplicate_fields():
    try: validate_schema([FieldRule("id"),FieldRule("id")])
    except ValueError: return
    raise AssertionError("expected ValueError")
