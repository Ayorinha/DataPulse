from dataclasses import dataclass
from time import perf_counter
@dataclass(frozen=True)
class BenchmarkResult:name:str;elapsed_ms:float
def benchmark(name,fn):
 start=perf_counter();value=fn();return BenchmarkResult(name,(perf_counter()-start)*1000),value
