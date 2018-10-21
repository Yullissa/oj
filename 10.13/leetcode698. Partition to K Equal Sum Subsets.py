class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        self.target, res = divmod(sum(nums), k)
        if res: return False

        def search(groups):
            if (len(nums) == 0): return True
            v = nums.pop()

            for i, group in enumerate(groups):
                if group + v <= self.target:
                    groups[i] += v
                    if (search(groups)):
                        return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > self.target:
            return False
        while nums and nums[-1] == self.target:
            nums.pop()
            k -= 1
        return search([0] * k)

# import copy
#
#
# class Solution:
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         # if k == 1: return True
#         # self.n = len(nums)
#         # if k > self.n:
#         #     return False
#         # totle = sum(nums)
#         # if totle % k: return False
#         # self.target = totle // k
#         # visit = [0] * self.n
#         # nums.sort(reversed=True)
#         #
#         # def dfs(k, ind, sum, cnt):
#         #     if k == 1: return True
#         #     if sum == self.target and cnt > 0:
#         #         return dfs(k - 1, 0, 0, 0)
#         #     for i in range(ind, self.n):
#         #         if not visit[i] and sum + nums[i] < self.target:
#         #             visit[i] = 1
#         #             if dfs(k, i + 1, sum - nums[i], cnt + 1):
#         #                 return True
#         #             visit[i] = 0
#         #     return False
#         #
#         # return dfs(k, 0, 0, 0)
#         # own wrong not pass
#         target = sum(nums) // k
#
#         self.n = len(nums)
#         visit = [0] * len(nums)
#
#         def digui( idx, target):
#             if (target == 0):
#
#             elif (len(nums) <= 0):
#                 return False
#             for i in range(idx,self.n):
#                 item = nums[0]
#                 if target - item in nums:
#                     self.K -= 1
#                     nums.remove(item)
#                     nums.remove(target - item)
#                     digui(nums, target)
#                 else:
#                     numstemp = copy.copy(nums)
#                     numstemp.remove(item)
#                     digui(numstemp, target - item)
#                     nums.remove(item)
#                     self.K -= 1
#                     return True
#             return False
#
#         if digui(nums, target) and self.K == 0:
#             return True
#         return False
#
#
# if __name__ == '__main__':
#     test = Solution()
#     test.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1]
#                               , 4)
