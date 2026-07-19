class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        rottenDQ = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    rottenDQ.append((i,j))

        ##decrement numFresh if fresh infested
        minutes = 0
        while rottenDQ and numFresh != 0:
            minutes += 1
            numRotten = len(rottenDQ)

            for index in range(numRotten):
                i,j = rottenDQ.popleft() #(i,j) location of current rotten apple

                if (i+1 < len(grid)) and grid[i+1][j] == 1:## fresh found up
                    rottenDQ.append((i+1,j)) #add location for dfs
                    grid[i+1][j] = 2 #make it rotten
                    numFresh -= 1
                if (i-1 >= 0) and grid[i-1][j] == 1:## fresh found down
                    rottenDQ.append((i-1,j))
                    grid[i-1][j] = 2
                    numFresh -= 1
                if (j+1 < len(grid[0])) and grid[i][j+1] == 1:## fresh found right
                    rottenDQ.append((i,j+1))
                    grid[i][j+1] = 2
                    numFresh -= 1
                if (j-1 >= 0) and grid[i][j-1] == 1:## fresh found left
                    rottenDQ.append((i,j-1))
                    grid[i][j-1] = 2
                    numFresh -= 1

        if numFresh != 0:
            return -1
        else:
            return minutes       