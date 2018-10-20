import traceback
import bisect


# 另一种做法，简单，哈哈哈哈哈

# num = int(input())
# arr = [0, 1, 1]
# while num > arr[-1]:
#     arr.append(arr[-1] + arr[-2])
# print(min(arr[-1] - num, num - arr[-2]))

try:
    n = int(input())
    arr = [0] * 1000000
    arr[0] = 0
    arr[1] = 1
    i = 1
    while arr[i] <= 1000000:
        i = i + 1
        arr[i] = arr[i - 1] + arr[i - 2]
    arr = arr[:i]
    index = bisect.bisect_left(arr, n)
    rightNum = arr[index] if index < i else -1
    leftNum = arr[index - 1] if index - 1 >= 0 else -1
    if rightNum >= 0 and leftNum >= 0:
        rightGap = rightNum - n
        leftGap = n - leftNum
        gap = rightGap if rightGap <= leftGap else leftGap
    elif rightNum < 0:
        gap = n - leftNum
    elif leftNum < 0:
        gap = rightNum - n
    print(gap)
except:
    traceback.print_exc()
    pass
