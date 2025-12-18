palindrome_max = 0
palindrome = 0

def ispalindrome(n):
    a = len(str(n))
    if a % 2 == 0 and int(str(n)[::-1]) == int(n):
        return n
    elif a % 2 == 1 and int(str(n)) == int(str(n)[::-1]):
        return n
    else:
        return 0

for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        palindrome = ispalindrome(num)
        if palindrome_max < palindrome:
            palindrome_max = palindrome
            
print(palindrome_max)



