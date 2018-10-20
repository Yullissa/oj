import traceback

try:
    n, m = map(int, input().split())
    arr = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(0, 500, 1):
        for j in range(0, 500, 1):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                arr[2 * i][2 * j] = 1
                arr[2 * i + 1][2 * j] = 1
                arr[2 * i + 1][2 * j + 1] = 1
                arr[2 * i][2 * j + 1] = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                ans += 1
    print(ans)

except:
    traceback.print_exc()
    pass
