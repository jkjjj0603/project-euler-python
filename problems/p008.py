tot = 0
for a in range(1,333):
    for b in range(a+1,500):
        c = 1000 - a - b
        if c <= b:
            continue

        if a * a + b * b == c * c:
            tot = a * b * c

print(tot)


