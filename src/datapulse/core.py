from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter
from typing import Callable, TypeVar
T = TypeVar("T")
@dataclass(frozen=True, slots=True)
class BenchmarkResult: name: str; elapsed_ms: float

def benchmark(name: str, fn: Callable[[], T]) -> tuple[BenchmarkResult, T]:
    if not name.strip(): raise ValueError("name must be non-empty")
    start = perf_counter(); value = fn(); elapsed = (perf_counter() - start) * 1000
    return BenchmarkResult(name, elapsed), value
