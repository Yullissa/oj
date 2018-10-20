import traceback
import sys
try:
    n = input()
    maxSum = int(-sys.maxsize)
    tempSum = 0
    for x in input().split():
        tempSum += int(x)
        if tempSum > maxSum:
            maxSum = tempSum
        if (tempSum<0):
            tempSum = 0
    print(maxSum)

except:
    traceback.print_exc()
    pass

# 3
# -1 2 1
# 3
