# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])

        rootIndex = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                rootIndex = i

        #root index tells us how many nodes are in the left subtree
        #left subtree: 
        root.left = self.buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])   
        root.right = self.buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])     

        return root