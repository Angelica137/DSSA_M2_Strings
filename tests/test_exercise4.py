from scripts.Exercise4 import hamming_distance


def test_hamming_distance_returns_10():
    assert hamming_distance('ACTTGACCGGG', 'GATCCGGTACA') == 10
