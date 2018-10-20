
#别人想出来的
#最优化方案：时间复杂的O(n*sum), 空间复杂度(sum)
n, sum = list(map(int,input().split()))
A = list(map(int,input().split()))
  
if sum == 0:
       print(1)
else:
       s = [0 for _ in range(sum)]
       for i in range(n):
             if A[i] > sum:
                   continue
             for j in range(sum-1-A[i], -1, -1):
                   if s[j] > 0:
                         s[j + A[i]] += s[j]
             s[A[i]-1] += 1
       print(s[-1])
  