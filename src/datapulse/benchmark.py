from dataclasses import dataclass
from time import perf_counter
@dataclass(frozen=True)
class BenchmarkResult: operation:str; rows:int; seconds:float
def measure(operation,rows,fn):
 if rows<0: raise ValueError('rows must be non-negative')
 t=perf_counter(); fn(); return BenchmarkResult(operation,rows,perf_counter()-t)
