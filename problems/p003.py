def sqrt_sum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i * i
    return total

def sum_sqrt(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total * total
a = sqrt_sum(100)
b = sum_sqrt(100)
print(b - a)
