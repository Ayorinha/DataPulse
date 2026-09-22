"""Lightweight distribution drift signal."""
def absolute_rate_delta(reference: float, current: float) -> float:
    if not 0 <= reference <= 1 or not 0 <= current <= 1: raise ValueError("rates must be between 0 and 1")
    return abs(current-reference)