import traceback
# 选举思想
try:
    n = map(int,input().strip().split())
    reslist = []
    for item in n:
        if len(reslist)==0:
            reslist.append(item)
        else:
            if(reslist[0] == item):
                reslist.append(item)
            else:
                reslist.pop()
    print(reslist[0])


except:
    traceback.print_exc()
    pass