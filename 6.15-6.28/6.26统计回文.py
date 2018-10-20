import traceback

# 两行的解法
# a, b = input(), input()
# print(sum(map(lambda c: c == c[::-1], map(lambda x: a[:x] + b + a[x:], range(len(a) + 1)))))

try:
    n = input().strip()
    m = input().strip()
    ans = 0
    # 简单的for 循环都可以写成lambda表达式
    temp = map(lambda x: n[:x] + m + n[x:],  range(0, len(n) + 1))
    for item in temp:
        print(item)
        if (item == item[::-1]):
            ans += 1
    print(ans)
except:
    traceback.print_exc()
    pass
