p = 29
ints = [14, 6, 11]

value = [a for a in range(p) if pow(a,2,p) in ints]
print(min(value))
        