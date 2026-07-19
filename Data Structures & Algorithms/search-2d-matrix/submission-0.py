class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1. find row
        toprow = 0
        botrow = len(matrix) - 1
        while toprow <= botrow:
            midrow = (toprow + botrow) // 2
            if target >= matrix[midrow][0] and target <= matrix[midrow][-1]:#found row!
                break
            elif target < matrix[midrow][0]: #search lower
                botrow = midrow - 1
            else: #target > matrix[midrow][-1]:
                toprow = midrow + 1

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[midrow][mid] == target:
                return True
            elif matrix[midrow][mid] < target: #second half
                left = mid + 1
            else: #
                right = mid - 1
            
        return False
