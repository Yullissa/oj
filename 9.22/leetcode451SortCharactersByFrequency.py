import collections
import heapq


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sArr = [word for word in s]
        collect = collections.Counter(sArr)
        # heap = [(-freq, word) for (word, freq) in collect.items()]
        # heapq.heapify(heap)
        # n = len(collect)
        l = sorted(collect.items, key=lambda l: l[1], reverse=True)
        rArr = []
        for word,freq in l:
            rArr.append(word * (-freq))
        return ''.join(rArr)
