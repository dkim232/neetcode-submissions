# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, pathMax):
            nonlocal res

            if not root:
                return
            
            if root.val >= pathMax:
                res += 1
                pathMax = root.val
            
            dfs(root.left, pathMax)
            dfs(root.right, pathMax)
        
        dfs(root, root.val)
        return res