class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        layer = 0
        res = 0
        for i, j in zip(S, S[1:]):
            layer += 1 if i == '(' else -1
            if i + j == '()': res += 2 ** (layer - 1)
        return res