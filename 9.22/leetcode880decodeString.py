class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        N = 0
        for j, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N:
                break
        for i in range(j, -1, -1):
            if (S[i].isdigit()):
                N /= int(S[i])
                K %= N
            else:
                if K == N or K == 0:
                    return S[i]
                else:
                    N -= 1
