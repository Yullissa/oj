import re
import traceback

try:
    n = input()
    m = input()
    pat = ".*"
    for i in m:
        pat += i + ".*"
    if re.match(pat, n):
        print("Yes")
    else:
        print("No")
except:
    traceback.print_exc()
    pass
