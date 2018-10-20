import traceback
#注意负数情况
#注意结果反转
arrRest = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E','F']
try:
    dain = list(map(int,input().strip().split()))
    n = int(dain[0])
    m = int(dain[1])
    res = ""
    flag = 0
    if (n < 0):
        flag = 1
        n = -n
    while (n >= m):
        c = int(n % m)
        n = int(n / m)
        res += str(arrRest[c])
    res += str(arrRest[n])
    res = res[::-1]
    if (flag):
        res = "-"+res
    print(res)
except:
    traceback.print_exc()
    pass
