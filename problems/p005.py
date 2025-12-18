a = []
c = 600851475143

def pf(n):
    while n % 2 == 0:
        a.append(2)
        n //= 2
    
    d = 3
    while d * d <=n:
        while n % d ==0:
            a.append(d)
            n //= d
        d += 2

    if n > 1:
        a.append(n)


pf(c)
print(max(a))






