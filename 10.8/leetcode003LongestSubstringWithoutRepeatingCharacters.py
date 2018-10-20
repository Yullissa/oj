class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 自己写的，AC,但是自己觉得时间复杂度高了
        # n = len(s)
        # maxlen = 0
        # if n == 0:
        #     return 0
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if s[j] in s[i:j]:
        #             break
        #         else:
        #             maxlen = max(maxlen, j - i)
        # return maxlen + 1

        # AC O(N)
        n = len(s)
        j = 0
        wordMap = {}
        maxlen = 0
        for i in range(n):
            if s[i] in wordMap.keys():
                j = max(j, wordMap.get(s[i]) + 1)
            wordMap.update({s[i]: i})
            maxlen = max(maxlen, i - j + 1)
        return maxlen
