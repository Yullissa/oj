import traceback

try:
    n = int(input())
    flagLen = 0
    flagLex = 0
    for i in range(0, n):
        cur = input()
        if i == 0:
            last = cur
        else:
            if len(cur) < len(last):
                flagLen = 1
            if cur < last:
                flagLex = 1
            if flagLex and flagLen:
                break
        last = cur
    if flagLex and flagLen:
        print("none")
    if flagLex and not flagLen:
        print("lengths")
    if not flagLex and  flagLen:
        print("lexicographically")
    if not flagLex and not flagLen:
        print("both")
except:
    traceback.print_exc()
    pass
