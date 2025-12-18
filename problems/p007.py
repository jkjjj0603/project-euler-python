def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

cnt = 0
num = 2

while True:
    if is_prime(num):
        cnt += 1
        if cnt == 10001:
            print(num)
            break
    num += 1
