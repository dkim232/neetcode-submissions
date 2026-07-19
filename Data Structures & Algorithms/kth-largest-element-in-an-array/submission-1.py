class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for val in nums:
            heapq.heappush(maxheap, -val)
        
        for i in range(k-1):
            heapq.heappop(maxheap)
        
        return -heapq.heappop(maxheap)