p = 28151
g = 2
flag = False
while not flag:
    for n in range(2,p):
        if pow(g,n,p) ==1:
         break
        if n == p-2:
            print(g)
            flag = True
    g=g+1