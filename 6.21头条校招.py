import sys
import traceback
# 贪心算法解决问题

n = int(input().strip())
b = sys.stdin.readline().strip().split(" ")
c = list(map(int,sorted(b, key=int)))
cur = c[0]
proSize = 1
totalNum = 0
i = 1
if (len(c) == 1 or len(c) == 0):
    print(2)
else:
    while (i < len(c)):
        if c[i] <= cur + 10:
            proSize += 1
        else:
            totalNum += 3 - proSize
            proSize = 1
        if proSize == 3:
            if (i + 1 < len(c)):
                i = i + 1
                proSize = 1
                cur =c[i]
            else:
                break
        else:
            cur = c[i]
            i += 1
    if (proSize != 0):
        totalNum += 3 - proSize
    print(totalNum)
