import traceback
# 回溯法
def backtracing(t, temp, sum, n, m):
    if (sum == m):
        print(" ".join(map(str, temp)))
    else:
        for i in range(t + 1, n + 1):
            if i + sum <= m:
                temp.append(i)
                backtracing(i, temp, sum + i, n, m)
                temp.pop()
try:
    n, m = input().strip().split()
    n = int(n)
    m = int(m)
    backtracing(0, [], 0, n, m)
except:
    traceback.print_exc()
