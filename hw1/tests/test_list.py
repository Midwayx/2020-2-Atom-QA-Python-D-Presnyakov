import pytest
import random


def test_count():
    lst = [0, 1, 2, 3, 3, 'c', 'cc']
    assert lst.count(3) == 2
    assert lst.count('c') == 1
    assert lst.count('a') == 0


def test_extend(get_randint, get_randlist):
    with pytest.raises(TypeError):
        assert get_randlist.extend(get_randint)


def test_insert(get_randlist):
    length = len(get_randlist)
    with pytest.raises(TypeError):
        assert get_randlist.insert('1', 'insert')
    index = random.randint(0, length)
    get_randlist.insert(index, 'insert')
    assert get_randlist[index] == 'insert'


@pytest.mark.parametrize('test_inp, expected', [(0, 0), (1, 1), (-1, 'cc'), (10, IndexError), ('s', TypeError)])
def test_pop(test_inp, expected):
    lst = [0, 1, 2, 3, 3, 'c', 'cc']
    if isinstance(test_inp, str) or abs(test_inp) > len(lst):
        with pytest.raises(expected):
            assert lst.pop(test_inp)
    else:
        assert lst.pop(test_inp) == expected


class TestClass:

    def test_sort(self, get_randlist):

        expected = sorted(get_randlist)
        get_randlist.sort()
        assert get_randlist == expected
