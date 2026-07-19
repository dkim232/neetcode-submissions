# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if p.val > q.val:
            temp = q
            q = p
            p = temp
        
        #p < q

        if not root:
            return None
        
        if (p.val <= root.val) and (q.val >= root.val):
            return root
        elif (p.val >= root.val) and (q.val >= root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else: #both less than
            return self.lowestCommonAncestor(root.left, p, q)