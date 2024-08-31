from bank import value

def test_bank():
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("whatsup") == 100
