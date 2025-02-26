class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            # row set
            row_dic = {}
            # column set
            column_dic = {}
            for j in range(9):
                # evaluate row 
                if board[i][j] in row_dic and board[i][j] != '.':
                    return False
                elif board[i][j] != '.':
                    row_dic[board[i][j]]=True
                # evaluate col
                if board[j][i] in column_dic and board[j][i] != '.':
                    return False
                elif board[j][i] != '.':
                    column_dic[board[j][i]]=True
            
        def check_box(row_p, col_p, board):
            box_dic = {}
            for i in range(3):
                for j in range(3):
                    if board[row_p+i][col_p+j] in box_dic and board[row_p+i][col_p+j]!= '.':
                        return False
                    elif board[row_p+i][col_p+j] != '.':
                        box_dic[board[row_p+i][col_p+j]]=True
            return True
            
        for i in range(3):
            row_p=i*3
            for j in range(3):
                col_p=j*3
                if check_box(row_p, col_p, board) is False:
                    return False
        
        return True
