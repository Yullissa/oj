import traceback
import math

try:
    n = int(input())
    if n ==1:
        print(0)
    else:
        for i in range(int(math.sqrt(n)), 0,-1):
            if i * i + i <= n:
                print(i)
                break

except:
    traceback.print_exc()
    pass
