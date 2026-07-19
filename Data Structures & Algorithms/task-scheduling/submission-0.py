class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        taskCounter = Counter(tasks)
        for key, freq in taskCounter.items():
            heapq.heappush(maxheap, -freq)
        
        ##queue to enforce order of processed tasks
        curtime = 0
        dq = deque()
        
        while dq or maxheap:
            if maxheap:
                curFreq = -heapq.heappop(maxheap)
                remaining_freq = curFreq - 1
                if remaining_freq > 0:
                   dq.append((remaining_freq, curtime+n))

            
            if dq:
                curDQ = dq[0] #remaining frequency
                if curtime >= curDQ[1]: ## we can process this
                    dq.popleft()
                    if curDQ[0] >= 1:
                        heapq.heappush(maxheap, -curDQ[0])
            curtime += 1
        return curtime