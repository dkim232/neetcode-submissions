class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort() #arr now in lowest position first order

        timeTaken = []
        for pos, spd in arr:
            timeTaken.append((target - pos) / spd)
        
        numFleets = 0
        while timeTaken:
            frontCarTimeTaken = timeTaken.pop()
            while timeTaken and timeTaken[-1] <= frontCarTimeTaken:
                timeTaken.pop()
            numFleets += 1
        
        return numFleets
