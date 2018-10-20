import traceback
import itertools

try:
    n, m = map(int, input().split())
    n = int(n)
    m = int(m)
    arr = list(map(int, input().split()))
    L = [i for i in range(1, n + 1)]
    L_not = list(set(L) - set(arr))
    unknownArray = list(itertools.permutations(L_not, len(L_not)))
    shunNum = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            for j in range(0, i):
                if arr[j] != 0 and arr[i] > arr[j]:
                    shunNum += 1
    ans = 0
    for arrtemp in unknownArray:
        addShun = 0
        j = 0
        arrPrim = [arr[i] for i in range(0, len(arr))]
        for i in range(0, len(arrPrim)):
            if arrPrim[i] == 0:
                arrPrim[i] = arrtemp[j]
                j += 1
                for k in range(0, i):
                    if arrPrim[k] != 0 and arrPrim[i] > arrPrim[k]:
                        addShun += 1
                for k in range(i, len(arr)):
                    if arrPrim[k] != 0 and arrPrim[i] < arrPrim[k]:
                        addShun += 1
        if addShun + shunNum == m:
            ans += 1
    print(ans)
except:
    traceback.print_exc()
    pass
