# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def deep(root):
            if not root:
                return 0, None

            left = deep(root.left)
            right = deep(root.right)
            if left[0] == right[0]:
                return left[0] + 1, root
            if left[0] > right[0]:
                return left[0]+1,left[1]
            if right > left:
                return right[0]+1,right[1]
        return deep(root)[1]
