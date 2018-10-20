# coding=utf-8
# from math import gcd
def gcd(n, m):
    while (m != 0):
        r = n % m
        n = m
        m = r
    return n

while (1):
    try:
        n = int(input().strip())
        sum = 0
        for i in range(2, n):
            tempn = n
            while (tempn != 0):
                sum += tempn % i
                tempn = int(tempn / i)
        m = gcd(sum, n - 2)
        print(str(int(sum / m)) + "/" + str(int((n - 2) / m)))
    except:
        break

# 5
# 3
#
# 7/3
# 2/1