import traceback

try:
    n = int(input().strip())
    arrRaw = list(map(int,input().split()))
    arrCol = list(map(int,input().split()))
    print(min(map(lambda x:abs(arrRaw[x]-1)+abs(arrCol[x]-1),range(n))))
except:
    traceback.print_exc()
    pass