from twttr import shorten

def test_shorten1():
    assert shorten("whatsapp") == "whtspp"
    assert shorten("HEY BRO HOW ARE YOU") == "HY BR HW R Y"
    assert shorten("2864") == "2864"
    assert shorten("?.@,!") == "?.@,!"
