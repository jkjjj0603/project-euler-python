num = 100
fac_num = 1
for i in range(1,101):
    fac_num = i * fac_num

num_str = str(fac_num)
snum = 0

for i in range(0,len(num_str)):
    inum = int(num_str[i])
    snum = snum + inum

print(snum)

