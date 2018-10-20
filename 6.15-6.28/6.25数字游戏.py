import traceback

try:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    N = 0
    flag = 0
    for item in arr:
        if item <= N + 1:
            N = N + item
        else:
            flag = 1
            print(N + 1)
            break
    if flag == 0:
        print(N + 1)


except:
    traceback.print_exc()
    pass
