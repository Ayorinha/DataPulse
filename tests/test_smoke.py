"""Production smoke tests for DataPulse."""
import importlib

def test_package_imports() -> None:
    module = importlib.import_module("datapulse")
    assert module.__name__ == "datapulse"
