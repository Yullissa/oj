import collections

import itertools


class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        s = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(s, 2):
            k = target - i - j
            if k in s:
                if k == i == j:
                    res += s[i] * (s[i] - 1) * (s[i] - 2) // 6
                elif i == j != k:
                    res += s[i] * (s[i] - 1) // 2 * s[k]
                elif k > i and k > j:
                    res += s[i] * s[j] * s[k]
        return int(res % (1e9 + 7))
