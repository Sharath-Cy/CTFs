
#a= 12
#b= 8

a = 66528  
b = 52920

if a < b:
    b = b-a

def gcd(a,b):

    while b!=0:
        t = b
        b = a % b
        a = t
    return a

print("GCD of given value is : {}".format(gcd(a,b)))