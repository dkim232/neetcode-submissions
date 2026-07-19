# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        pq = deque()
        pq.append(root)

        while pq:
            numElements = len(pq)
            curLevel = []
            for i in range(numElements):
                curNode = pq.popleft()
                if not curNode:
                    return res
                curLevel.append(curNode.val)
                if curNode.left:
                    pq.append(curNode.left)
                if curNode.right:
                    pq.append(curNode.right)
            res.append(curLevel)
        return res