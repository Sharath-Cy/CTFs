
from Crypto.Util.number import inverse, long_to_bytes

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

#factorized n from factordb.com and obtained below
p = 752708788837165590355094155871
q = 986369682585281993933185289261

N = (p-1)*(q-1)
d = inverse(e,N)

message = pow(ct, d, n)
decrypted = long_to_bytes(message)
print(decrypted)
