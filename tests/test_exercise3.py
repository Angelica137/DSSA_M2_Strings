from scripts.Exercise3 import word_flipper


def test_word_flipper_returns_string():
    assert word_flipper('hello') == 'olleh'
