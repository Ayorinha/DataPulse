from datapulse.benchmark import *
def test_measure(): assert measure('noop',10,lambda:sum(range(10))).seconds>=0
