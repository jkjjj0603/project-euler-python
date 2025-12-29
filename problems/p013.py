cnt = 0
max_cnt = 0
n = 0
num = 0
for i in range(1,1000000):
    cnt = 0
    n = i
    while True:
        if n % 2 == 0:
            n = n // 2
            cnt += 1
        elif n % 2 != 0:
            n = 3 * n + 1
            cnt += 1
        if n == 1:
            break
    if cnt > max_cnt:
            max_cnt = cnt
            num = i
    
print(num)
