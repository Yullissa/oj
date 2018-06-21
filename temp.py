import sys
   
n = int(input())
d = sys.stdin.readline().strip().split(" ")
d = sorted(d, key=int)
dp = [0]*n
dp[0] = 2
for i in range(1,len(d)):
    if int(dp[i-1]) == 0:
        dp[i] = 2
        continue
    if int(d[i])-int(d[i-1]) >20:
        dp[i] = int(dp[i-1]) + 2
    else:
        dp[i] = int(dp[i-1]) -1
print(dp[n-1])