import bisect


class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N, self.L = N, []

    def seat(self):
        """
        :rtype: int
        """
        N, L = self.N, self.L
        d, res = L[0] // 2, 0
        if not L:
            res = 0
        else:
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.L.pop(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
