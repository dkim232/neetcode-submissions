class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)): #point 1 index
            for j in range(len(points)): #point 2 index
                if i == j:
                    continue
                # different points
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                graph[tuple(points[i])].append((distance,tuple(points[j])))
        

        seen = set()
        minheap = []
        totalDistance = 0
        heapq.heappush(minheap, (0, tuple(points[0]))) #push first point

        while minheap:
            curDist, curPoint = heapq.heappop(minheap)
            if curPoint in seen:
                continue

            totalDistance += curDist
            seen.add(tuple(curPoint))
            for nextDist, nextPoint in graph[curPoint]:#we have our neighbors now
                heapq.heappush(minheap, (nextDist, tuple(nextPoint)))
        
        return totalDistance