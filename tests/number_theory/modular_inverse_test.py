from number_theory import modular_inverse


def test_modular_inverse_coprimes():
    assert 13 * modular_inverse(13, 9) % 9 == 1
    assert 12 * modular_inverse(12, 67) % 67 == 1 
    assert 2 * modular_inverse(2, 3) % 3 == 1
    assert 3 * modular_inverse(3, 11) % 11 == 1
    assert 7 * modular_inverse(7, 13) % 13 == 1


def test_modular_inverse_non_coprimes():
    assert modular_inverse(2, 2) is None
    assert modular_inverse(2, 4) is None
    assert modular_inverse(3, 6) is None
    assert modular_inverse(3, 12) is None
    assert modular_inverse(8, 64) is None
