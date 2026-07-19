class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.sinkIslands(grid, i, j)
                    res += 1
        return res
    

    def sinkIslands(self, grid, i, j):
        #exit condition:
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])):
            return
        if grid[i][j] == '1': #change the tile and keep searching
            grid[i][j] = '0'
            self.sinkIslands(grid, i+1, j)
            self.sinkIslands(grid, i-1, j)
            self.sinkIslands(grid, i, j+1)
            self.sinkIslands(grid, i, j-1)
            
