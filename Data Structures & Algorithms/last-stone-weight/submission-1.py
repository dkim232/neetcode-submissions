class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for val in stones:
            heapq.heappush(maxheap, -val) #maxheap
        
        numvals = len(stones)

        while len(maxheap) > 1:
            temp1 = heapq.heappop(maxheap) #largest value
            temp2 = heapq.heappop(maxheap) #2nd largest value
            if temp1 < temp2:
                heapq.heappush(maxheap, temp1 - temp2)
        
        if not maxheap:
            return 0
        else:
            return -maxheap[0]