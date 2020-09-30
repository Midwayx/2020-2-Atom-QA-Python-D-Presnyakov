import pytest


@pytest.mark.parametrize('test_inp, expected', [(-10, -10), (0, 0), (0.5, 0),
                                                (0.9, 0), ('-1', -1), ([], TypeError),
                                                ({}, TypeError), ('-10.5', ValueError), ('a', ValueError)])
def test_int(test_inp, expected):
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            assert int(test_inp)
    else:
        assert int(test_inp) == expected


def test_bit_length(get_randint):
    assert get_randint.bit_length() == len(bin(get_randint).lstrip('-0b'))


@pytest.mark.parametrize('test_inp1, test_inp2, expected', [(0, 0, 0), (-1, 1, 0), (8, 12, 20),
                                                            (1, [], TypeError), (2, '2', TypeError)])
def test_plus(test_inp1, test_inp2, expected):
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            assert test_inp1 + test_inp2
    else:
        assert test_inp1 + test_inp2 == expected


def test_hex(get_randint):
    assert int(hex(get_randint), 16) == get_randint


class TestClass:
    def test_pow(self, get_randint):
        assert get_randint**get_randint == pow(get_randint, get_randint)
