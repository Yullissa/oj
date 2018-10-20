
try:
    n,m = input().strip().split(" ")
    n = int(n)
    m = int(m)

    if(n not in range(1,1025) or m not in range(1,1025)):
        print("-1")
    elif(n==m):
        print("1")
    else:
        print("0")
except:
    pass