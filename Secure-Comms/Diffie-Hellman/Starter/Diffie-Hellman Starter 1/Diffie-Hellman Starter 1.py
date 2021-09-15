p = 991
g = 209
#d = ?, such that g*d mod 991=1

for d in range(991):
    if (g*d)%991==1:
        print(d)
        break