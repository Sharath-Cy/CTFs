from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from itertools import combinations
from math import gcd

#reading pem file to get n and e and appending it into keys list
keys = []
for i in range(1, 51):
    with open(f'/home/gubbs/Downloads/keys_and_messages/{i}.pem') as f:
        keys.append((i, RSA.import_key(f.read())))

#Taking combinations from the imported keys.
for (i, key1), (j, key2) in combinations(keys, 2):
    p = gcd(key1.n, key2.n)
    if p == 1: # other than 1 jump next if not loop again
        continue
    q1 = key1.n//p
    q2 = key2.n//p
    pkey1 = RSA.construct((key1.n, key1.e, pow(key1.e, -1, (p-1)*(q1-1)), p, q1)) # constructing all values, p,q, n, e, d
    pkey2 = RSA.construct((key2.n, key2.e, pow(key2.e, -1, (p-1)*(q2-1)), p, q2))
    with open(f'/home/gubbs/Downloads/keys_and_messages/{i}.ciphertext') as f: 
        print(PKCS1_OAEP.new(pkey1).decrypt(bytes.fromhex(f.read()))) #decrypting the cipher using the available keys
    with open(f'/home/gubbs/Downloads/keys_and_messages/{j}.ciphertext') as f:
        print(PKCS1_OAEP.new(pkey2).decrypt(bytes.fromhex(f.read())))


