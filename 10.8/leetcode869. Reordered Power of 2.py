import collections


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        num = 1
        cn = collections.Counter(str(N))

        while num <= 1e9:
            if cn == collections.Counter(str(num)):
                return True
            num *= 2
        return False