import pytest

from roman_to_integer import roman_to_integer

def test_roman_to_integer():
    assert roman_to_integer('I') == 1
    assert roman_to_integer('IV') == 4
    assert roman_to_integer('IX') == 9
    assert roman_to_integer('XIV') == 14
    assert roman_to_integer('XXVII') == 27
    assert roman_to_integer('XLVIII') == 48
    assert roman_to_integer('LXXXVIII') == 88
    assert roman_to_integer('XCIX') == 99
    assert roman_to_integer('CXVIII') == 118
    assert roman_to_integer('CDLXXXVII') == 487
    assert roman_to_integer('DCLXXXIV') == 684
    assert roman_to_integer('CMXCIX') == 999
    assert roman_to_integer('MDCCLXXVI') == 1776
    assert roman_to_integer('MCMLIV') == 1954
    assert roman_to_integer('MMXIV') == 2014

def test_roman_to_integer_invalid_input():
    with pytest.raises(KeyError):
        roman_to_integer('Z')
    with pytest.raises(TypeError):
        roman_to_integer(123)
    with pytest.raises(TypeError):
        roman_to_integer(None)
