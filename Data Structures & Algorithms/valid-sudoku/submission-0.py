class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for arr in board:
            seen = set()
            for i in arr:
                if  i != '.' and i in seen:
                    return False
                else:
                    seen.add(i)
            
        for i in range(9):
            seen = set()
            for j in range(9):

                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
                
        for i in range(0, 9 , 3):
            for j in range(0,9,3):
                seen = set()
                for row in range(3):
                    for col in range(3):

                        if board[i+row][j+col] != '.' and board[i+row][j+col] in seen:
                            return False
                        else:
                            seen.add(board[i+row][j+col])

        return True
