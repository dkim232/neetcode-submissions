class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.findLength(grid,i,j,0)
        
        

    def findLength(self, grid,i,j,distance):
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or (grid[i][j] == -1): #not valid i,j or not land:
            return
        

        ##here, the grid position IS land.
        if grid[i][j] < distance:
            return
        else:
            grid[i][j] = distance
            self.findLength(grid, i+1, j, distance+1)
            self.findLength(grid, i-1, j, distance+1)
            self.findLength(grid, i, j+1, distance+1)
            self.findLength(grid, i, j-1, distance+1)