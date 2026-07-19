class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(minheap, (distance, [x,y]))
        
        numpoints = len(points)
        for i in range(k):
            res.append((heapq.heappop(minheap))[1])
        return res