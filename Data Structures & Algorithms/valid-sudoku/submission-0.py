class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #function takes a 9*9 array, have to return true if there is no duplicate 
        #in side the entire row and column and in the 3*3 matrix, unless other wise False
        #all elements are strings

        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]):
                    return False
                    
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                
                square[(r // 3, c // 3)].add(board[r][c])
        return True







        