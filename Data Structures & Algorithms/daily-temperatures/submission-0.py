class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stackIndex = []


        for index,temp in enumerate(temperatures):
            while stackIndex and temp > temperatures[stackIndex[-1]]:
                indexToUpdate = stackIndex.pop()
                res[indexToUpdate] = index - indexToUpdate
            
            
            stackIndex.append(index)
        
        return res