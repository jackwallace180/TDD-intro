from sci_calc import *

def test_find_sqrt():
    assert find_sqrt(100) == 10.0
    assert find_sqrt(16) == 4
    assert find_sqrt(49) == 7

def test_find_ceil():
    assert find_ceil(12.7) == 13
    assert find_ceil(15.6) == 16