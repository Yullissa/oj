import collections


class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(quiet)
        link = collections.defaultdict(list)
        for item in richer:
            link[item[1]].append(item[0])

        def dfs(i):
            if res[i] != -1:
                return res[i]
            else:
                res[i] = i
                for j in link[i]:
                    if quiet[res[i]] > quiet[dfs(j)]:
                        res[i] = res[j]
                return res[i]

        for i in range(len(quiet)):
            if res[i] == -1:
                dfs(i)
        return res
