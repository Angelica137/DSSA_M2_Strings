from scripts.Exercise1 import string_reverser


def test_string_reverser_returns_retaw():
    assert string_reverser('water') == 'retaw'


def test_string_reverse_returns_test2():
    string = 'Practicing string manipulation!'
    assert string_reverser(string) == '!noitalupinam gnirts gnicitcarP'


def test_string_reverse_returns_test3():
    string = 'The house code is: 2343'
    assert string_reverser(string) == '3432 :si edoc esuoh ehT'
