import traceback
import math
import bisect

try:
    n = int(input())
    m = int(math.sqrt(n))
    ans = 0
    if m * m == n:
        ans += 4
    arr = [0] * (m + 1)
    for i in range(0, m + 1):
        arr[i] = i * i
    i = 1
    while (i * i <= int(n / 2)):
        index = bisect.bisect_left(arr, n - i * i)
        if index <= m:
            if arr[index] == n - i * i:
                if i * i * 2 == n:
                    ans += 4
                else:
                    ans += 8
        i = i + 1
    print(ans)
except:
    traceback.print_exc()
    pass
