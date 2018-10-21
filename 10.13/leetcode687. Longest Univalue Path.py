# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    maxdist = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if (root == None):
                return 0
            if (root.left == None and root.right == None):
                return 0
            leftnum = 0
            if (root.left != None):
                leftsingle = dfs(root.left)
                if (root.left.val == root.val):
                    leftnum = leftsingle + 1

            rightnum = 0
            if (root.right != None):
                rightsingle = dfs(root.right)
                if (root.right.val == root.val):
                    rightnum = rightsingle + 1
            self.maxdist = max(self.maxdist, leftnum + rightnum)
            return max(leftnum, rightnum)

        dfs(root)
        return self.maxdist

