class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            count = 0
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    count += 1
                    seen.add(board[i][j])
            
            if len(seen) != count:
                return False
        for j in range(9):
            count = 0
            seen = set()
            for i in range(9):
                if board[i][j] != ".":
                    count += 1
                    seen.add(board[i][j])
            if len(seen) != count:
                return False
        
        set1 = set()
        set2 = set()
        set3 = set()
        set4 = set()
        set5 = set()
        set6 = set()
        set7 = set()
        set8 = set()
        set9 = set()

        count = 0
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue


                if i <= 2:
                    if j <= 2:
                        set1.add(val)
                    elif j <= 5:
                        set2.add(val)
                    elif j <= 8:
                        set3.add(val)
                
                elif i <= 5:
                    if j <= 2:
                        set4.add(val)
                    elif j <= 5:
                        set5.add(val)
                    elif j <= 8:
                        set6.add(val)
                    
                elif i <= 8:
                    if j <= 2:
                        set7.add(val)
                    elif j <= 5:
                        set8.add(val)
                    elif j <= 8:
                        set9.add(val)
                
                count += 1
        if len(set1) + len(set2) + len(set3) + len(set4) + len(set5) + len(set6) + len(set7) + len(set8) + len(set9) != count:
            return False
        
        return True



        

      









