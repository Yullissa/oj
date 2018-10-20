class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        res = (1 << N - 1) * M
        # not needed
        # for i in range(len(A)):
        #     if A[i, 0] == 0:
        #         for j in range(len(A[i])):
        #             A[i, j] = 1 - A[i, j]
        for j in range(1, N):
            cur = sum(A[i][j] == A[i][0] for i in range(N))
            res += max(M - cur, cur) * (1 << N - 1 - j)
        return res
