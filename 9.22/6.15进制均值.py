# coding=utf-8
while (1):
    try:
        n = input()
        sum = 0
        for i in range(2, n - 1):
            while (n >= 1):
                sum += n % i
                n = n / i
            sum += n
        m = gcd(sum,n-2)
        if(sum % m == 0):
            print(sum/m)
        else:
            print(sum/m+"/"+(n-2)/m)
    except:
        pass

def gcd(n, m):
    while (m != 0):
        r = n % m
        n = m
        m = r
    return
