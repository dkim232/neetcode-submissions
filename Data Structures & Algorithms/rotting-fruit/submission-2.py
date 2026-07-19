class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        rotten = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        totalMins = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while rotten and numFresh > 0:
            totalMins += 1
            numRotten = len(rotten)

            for i in range(numRotten): #iterate through the rotten 
                i_rotten, j_rotten = rotten.popleft()

                for dr, dc in directions:
                    newI = i_rotten + dr
                    newJ = j_rotten + dc
                    if (newI < 0) or (newI >= len(grid)) or (newJ < 0) or (newJ >= len(grid[0])) or (grid[newI][newJ] != 1):
                        #not within grid or not fresh,
                        continue
                    #else, valid index AND is fresh banana
                    else:
                        rotten.append((newI, newJ))
                        grid[newI][newJ] = 2
                        numFresh -= 1
            
        if numFresh > 0:#didnt clear all
            return -1
        else:
            return totalMins
