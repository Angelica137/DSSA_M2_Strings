from scripts.Exercise4 import hamming_distance


def test_hamming_distance_returns_None():
    assert hamming_distance('ACTTGACCGGG', 'GATCCGGTACAsaijfdoids') == None


def test_hamming_distance_returns_None():
    assert hamming_distance('ACTTGACCGGG', 'GATCCGGTACA') == 10


def test_hamming_distance_returns_1():
    assert hamming_distance('shove', 'stove') == 1


def test_hamming_distance_returns_None2():
    assert hamming_distance('Slot machines', 'Cash lost in me') == None
