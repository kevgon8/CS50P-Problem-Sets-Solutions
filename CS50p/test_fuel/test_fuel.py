from fuel import convert, gauge
import pytest

def test_actual():
    assert convert("5/10") == 50 and gauge(50) == "50%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_zero_division_error():
        with pytest.raises(ZeroDivisionError):
            convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cake/eggs")
