class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(row_len,board): 
            for i in range(row_len):
                if not check_list(board[i]):
                    print('check row false',board[i])
                    return False 
            return True 


        def check_list(lis:List[str]):
            seen = set ()
            for char in lis:
                if char!=".":
                    if char in seen: 
                        print('check list false:',seen)
                        return False
                    seen.add(char)
            return True

        row_len = len(board)
        col_len = len(board[0])

        def check_box(board, start_row, start_col):
            seen = set() 
            for i in range(start_row, start_row+3):
                for j in range(start_col, start_col+3): 
                    val = board[i][j] 
                    if val !=".":
                        if val in seen: 
                            return False
                        seen.add(val)
            return True

        # create new board -> row and col switch 
        new_board = [] 
        for i in range(col_len):
            row = [] 
            for j in range(row_len):
                row.append(board[j][i])
            new_board.append(row)
        print(new_board)

        if check_row(row_len,board) and check_row(col_len,new_board):
            starting_points = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]] 
            for start_pt in starting_points: 
                if not check_box(board,start_pt[0],start_pt[1]):
                    return False 

            return True
        return False 
        
        


        