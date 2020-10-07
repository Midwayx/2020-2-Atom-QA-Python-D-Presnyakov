import pytest


def test_clear(get_randdict):
    get_randdict.clear()
    assert not get_randdict


@pytest.mark.parametrize('test_inp, expected', [(0, 0), (1, 1), ('test', 'test'), (2, None),
                                                ([], TypeError), ({}, TypeError)])
def test_2(test_inp, expected):
    dct = {0: 0, 'test': 'test', 1: 1}
    if isinstance(test_inp, list) or isinstance(test_inp, dict):
        with pytest.raises(expected):
            assert dct.get(test_inp)
    else:
        assert dct.get(test_inp) == expected


def test_copy(get_randdict):
    copy = get_randdict.copy()
    assert id(copy) != id(get_randdict)
    assert all(copy[i] == get_randdict[i] for i in get_randdict) and len(copy) == len(get_randdict)


def test_items(get_randdict):
    lst = [(key, get_randdict[key]) for key in get_randdict]
    assert list(get_randdict.items()) == lst


class TestClass:
    def test_key(self, get_randdict):
        lst = [key for key in get_randdict]
        assert list(get_randdict.keys()) == lst
