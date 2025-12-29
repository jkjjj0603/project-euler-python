num = 2 ** 1000
num_str = str(num)
snum = 0

for i in range(0,len(num_str)):
    inum = int(num_str[i])
    snum = inum + snum

print(snum)
