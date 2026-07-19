# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in-order traversal dfs: left root right
        counter = 0
        ans = 0
    

        def inorder(root):
            nonlocal counter
            nonlocal ans
            ##base case: k-th index OR none
            if not root:
                return
            
            ##this is a node.
            inorder(root.left)
            counter += 1
            if counter == k:
                ans = root.val
            inorder(root.right)
        
        inorder(root)
        return ans