import pytest


def test_clear(get_randset):
    inp = get_randset()
    inp.clear()
    assert not inp


def test_update(get_randset):
    set1 = get_randset()
    set2 = get_randset()
    set1.update(set2)
    assert all(i in set1 for i in set2)


def test_intersection(get_randset):
    set1 = get_randset()
    set2 = get_randset()
    assert all(i in set1 and i in set2 for i in set1.intersection(set2))


@pytest.mark.parametrize('element', ['test', -100,  0, 100])
def test_(element, get_randset):
    set1 = get_randset()
    if element not in set1:
        with pytest.raises(KeyError):
            assert set1.remove(element)
    else:
        set1.remove(element)
        assert element not in set1


class TestClass:
    def test_add(self, get_randset):
        set1 = get_randset()
        set2 = get_randset()
        assert all(i not in set2 and i in set1 or set1 == set2 for i in set1.difference(set2))
