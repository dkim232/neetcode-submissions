# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()
        if not root:
            return res
        queue.append(root)

        while queue:
            numNodes = len(queue)
            temp = []
            for i in range(numNodes):
                curNode = queue.popleft()
                temp.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                #else continue
            res.append(temp)
        
        return res
        