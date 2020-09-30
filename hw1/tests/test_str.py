import pytest


def test_capitalize(get_randstring):
    capitalize = get_randstring().capitalize()
    assert all(i.islower() for i in capitalize[1:]) and capitalize[0].isupper


def test_zfill(get_randstring):
    string = get_randstring()
    zero_string = string.zfill(30)
    assert all(i == '0' for i in zero_string[:30 - len(string)]) and string in zero_string


def test_index(get_randstring):
    string = get_randstring()
    sub_string = get_randstring(3)
    if sub_string not in string:
        with pytest.raises(ValueError):
            assert string.index(sub_string)
    else:
        index = string.index(sub_string)
        assert string[index:index + len(sub_string)] == sub_string


@pytest.mark.parametrize('test_inp', [';', ' ', '0'])
def test_join(test_inp, get_randstring):
    string = get_randstring()
    divided = list(string)
    join = test_inp.join(divided)
    assert all(join[i] == string[i // 2] if i % 2 == 0 else join[i] == test_inp for i in range(len(join)))


class TestClass:
    def test_replace(self, get_randstring):
        string = get_randstring(100)
        old = get_randstring(4)
        new = get_randstring(4)
        if old not in string:
            assert string.replace(old, new) == string
        else:
            cnt = string.count(new) + string.count(old)
            replaced = string.replace(old, new)
            assert old not in replaced and len(replaced) == len(string) and replaced.count(new) == cnt
