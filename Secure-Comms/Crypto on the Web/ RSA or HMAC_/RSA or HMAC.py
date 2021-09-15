import jwt # note this is the PyJWT module, not python-jwt
import requests

url = "http://web.cryptohack.org"
PUBLIC_KEY = "/rsa-or-hmac/get_pubkey/"
username = 'admin'

resp = requests.get(url+PUBLIC_KEY)
pubkey = resp.json()
key = pubkey['pubkey']

print(key)

encoded = jwt.encode({'username': username, 'admin': True}, key, algorithm='HS256')
print(encoded)


