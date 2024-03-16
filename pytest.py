import pytest

# Tests for string data structure
def test_string_uppercase():
    string = "hello"
    assert string.upper() == "HELLO"

def test_string_concatenation():
    string1 = "Hello"
    string2 = ", World!"
    assert string1 + string2 == "Hello, World!"

def test_string_strip():
    string = "  Hello  "
    assert string.strip() == "Hello"

# Tests for dictionary data structure
def test_dict_update():
    dictionary = {'a': 1, 'b': 2}
    dictionary.update({'c': 3})
    assert dictionary == {'a': 1, 'b': 2, 'c': 3}

def test_dict_pop():
    dictionary = {'a': 1, 'b': 2}
    value = dictionary.pop('a')
    assert value == 1
    assert dictionary == {'b': 2}

@pytest.mark.parametrize("key", ["a", "b", "c"])
def test_dict_get(key):
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    assert dictionary.get(key) == dictionary[key]
