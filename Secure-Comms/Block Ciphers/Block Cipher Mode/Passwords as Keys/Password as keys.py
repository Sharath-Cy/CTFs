from Crypto.Cipher import AES
import hashlib
import json
import requests
import binascii



response = requests.get(f'http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
ciphertext = json.loads(response.content)['ciphertext']

with open("/usr/share/dict/words") as f:
    for words in f:
        words = words.strip() 
        KEY = hashlib.md5(words.encode()).digest()
        ciphertextfromhex = bytes.fromhex(ciphertext)
        cipher = AES.new(KEY, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertextfromhex)
            if decrypted.startswith('crypto{'.encode()):
                print("Flag obtained : {}".format(decrypted.decode('utf-8')))
                break
        except ValueError as e:
            print(str(e))