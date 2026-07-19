class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        



        #dijkstras: 4 things (minus graph, bc. we can just search the grid)
        seen = set()
        minheap = []
        #no dist, as stop condition is if we reach bottom right

        heapq.heappush(minheap, (grid[0][0], (0,0)))

        while minheap:
            curPathMax, curIndex = heapq.heappop(minheap)
            if (curIndex in seen) or (curIndex[0] < 0) or (curIndex[0] >= len(grid)) or (curIndex[1] < 0) or (curIndex[1] >= len(grid[0])):#out of range
                continue
            
            i = curIndex[0]
            j = curIndex[1]
            seen.add(curIndex)
            curPathMax = max(curPathMax, grid[i][j])

            if curIndex == (len(grid)-1, len(grid[0])-1): #reached bottom right
                return curPathMax
            #check neighbors
            heapq.heappush(minheap, (curPathMax, (i+1,j)))
            heapq.heappush(minheap, (curPathMax, (i-1,j)))
            heapq.heappush(minheap, (curPathMax, (i,j+1)))
            heapq.heappush(minheap, (curPathMax, (i,j-1)))