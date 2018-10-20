import collections


class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            # dictlike object
            # use list to solve the problem that same key occurs for multiple times
            # >> > s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
            # >> > d = defaultdict(list)
            # >> > for k, v in s:
            #     ...
            #     d[k].append(v)
            # ...
            # >> > d.items()
            # [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
            if b < A[-1]: take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
