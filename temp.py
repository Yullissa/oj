def f(x):
    if x % 2 != 0:
        return x
    else:
        return f(int(x / 2))


if __name__ == '__main__':
    NUM = int(input("Please input the number:>"))
    SUM = 0
    for i in range(1, NUM + 1):
        SUM = SUM + f(i)
    print(SUM)
