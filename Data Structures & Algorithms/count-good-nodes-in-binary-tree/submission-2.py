# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #keep track of the max value along the path
        res = 0

        def dfs(root,maxval):
            nonlocal res

            if not root:
                return
            if root.val >= maxval: #good node; update res and maxval
                res += 1
                maxval = root.val
            
            dfs(root.left, maxval)
            dfs(root.right, maxval)

        dfs(root, root.val)
        return res