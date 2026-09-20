from src.main import number_to_word


def test_zero():
    assert number_to_word(0) == "zero"


def test_single_digit():
    assert number_to_word(7) == "seven"


def test_under_twenty():
    assert number_to_word(15) == "fifteen"


def test_compound_number():
    assert number_to_word(23) == "twenty-three"


def test_hundreds():
    assert number_to_word(123) == "one hundred twenty-three"


def test_thousands():
    assert number_to_word(1001) == "one thousand one"


def test_millions():
    assert number_to_word(1000000) == "one million"