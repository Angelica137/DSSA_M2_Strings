from scripts.Exercise2 import anagram_checker


def test_anagram_checker_length_differ():
    assert anagram_checker('lol', 'lolz') == False


def test_anagram_length_differ_2():
    assert anagram_checker('water', 'waiter') == False
