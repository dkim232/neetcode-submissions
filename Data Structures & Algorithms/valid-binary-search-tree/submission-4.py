# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, maxval, minval):
            #maxvalue of left subtree must be less than root value
            #minval of right subtree must be greater than root value

            if not root:
                return True
            
            if root.val >= maxval or root.val <= minval:
                return False
            

            return dfs(root.right, maxval, root.val) and dfs(root.left, root.val, minval)
        
        return dfs(root, float('inf'), float('-inf'))