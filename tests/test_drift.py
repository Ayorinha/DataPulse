import pytest

from datapulse.drift import absolute_rate_delta


def test_rate_delta():
    assert absolute_rate_delta(.2, .3) == pytest.approx(.1)
