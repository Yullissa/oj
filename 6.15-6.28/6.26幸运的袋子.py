import traceback
import bisect

#这个问题是求有重复数字的集合的所有子集的一个扩展
#加了限制条件，这些限制条件恰好可以用来剪枝
def dfs(x, pos, s, p):#s为和，p为积，pos为初始位置
    ans=0
    i=pos
    while i<n:
        if s+x[i]>p*x[i]:
            ans+=1+dfs(x,i+1,s+x[i],p*x[i])
        elif x[i]==1: 
            ans+=dfs(x,i+1,s+1,p)
        else: 
            break
        while i<n-1 and x[i]==x[i+1]: 
            i+=1
        i+=1
    return ans
 
n=int(input())
x = sorted(list(map(int, input().split())))#对x从小到大进行排序
print(dfs(x,0,0,1))
# try:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     ans = 0
#     last = arr[0]
#     index = bisect.bisect(arr, 1)
#     redunOne = 0
#     if index > 1:
#         redunOne = index - 1
#     S = arr[redunOne]
#     N = arr[redunOne]
#     for i in range(redunOne + 1, len(arr)):
#         S = S + arr[i]
#         N = N * arr[i]
#         diff = S - N
#         if diff > 0:
#             ans += 1 + redunOne
#         elif diff <= 0 and redunOne > abs(diff):
#             ans += redunOne - abs(diff)
#     ans += redunOne
#     print(ans)
# 
# except:
#     traceback.print_exc()
#     pass
