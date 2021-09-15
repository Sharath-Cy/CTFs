import json
import requests
from binascii import unhexlify

response = requests.get(f'http://aes.cryptohack.org/symmetry/encrypt_flag/')

ivciphertext = json.loads(response.content)['ciphertext']

print("Response combined with iv and Cipher text : {}".format(ivciphertext))

iv = ivciphertext[:32]#First 32 is Initialization vector
print("iv seprated from  Cipher text : {}".format(iv))
ciphertext = ivciphertext[32:] #Remainingthat is from 32 onwards it will be cipher text
print("Final Cipher text obtained : {}".format(ciphertext))


response = requests.get(f'http://aes.cryptohack.org/symmetry/encrypt/{ciphertext}/{iv}/')

print(unhexlify(json.loads(response.content)['ciphertext']))