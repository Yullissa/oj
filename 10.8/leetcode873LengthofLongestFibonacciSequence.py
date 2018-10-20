# class Solution:
#     def lenLongestFibSubseq(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         s = set(A)
#         res = 2
#         for i in range(len(A)):
#             for j in range(i + 1, len(A)):
#                 a, b, l = A[i], A[j], 2
#                 while a + b in s:
#                     a, b, l = b, a + b, l + 1
#                 res = max(res, l)
#         return res if res > 2 else 0

# way2
import collections


class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        s = set(A)
        res = 0
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    # [xiao, da]
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
                    res = max(res, dp[A[i], A[j]])
        return res
