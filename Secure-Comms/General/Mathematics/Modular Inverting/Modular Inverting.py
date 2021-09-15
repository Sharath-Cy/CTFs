#3 * d ≡ 1 mod 13?
#reference  https://cp-algorithms.com/algebra/module-inverse.html
a = 3
p = 13
print(pow(a,p-2) % p)