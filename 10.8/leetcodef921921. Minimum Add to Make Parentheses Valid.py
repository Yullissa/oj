class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left = right = 0
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right
