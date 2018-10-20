import traceback
import sys

try:
    n, m, p = list(map(int, input().strip().split()))
    maxInt = 200
    arr = [[0 for _ in range(0, m)] for _ in range(0, n)]
    for i in range(0, n):
        arr[i] = list(map(int, input().strip().split()))
    queueList = [(0, 0)]
    cost = [[maxInt for _ in range(0, m)] for _ in range(0, n)]
    cost[0][0] = 0
    pre = [[(-1, -1) for _ in range(0, m)] for _ in range(0, n)]

    flag = 1
    # DFS广度优先搜索
    while (len(queueList) != 0):
        raw, col = queueList.pop(0)
        if (cost[raw][col] > p):
            flag = 0
            break
        if (col + 1 < m and arr[raw][col + 1] == 1 and cost[raw][col + 1] > cost[raw][col] + 1):
            cost[raw][col + 1] = cost[raw][col] + 1
            pre[raw][col + 1] = (raw, col)
            queueList.append((raw, col + 1))
        if (col - 1 >= 0 and arr[raw][col - 1] == 1 and cost[raw][col - 1] > cost[raw][col] + 1):
            cost[raw][col - 1] = cost[raw][col] + 1
            pre[raw][col - 1] = (raw, col)
            queueList.append((raw, col - 1))
        if (raw + 1 < n and arr[raw + 1][col] == 1 and cost[raw + 1][col] > cost[raw][col]):
            cost[raw + 1][col] = cost[raw][col]
            pre[raw + 1][col] = (raw, col)
            queueList.append((raw + 1, col))
        if (raw - 1 >= 0 and arr[raw - 1][col] == 1 and cost[raw - 1][col] > cost[raw][col] + 3):
            cost[raw - 1][col] = cost[raw][col] + 3
            pre[raw - 1][col] = (raw, col)
            queueList.append((raw - 1, col))
    resPath = [(0, m - 1)]
    if (flag):
        rawCur = 0
        colCur = m - 1
        while (rawCur != 0 or colCur != 0):
            resPath.append((pre[rawCur][colCur]))
            (rawCur, colCur) = pre[rawCur][colCur]
        # 记住去掉列表中的空格
        resPath = str(resPath[::-1]).strip("[").strip("]").replace("(","[").replace(")","]").replace(" ","")
        print(resPath)

    else:
        print("Can not escape!")
except:
    traceback.print_exc()
pass


# 4 4 10
#  1 0 0 1
# 1 1 0 1
#  0 1 1 1
#  0 0 1 1
