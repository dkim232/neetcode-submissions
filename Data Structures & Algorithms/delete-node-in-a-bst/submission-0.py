# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == key:#found it
            if root.left and root.right: #both left and right exist
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                root = root.right
            elif root.left and not root.right: #left exists, right doesnt
                root = root.left
            elif root.right and not root.left:
                root = root.right
            else: #leaf node
                root = None
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root
