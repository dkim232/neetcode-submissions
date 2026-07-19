class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []

        for num in nums:
            heapq.heappush(maxheap, -1*num)
        
        for i in range(k-1):
            heapq.heappop(maxheap)
        
        return -1*heapq.heappop(maxheap)