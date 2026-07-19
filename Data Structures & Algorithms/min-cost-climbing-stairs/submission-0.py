class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = cost[0]
        step2 = cost[1]

        for i in range(2,len(cost)):
            mincost = min(cost[i] + step1, cost[i] + step2)
            
            temp = step2
            step2 = mincost
            step1 = temp
        
        return min(step1, step2)