import traceback

try:
    n = input()
    apple = list(map(int, input().split()))
    sumApple = sum(apple)
    if sumApple % int(n) != 0:
        print("-1")
    else:
        diff = []
        red = 0
        avg = sumApple // int(n)
        for i in range(int(n)):
            diff.append(apple[i] - avg)
            if abs(diff[i]) % 2 != 0:
                print("-1")
                exit()
        for i in range(len(diff)):
            if diff[i] > 0:
                red += diff[i]
        print(red // 2)
except:
    traceback.print_exc()
    pass
