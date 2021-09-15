import json
import requests
from binascii import unhexlify

encrypted_flag = requests.get(f'http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')

ciphertext = json.loads(encrypted_flag.content)['ciphertext']

print("Ciphertext  : {}".format(ciphertext))


plaintext_hex = requests.get(f'http://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext}/')

plaintext = (json.loads(plaintext_hex.content)['plaintext'])

print("Plaintext   : {}".format(plaintext))

print("Flag        : {}".format(unhexlify(plaintext)))