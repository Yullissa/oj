class Solution:

    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        def helper(S, idx):
            if (idx == len(S) and len(ans) >= 3):
                return True
            i = idx
            while (i < len(S)):
                if (S[idx] == '0' and i > idx):
                    return False
                num = int(S[idx:i + 1])
                if (num > 1 << 32 - 1):
                    break
                if (len(ans) >= 2 and num > int(ans[len(ans) - 1]) + int(ans[len(ans) - 2])):
                    break
                if (len(ans) <= 1 or num == int(ans[len(ans) - 1]) + int(ans[len(ans) - 2])):
                    ans.append(num)
                    if (helper(S, i+1)):
                        return True
                    ans.pop()
                i += 1
            return False

        ans = []
        helper(S, 0)
        return ans

if __name__ == '__main__':
    test =Solution()
    test.splitIntoFibonacci("123456579")