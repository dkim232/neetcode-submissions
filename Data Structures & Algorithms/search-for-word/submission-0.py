class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i,j,index):
            if index >= len(word):
                return True
            
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            
            if board[i][j] != word[index]:
                return False
            
            #valid index, and letter matches

            temp = board[i][j]
            board[i][j] = "#"

            foundWord = dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)

            board[i][j] = temp
            return foundWord
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
    


                