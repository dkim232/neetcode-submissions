class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curArea = self.countArea(grid, i, j)
                    maxArea = max(maxArea, curArea)
        return maxArea
    
    def countArea(self, grid, i, j):
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or (grid[i][j] != 1):
            return 0

        grid[i][j] = 0
        
        return 1 + self.countArea(grid, i+1, j) + self.countArea(grid, i-1, j) + self.countArea(grid, i, j+1) + self.countArea(grid, i, j-1)