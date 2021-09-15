#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
e = 1
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485

d = -1

#The relationship between N, e, and d is given by:
#d*e = 1 mod (p-1)(q-1)
#if we pick e =1, then d = 1 mod (p-1)(q-1)
#cipher text c = m^e (mod N) i.e. c = m mod N but m < N so m mod N is m so we have c = m
#decrypting given ct will give the flag
#referred from stackoverflow https://stackoverflow.com/questions/17490282/why-is-this-commit-that-sets-the-rsa-public-exponent-to-1-problematic

decrypted = long_to_bytes(ct)
print(decrypted)
