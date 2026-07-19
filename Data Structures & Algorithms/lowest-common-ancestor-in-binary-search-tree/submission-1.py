# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #a node can be a descendent of itself
        #binary search tree is big hint!

        if p.val > q.val:
            temp = q
            q = p
            p = temp


        if root is None:
            return None
        
        if (p.val <= root.val) and (root.val <= q.val): #success
            return root
        
        elif (p.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
            