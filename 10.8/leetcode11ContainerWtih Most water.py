class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxtemp = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxtemp = max(maxtemp, min(height[i], height[j]) * (j - i))
            if (height[i] < height[j]):
                i += 1
            if (height[i] > height[j]):
                j -= 1

        # n^2 TLE
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         cur = min(height[i], height[j]) * (j - i)
        #         maxtemp = max(cur, maxtemp)
        return maxtemp
