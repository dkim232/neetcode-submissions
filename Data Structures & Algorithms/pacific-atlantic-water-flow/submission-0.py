class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        canReachAtlantic = set()
        canReachPacific = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i == 0) or (j == 0):
                    self.intoOcean(heights,i,j,canReachPacific, -1)
                if (i == len(heights)-1) or (j == len(heights[0])-1):
                    self.intoOcean(heights,i,j, canReachAtlantic, -1)
                
        for cell in canReachAtlantic:
            if cell in canReachPacific:
                res.append(list(cell))
        
        return res

                

    def intoOcean(self, grid, i, j, curSet, prevHeight): #i = row num, j = col num; 
        ##base case: out of bounds, already in set, or height < prevHeight:
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) or ((i,j) in curSet) or (grid[i][j] < prevHeight):
            return
        
        ##valid grid[i][j]; continue recursion
        curSet.add((i,j))
        curVal = grid[i][j]
        self.intoOcean(grid,i+1,j,curSet, curVal)
        self.intoOcean(grid,i-1,j,curSet, curVal)
        self.intoOcean(grid,i,j+1,curSet, curVal)
        self.intoOcean(grid,i,j-1,curSet, curVal)

