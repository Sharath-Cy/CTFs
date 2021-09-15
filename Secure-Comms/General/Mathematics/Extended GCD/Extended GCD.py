
def gcd_extended(a,b):
    if a==0:
        return b,0,1
    gcd, p1, q1 = gcd_extended(b%a,a)

    x = q1-(b//a)*p1
    y = p1

    return gcd, x, y

p = 26513
q = 32321

gcd, u, v = gcd_extended(p,q)
print("GCD FLAG : crypto{{{},{}}}".format(u,v))