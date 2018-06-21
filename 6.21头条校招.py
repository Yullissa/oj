import sys
import traceback

n = int(input().strip())
b = sys.stdin.readline().strip().split(" ")
c = sorted(b, key=int)
cur = int(c[0])
proSize = 1
totalNum = 0
i = 1
if (len(c) == 1 or len(c) == 0):
    print(2)
else:
    while (i < len(c)):
        if int(c[i]) <= cur + 10:
            proSize += 1
        else:
            totalNum += 3 - proSize
            proSize = 1
        if proSize == 3:
            if (i + 1 < len(c)):
                i = i + 1
                proSize = 1
                cur = int(c[i])
            else:
                break
        else:
            cur = int(c[i])
            i += 1
    if (proSize != 0):
        totalNum += 3 - proSize
    print(totalNum)
