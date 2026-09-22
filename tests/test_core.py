from datapulse.core import benchmark

def test_benchmark():
    result, value = benchmark("identity", lambda: 42)
    assert result.name == "identity" and value == 42 and result.elapsed_ms >= 0
