# public boolean PredictTheWinner(int[] nums) {
#     if (nums == null) { return true; }
#     int n = nums.length;
#     if ((n & 1) == 0) { return true; } // Improved with hot13399's comment.
#     int[] dp = new int[n];
#     for (int i = n - 1; i >= 0; i--) {
#         for (int j = i; j < n; j++) {
#             if (i == j) {
#                 dp[i] = nums[i];
#             } else {
#                 dp[j] = Math.max(nums[i] - dp[j], nums[j] - dp[j - 1]);
#             }
#         }
#     }
#     return dp[n - 1] >= 0;
# }
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        n = len(nums)
        if n & 1 == 0:
            return True
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[j] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[n - 1] >= 0
