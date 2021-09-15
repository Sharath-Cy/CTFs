from Crypto.Util.number import inverse

#x ≡ 2 mod 5
#x ≡ 3 mod 11
#x ≡ 5 mod 17


#https://faculty.math.illinois.edu/~ruan/347Sp18HW/HW12sol.pdf
#x = a1N1y1 + a2N2y2 + a3N3y3 (mod N)
#y1 = inverse(n2*n3,n1)
#y2 = inverse(n1*n3,n2)
#y3 = inverse(n1*n2,n3)
print((2*11*17*inverse(11*17,5) + 3*5*17*inverse(5*17,11) + 5*5*11*inverse(5*11,17)) % 935)