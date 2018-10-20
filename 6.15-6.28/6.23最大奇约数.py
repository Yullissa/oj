import traceback
import math

try:
    res = 0
    n = int(input())
    while (n > 0):
        temp = int((n + 1) / 2)
        res += temp * temp
        n = n / 2
    print(res)

except:
    traceback.print_exc()
    pass
