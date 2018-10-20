import traceback

try:
    n = input().strip().split()
    print(' '.join(map(str,n[::-1])))
except:
    traceback.print_exc()
    pass