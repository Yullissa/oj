import traceback
import bisect

try:
    n, m = map(int, input().strip().split())
    # zhuozi = sorted(list(map(int, input().strip().split())))

    zhuozi = [int(x) for x in input().split()]
    keren = [[int(x) for x in input().split()] for i in range(m)]
    # keren = []
    # # 低效
    # for i in range(0, m):
    #     keren.append(list(map(int, input().strip().split())))
    keren = sorted(keren, key=lambda x: (x[1], x[0]), reverse=True)
    zhuozi.sort()
    totalMoney = 0
    # for ren, jia in keren:
    while (len(keren)!=0):
        ren,jia = keren.pop(0)
        if len(zhuozi) == 0:
            break
        index = bisect.bisect_left(zhuozi, ren)
        if (index == len(zhuozi)):
            continue
        else:
            totalMoney += jia
            zhuozi.pop(index)
    print(totalMoney)
except:
    traceback.print_exc()
    pass

# 3 5
# 2 4 2
# 1 3
# 3 5
# 3 7
# 5 9
# 1 10
