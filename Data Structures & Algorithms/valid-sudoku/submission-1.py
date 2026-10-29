class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        input: a 2d array str,
        output: boolean

        check there is now duplicate in each row, column and square

        create a hash set var to store unique digits for each row, column and square
        loop through the row or each inside arrays
        loop through the columns
        if the item is a dot or empty continue the column loop
        check if the item is already in row,column and square var
        if already exists in these var return false
        add the item in each var
        """
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in col[c] or 
                board[r][c] in row[r] or 
                board[r][c] in square[(r // 3, c // 3)]):
                    return False

                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r //3,c//3)].add(board[r][c])
        return True

        