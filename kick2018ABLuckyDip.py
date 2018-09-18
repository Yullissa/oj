import bisect

casenum = 0
with open("B-large-practice.in", "r") as fin:
    with open("B.out", "w") as fout:
        n = int(fin.readline())
        for i in range(n):
            casenum = casenum + 1
            N, K = map(int, fin.readline().strip().split(" "))
            arr = map(float, fin.readline().strip().split(" "))
            arr.sort()
            EV = sum(arr) / N
            for j in range(0, K, 1):
                lowCount = bisect.bisect_left(arr, EV)
                EV = lowCount * EV / N + sum(arr[lowCount:]) / N
            fout.write("Case #{}: {}\n".format(casenum, EV))
