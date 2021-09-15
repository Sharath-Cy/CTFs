
from Crypto.PublicKey import RSA

pem = open("CryptoHack/General/Data Formats/Privacy-Enhanced Mail/privacy_enhanced_mail.pem","r")

rsa_key = RSA.importKey(pem.read())

print(rsa_key.d)