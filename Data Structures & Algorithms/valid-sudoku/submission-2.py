class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                val = board[row][col]

                if (val in rows[row]) or (val in cols[col]) or (val in squares[(row//3, col//3)]):
                    return False
                
                cols[col].add(val)
                rows[row].add(val)
                squares[(row//3, col//3)].add(val)
        
        return True