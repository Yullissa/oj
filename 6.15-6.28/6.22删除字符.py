import traceback

try:
    n = input().strip()
    delstr = input().strip()
    for ch in delstr:
        n = n.replace(ch,'')
    print(n)
except:
    traceback.print_exc()
    pass