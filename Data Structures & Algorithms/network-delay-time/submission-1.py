class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distFromN = [float('inf') for _ in range(n+1)]
        seen = set()
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((time, target))

        nextNode = []#min-heap
        heapq.heappush(nextNode, (0, k))
        distFromN[k] = 0

        #start:
        while nextNode:#while neighbors exist
            curDist, curNode = heapq.heappop(nextNode) #get smallest distance node from minheap
            
            if curNode in seen:
                continue
            seen.add(curNode)

            for time, target in graph[curNode]:
                distFromN[target] = min(distFromN[target], curDist + time)
                heapq.heappush(nextNode, (distFromN[target], target))
        
        maxVal = max(distFromN[1:])
        if maxVal == float('inf'):
            return -1
        else:
            return maxVal