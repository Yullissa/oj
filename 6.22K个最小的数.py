import traceback
from queue import PriorityQueue as PQueue

try:
    n = list(map(int, input().strip().split()))
    m = n[-1]
    n = n[:-2]
    n = sorted(n)
    print(" ".join(map(str,n[0:m])))

except:
    traceback.print_exc()
    pass
