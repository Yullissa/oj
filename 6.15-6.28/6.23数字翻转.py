import traceback

try:
    n, m = input().strip().split()
    n = n[::-1]
    m = m[::-1]
    res = int(n)+ int(m)
    res = str(res)
    print(res[::-1].lstrip('0'))

except:
    traceback.print_exc()
    pass
