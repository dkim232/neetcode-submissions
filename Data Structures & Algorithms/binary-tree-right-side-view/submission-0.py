# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #right-most node of each level
        res = []
        if not root:
            return res
        
        dq = deque()
        dq.append(root)

        while dq:
            numvals = len(dq)
            for i in range(numvals):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
                if i < numvals-1:
                    continue
                else:
                    res.append(cur.val)

        return res