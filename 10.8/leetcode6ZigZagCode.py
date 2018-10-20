class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ""

        for i in range(numRows):
            inter1 = (numRows - i - 1) * 2
            inter2 = (i - 0) * 2
            j = i
            # sp case:  "" 1
            if (j < len(s)):
                res += s[j]
            #   sp case : "AB" 1
            if inter1 == 0 and inter2 == 0:
                inter1 = 1
            while (j < len(s)):
                if inter1 != 0:
                    j += inter1
                if (j < len(s) and inter1 != 0):
                    res += s[j]
                if inter2 != 0:
                    j += inter2
                if (j < len(s) and inter2 != 0):
                    res += s[j]
        return res


if __name__ == '__main__':
    test = Solution()
    test.convert("PAYPALISHIRING", 3)
