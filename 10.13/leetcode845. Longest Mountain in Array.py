import copy


class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res
        # own AC but long and easy to make mistake
        # if len(A) == 0:
        #     return 0
        # i = 1
        # maxtemp = 0
        # while (i < len(A)):
        #     temp = 0
        #     while (i < len(A) and A[i] > A[i - 1]):
        #         temp += 1
        #         i += 1
        #     if temp == 0:
        #         i += 1
        #         continue
        #     k = i
        #     while (k < len(A) and A[k - 1] > A[k]):
        #         temp += 1
        #         k += 1
        #     if k == i:
        #         i = k + 1
        #         continue
        #     i = k
        #     maxtemp = max(maxtemp, temp)
        # if maxtemp >= 2:
        #     return maxtemp + 1
        # else:
        #     return 0
    # AC but Can you solve it using only one pass?
# Can you solve it in O(1) space??
# if len(A) == 0:
#     return 0
# left = [0] * len(A)
# right = [0] * len(A)
# left[0] = 0
# for i in range(len(A) - 1):
#     if A[i] < A[i + 1]:
#         left[i + 1] = left[i] + 1
#     else:
#         left[i + 1] = 0
# right[len(A) - 1] = 0
# for i in range(len(A) - 2, -1, -1):
#     if A[i] > A[i + 1]:
#         right[i] = right[i + 1] + 1
#     else:
#         right[i] = 0
# maxtemp = 0
# for i in range(len(A)):
#     if left[i] != 0 and right[i] != 0:
#         maxtemp = max(maxtemp, left[i] + right[i])
# if maxtemp >= 2:
#     return maxtemp + 1
# else:
#     return 0
