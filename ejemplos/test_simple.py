import pytest

def pcg(a, b):
    return None

def test_value():
    assert pcg(5, 100) == 5
    assert pcg(1, 10) == 10

def test_type():
    with pytest.raises(TypeError):  pcg('a', 10)
    with pytest.raises(TypeError):  pcg(10, 'a')

def test_sign():
    with pytest.raises(ValueError): pcg(-10, 100)
    with pytest.raises(ValueError): pcg(10, -100)
