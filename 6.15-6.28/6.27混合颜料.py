import traceback

try:
    def getHiBit(n):
        ans = 0
        while n:
            ans += 1
            n >>= 1
        return ans

    n = int(input())
    color = list(map(int, input().split()))
    color.sort(reverse=True)
    i = 0
    while i < len(color) and color[i]:
        hibit = getHiBit(color[i])
        for j in range(i + 1, len(color)):
            if getHiBit(color[j]) == hibit:
                color[j] ^= color[i]
            else :
                break
        color.sort(reverse=True)
        i += 1
    print(i)
except:
    traceback.print_exc()
    pass
