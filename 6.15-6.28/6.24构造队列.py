import traceback
from collections import deque
try:
    n = int(input())
    for i in range(0,n):
        m = int(input())
        # 初始化一个双向队列，必须使用deque()，变绿，否则用deque 是不对的
        q = deque()
        for j in range(m,0,-1):
            q.appendleft(j)
            t = q.pop()
            q.appendleft(t)
        print(" ".join(map(str,q)))
except:
    traceback.print_exc()
    pass