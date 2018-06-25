import traceback

try:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0] * 100000 * 20
    arr.sort()
    ans[arr[0]] = 1
    arrtemp = []
    arrtemp.append(arr[0])
    for i in range(1, len(arr)):
        if ans[arr[i]] == 0:
            ans[arr[i]] = 1
            arrtemp.append(arr[i])
        for j in range(0, i):
            if ans[arr[i] + arr[j]] == 0:
                arrtemp.append(arr[i] + arr[j])
                ans[arr[i] + arr[j]] = 1
        le = len(arrtemp)
        for k in range(0, le):
            if ans[arr[i] + arrtemp[k]] == 0:
                arrtemp.append(arr[i] + arrtemp[k])
                ans[arr[i] + arrtemp[k]] = 1
    for j in range(1, 20 * 100000):
        if ans[j] == 0:
            print(j)
            break
except:
    traceback.print_exc()
    pass
