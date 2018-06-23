import math
import traceback


def isPrime(n):
    # math.sqrt(n)>2, n>=5
    # 取整
    # 取整之后>2 因此+1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


try:
    n = int(input().strip())
    # 2是最小的质数。1 不是质数
    primeList = [2, 3]
    totalNum = 0
    if n > 4:
        for num in range(4, n):
            if isPrime(num):
                primeList.append(num)
    for item1 in primeList:
        if item1+item1<=n and n-item1 in primeList :
                totalNum += 1
    print(totalNum)
except:
    traceback.print_exc()
    pass
