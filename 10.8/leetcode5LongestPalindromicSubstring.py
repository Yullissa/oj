class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # BUG
        # dp = [[0] * n] * n
        dp = [[0 for i in range(n)] for j in range(n)]
        maxS = ""
        for d in range(n):
            for i in range(0, n - d):
                j = d + i
                if j == i or (s[j] == s[i] and j - 1 == 1):
                    dp[i][j] = True
                    if j - i + 1 > len(maxS):
                        maxS = s[i:j + 1]
                elif s[j] == s[i] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if j - i + 1 > len(maxS):
                        maxS = s[i:j + 1]
                else:
                    dp[i][j] = False
        return maxS


if __name__ == '__main__':
    test = Solution()
    test.longestPalindrome("babad")
