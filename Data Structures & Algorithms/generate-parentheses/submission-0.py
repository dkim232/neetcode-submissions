class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtracking

        res = []
        cur = ""
        numLeft = 0
        numRight = 0

        def backtrack(cur, numLeft, numRight):
            if numLeft == n and numRight == n:
                res.append(cur)
                return
            
            if numLeft < n: #need to put in more 
                backtrack(cur + "(", numLeft + 1, numRight)
            
            if numRight < numLeft: #can place right
                backtrack(cur + ")", numLeft, numRight + 1)

        backtrack("", numLeft, numRight)
        return res