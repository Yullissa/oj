import traceback

# 自己的思路：推出来对A分支而言，3可分裂为一个3和2个2，因此3有上一次的3的个数加上2的个数的和那么多，2的个数有上次3的个数的2被+2的个数那么多
# 则对总的来说是3倍的关系
#更加巧妙的思路：这种递推关系都可以写成递推方程，使用动态规划求解，2f(n-1)+f(n-2)即可
try:
    n = int(input())
    arr3 = [0 for i in range(0, 31)]
    arr2 = [0 for i in range(0, 31)]

    arr3[2] = 1
    arr2[2] = 2
    for i in range(3, 31):
        arr3[i] = arr3[i - 1] + arr2[i - 1]
        arr2[i] = arr3[i - 1] * 2 + arr2[i - 1]
    if n==1:
        print("3")
    elif n==2:
        print("9")
    else:
        print((arr3[n-1]*3 + arr2[n-1]*2) * 3)

except:
    traceback.print_exc()
    pass
