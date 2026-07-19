class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1):
                    self.markGrid(board, i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    
    def markGrid(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 'O':
            return
        grid[i][j] = 'M'
        self.markGrid(grid, i+1, j)
        self.markGrid(grid, i-1, j)
        self.markGrid(grid, i, j+1)
        self.markGrid(grid, i, j-1)