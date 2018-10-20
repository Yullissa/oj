def height(X, node):
    l = len(X[node])
    r = 0
    for i in range(l):
        r = max(height(X, X[node][i]), r)
    return 1 + r


n = int(input())
X = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    if (len(X[x]) < 2):
        X[x].append(y)

print(height(X, 0))
