from key_exchange import diffie_hellman as dh
from key_exchange.diffie_hellman import BASE, MODULUS, KEY_BITS



def test_diffie_hellman_key_exchange():
	alice_private_key = dh.generate_secret(KEY_BITS)
	bob_private_key = dh.generate_secret(KEY_BITS)

	print('Alice private key: {}'.format(dh.to_bits(alice_private_key)))
	print("Bob's private key: {}".format(dh.to_bits(bob_private_key)))

	alice_public_key = dh.calc_key(BASE, alice_private_key, MODULUS)
	bob_public_key = dh.calc_key(BASE, bob_private_key, MODULUS)

	print('Alice public key: {}'.format(dh.to_bits(alice_public_key)))
	print("Bob's public key: {}".format(dh.to_bits(bob_public_key)))

	alice_shared_secret_key = dh.calc_key(bob_public_key, alice_private_key, MODULUS)
	bob_shared_secret_key = dh.calc_key(alice_public_key, bob_private_key, MODULUS)

	print('Alice shared secret key: {}'.format(dh.to_bits(alice_shared_secret_key)))
	print("Bob's shared secret key: {}".format(dh.to_bits(bob_shared_secret_key)))
	assert alice_shared_secret_key == bob_shared_secret_key
