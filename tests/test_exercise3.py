from scripts.Exercise3 import word_flipper


def test_word_flipper_returns_reverse_string():
    assert word_flipper('hello') == 'olleh'


def test_world_flipper_returns_reverse_string_2_words():
    assert word_flipper('hello goodbye') == 'olleh eybdoog'


def test_word_flipper_returns_reverse_string_water():
    assert word_flipper('water') == 'retaw'


def test_word_flipper_returns_reverse_string_water():
    assert word_flipper('This is an example') == 'sihT si na elpmaxe'


def test_word_flipper_returns_reverse_string_water():
    assert word_flipper(
        'This is one small step for ...') == 'sihT si eno llams pets rof ...'
