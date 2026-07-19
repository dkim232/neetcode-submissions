# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ### first value of preorder
        ### using in-order, left subtree is to the left of 1
        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])
        
        indexRoot = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                indexRoot = i
        root.left = self.buildTree(preorder[1:indexRoot+1], inorder[:indexRoot])
        root.right = self.buildTree(preorder[indexRoot+1:], inorder[indexRoot+1:])


        return root