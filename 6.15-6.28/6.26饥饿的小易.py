import traceback
# 遍历数列 x[i] = 2**i*(X+1)-1, i>=2.
# x[i+1] = 2x[i]+1; 对应的模 a[i+1] = (2*a[i]+1)%m
# https://blog.csdn.net/fcxxzux/article/details/52138964#t0
N = 1000000007
try:
    x = int(input())
    ans = 100001
    if x % N == 0:
        print("0")
    else:
        ax = (2 * (x + 1) - 1) % N
        for i in range(2, 300001):
            ax = (2 * ax + 1) % N
            if ax == 0:
                ans = i // 3 + (i % 3 != 0)
                break
        if ans < 100001:
            print(ans)
        else:
            print("-1")

except:
    traceback.print_exc()
    pass
