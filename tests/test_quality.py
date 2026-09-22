from datapulse.quality import assess

def test_quality_metrics():
    r=assess([{"id":1,"x":None},{"id":1,"x":None},{"id":2,"x":3}])
    assert r.rows==3 and r.nulls==2
    assert r.duplicate_rate==1/3
