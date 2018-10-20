import traceback
# 根据回文的特征，判断第一个和最后一个即可
try:
    n = input()
    arr = list(map(int, input().strip().split()))
    ans = 0
    while (len(arr) > 0):
        le = len(arr) - 1
        if arr[0] == arr[le]:
            arr.pop(0)
            if len(arr) != 0:
                arr.pop(len(arr) - 1)
        elif arr[0] < arr[le]:
            arr[1] = arr[0] + arr[1]
            ans += 1
            arr.pop(0)
        elif arr[le] < arr[0]:
            arr[le - 1] = arr[le - 1] + arr[le]
            ans += 1
            arr.pop(le)
    print(ans)
except:
    traceback.print_exc()
    pass
