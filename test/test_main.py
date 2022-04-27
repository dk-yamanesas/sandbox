import pytest
from src.main import add, div, mul, sub


@pytest.mark.parametrize("params", [(1, 1)])
def test_add(params):
    x = params[0]
    y = params[1]
    ans = add(x, y)

    assert ans == x + y


@pytest.mark.parametrize("params", [(1, 1)])
def test_sub(params):
    x = params[0]
    y = params[1]
    ans = sub(x, y)

    assert ans == x - y

@pytest.mark.parametrize("params", [(1, 1)])
def test_mul(params):
    x = params[0]
    y = params[1]
    ans = mul(x, y)

    assert ans == x * y

@pytest.mark.parametrize("params", [(1, 1)])
def test_div(params):
    x = params[0]
    y = params[1]
    ans = div(x, y)

    assert ans == x / y
