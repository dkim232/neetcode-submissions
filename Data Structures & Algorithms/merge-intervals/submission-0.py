class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        sortedIntervals = sorted(intervals)
        res = list()

        for index, interval in enumerate(sortedIntervals):
            if index == 0:
                res.append(interval)
                continue
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
                continue
            
            res.append(interval)
        
        return res