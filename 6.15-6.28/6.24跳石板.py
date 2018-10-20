import sys

# 用空间换时间 巧妙的求解 约数的方法

def jump(N, M):
    divs = [[] for _ in range(M + 1)]
    for i in range(2, M + 1):
        for j in range(i + i, M + 1, i):
            divs[j].append(i)
    res = [0] * (M + 1)
    res[N] = 1
    for n in range(N, M):
        if res[n]:
            for dn in divs[n]:
                if n + dn <= M:
                    res[n + dn] = min(res[n + dn], res[n] + 1) if res[n + dn] else res[n] + 1
    return res[M] - 1 if res[M] else -1


if __name__ == '__main__':
    try:
        std_in = sys.stdin
        ##        std_in = open("parlindromes.txt")
        while True:
            line = std_in.readline()
            if line == '':
                break
            line = [int(t) for t in line.splitlines()[0].split()]
            print(jump(line[0], line[1]))
    except:
        pass