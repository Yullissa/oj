import traceback

try:
    n = int(input())
    arr = [200 for i in range(0,101)]
    arr[6]=1
    arr[8]=1
    for i in range(14,101):
        arr[i] = min(arr[i-6]+1,arr[i-8]+1)
    if arr[n]<200:
        print(arr[n])
    else :
        print("-1")
except:
    traceback.print_exc()
    pass