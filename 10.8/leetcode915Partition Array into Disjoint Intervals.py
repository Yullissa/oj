class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.max, self.min = [], []
        leftmax = A[0]
        for i in range(0, len(A)):
            leftmax = A[i] if A[i] > leftmax else leftmax
            self.max.append(leftmax)
        rightmin = A[-1]
        for i in range(len(A) - 1, -1, -1):
            rightmin = A[i] if A[i] < rightmin else rightmin
            self.min.append(rightmin)
        for i in range(0, len(A) - 1):
            if self.max[i] <= self.min[len(A) - i - 2]:
                return i + 1
        return len(A)


if __name__ == '__main__':
    test = Solution()
    A = [5, 0, 3, 8, 6]
    test.partitionDisjoint(A)
