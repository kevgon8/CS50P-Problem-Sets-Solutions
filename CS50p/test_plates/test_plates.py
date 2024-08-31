from plates import is_valid

def test_plates():
    assert is_valid("BM9") == True
    assert is_valid("ABJSHV25") == False
    assert is_valid("AMA9G0") == False
    assert is_valid("GHNJ09") == False
    assert is_valid("GH.-9") == False
    assert is_valid("KK") == True
    assert is_valid("4") == False
    assert is_valid("3V") == False
    assert is_valid("V3") == False
    assert is_valid("35") == False
