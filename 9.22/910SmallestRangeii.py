class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        if n <= 1:
            return 0
        A.sort()
        right = A[-1] - K
        left = A[0] + K
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            maxn = max(A[i] + K, right)
            minn = min(A[i + 1] - K, left)
            res = min(res,maxn - minn)
        return res


if __name__ == '__main__':
    A = [1, 3, 6]
    K = 3
    t = Solution()
    t.smallestRangeII(A, K)
