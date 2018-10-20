class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # O(N2) TLE  Time Limit Exceeded
        # B = A + A
        # maxtemp = -30001
        # for i in range(len(A)):
        #     res = B[i]
        #     maxtemp = max(maxtemp, res)
        #     j = i + 1
        #     while (res >= 0 and j < i + len(A)):
        #         res += B[j]
        #         maxtemp = max(maxtemp, res)
        #         j = j + 1
        # return maxtemp
        total, maxtemp, curmax, mintemp, curmin = 0, -30000, 0, 30000, 0
        for a in A:
            curmax = max(curmax + a, a)
            maxtemp = max(maxtemp, curmax)
            curmin = min(curmin + a, a)
            mintemp = min(mintemp, curmin)
            total += a
        return max(maxtemp, total - mintemp) if maxtemp > 0 else maxtemp
