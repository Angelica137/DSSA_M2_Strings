from scripts.Exercise4 import hamming_distance


def test_hamming_distance_returns_None():
    assert hamming_distance('ACTTGACCGGG', 'GATCCGGTACAsaijfdoids') == None


def test_hamming_distance_returns_None():
    assert hamming_distance('ACTTGACCGGG', 'GATCCGGTACA') == 10
