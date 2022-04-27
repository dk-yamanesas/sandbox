import pytest
from src.main import calc


@pytest.mark.parametrize("params", [(1, 1)])
def test(params):
    x = params[0]
    y = params[1]
    ans = calc(x, y)

    assert ans == x + y
