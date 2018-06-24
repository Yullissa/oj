import traceback

try:
    n1, n2, n3, n4 = map(int, input().split())
    a = int((n1 + n3) / 2)
    b = int((n2 + n4) / 2)
    c = n4 - b
    if (a - b == n1 and b - c == n2 and a + b == n3 and b + c == n4):
        print("{} {} {}".format(a, b, c))
    else:
        print("No")
except:
    traceback.print_exc()
    pass
