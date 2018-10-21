class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shifts[-1] = shifts[-1] % 26
        for i in range(len(shifts) - 1, 0, -1):
            shifts[i - 1] = (shifts[i] + shifts[i - 1]) % 26
        res = ""
        for j in range(len(shifts)):
            ch = S[j]
            remove = shifts[j]
            if ord(ch) - ord('a') + remove > 25:
                res = res + res.join(chr(ord(ch) - 26 + remove))
            else:
                res = res + res.join(chr(ord(ch) + remove))

        res = res + res.join(S[len(shifts): len(S)])
        return res


if __name__ == '__main__':
    test = Solution()
    test.shiftingLetters("gdhbjaph",
                         [74, 34, 65, 30, 43, 91, 14, 10])
