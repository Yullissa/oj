from collections import Counter

import operator


class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        # traditional way
        # cnb = collections.Counter()
        # for b in B:
        #     for i, n in collections.Counter(b).items():
        #         cnb[i] = max(cnb[i], n)
        # res = []
        # for a in A:
        #     count = collections.Counter(a)
        #     if all(count[c] >= cnb[c] for c in cnb):
        #         res.append(a)
        # return res
        cnb = reduce(operator.ior, map(Counter, B))
        print [a for a in A if Counter(a) & cnb == cnb]


if __name__ == '__main__':
    test = Solution()
    test.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"])
