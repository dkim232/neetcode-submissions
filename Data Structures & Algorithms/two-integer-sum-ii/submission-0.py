class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while (left != right):
            sumval = numbers[left] + numbers[right]

            if sumval < target:
                left += 1
                continue
            
            elif sumval > target:
                right -= 1
                continue
            
            return [left+1, right+1]
        
        return []