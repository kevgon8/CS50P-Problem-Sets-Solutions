from seasons import mins_convert
import pytest

def test_1():
    assert mins_convert(2006, 9, 14) == "Nine million, three hundred seventy-two thousand, nine hundred sixty minutes"
    assert mins_convert(2013, 9, 2) == "Five million, seven hundred eight thousand, one hundred sixty minutes"

def test_2():
    assert mins_convert(23, 1, 2000) == "Invalid date :("
