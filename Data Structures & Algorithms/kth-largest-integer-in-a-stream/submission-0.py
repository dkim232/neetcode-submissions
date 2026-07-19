class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.kval = k
        for val in nums:
            heapq.heappush(self.minheap, val)

        self.numvals = len(nums)
        while self.numvals > k:
            heapq.heappop(self.minheap)
            self.numvals -= 1

                

    def add(self, val: int) -> int:
        #return the kith largest
        heapq.heappush(self.minheap, val)
        self.numvals += 1

        while self.numvals > self.kval:
            heapq.heappop(self.minheap)
            self.numvals -= 1
        
        temp = heapq.heappop(self.minheap)
        heapq.heappush(self.minheap, temp)
        return temp