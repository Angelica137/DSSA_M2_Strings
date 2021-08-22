from scripts.Exercise3 import word_flipper


def test_word_flipper_returns_reverse_string():
    assert word_flipper('hello') == 'olleh'


def test_world_flipper_returns_reverse_string_2_words():
    assert word_flipper('hello goodbye') == 'olled eybdoog'
