import traceback

T = int(input())
for i in range(0, T):
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        temp = [0] * 2 * n
        for q in range(0, k):
            for j in range(0, n):
                temp[2 * j] = arr[j]
                temp[2 * j + 1] = arr[n + j]
            for m in range(0, 2 * n):
                arr[m] = temp[m]
        print(" ".join(map(str, arr)))
    except:
        traceback.print_exc()
        pass

# 3
# 3 2
# 1 2 3 4 5 6
