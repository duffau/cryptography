from number_theory import modular_inverse


def test_modular_inverse():
    assert 13 * modular_inverse(13, 9) % 9 == 1
    assert 12 * modular_inverse(12, 67) % 67 == 1 
