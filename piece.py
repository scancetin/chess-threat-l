from enums import Chess

class Piece:
    # Initialize the piece
    def __init__(self, name, row_no, col_no, point):
        self.name = name
        self.row_no = row_no
        self.col_no = col_no
        self.point = point

    # Get the name value
    def get_name(self):
        return self.name

    # Get the row
    def get_row_no(self):
        return self.row_no

    # Get the column
    def get_col_no(self):
        return self.col_no

    # Get the calculated point
    def get_point(self, board):
        return self.point / 2 if self.is_threatened(board) else self.point

    # Find if the piece is threatened horizontal of vertical
    def is_threatened_hor_ver(self, board):
        i = self.get_row_no()
        j = self.get_col_no()

        # Left of the Piece
        for k in range(j, 0, -1):
            if board[i][k-1] == Chess.EMPTY:
                continue
            elif board[i][k-1][1] == board[i][j][1] or board[i][k-1][0] != Chess.PIECES[3] and board[i][k-1][0] != Chess.PIECES[4]:
                break
            elif board[i][k-1][0] == Chess.PIECES[3] or board[i][k-1][0] == Chess.PIECES[4]:
                return True

        # Right of the Piece
        for k in range(j, 7):
            if board[i][k+1] == Chess.EMPTY:
                continue
            elif board[i][k+1][1] == board[i][j][1] or board[i][k+1][0] != Chess.PIECES[3] and board[i][k+1][0] != Chess.PIECES[4]:
                break
            elif board[i][k+1][0] == Chess.PIECES[3] or board[i][k+1][0] == Chess.PIECES[4]:
                return True

        # Above the Piece
        for k in range(i, 0, -1):
            if board[k-1][j] == Chess.EMPTY:
                continue
            elif board[k-1][j][1] == board[i][j][1] or board[k-1][j][0] != Chess.PIECES[3] and board[k-1][j][0] != Chess.PIECES[4]:
                break
            elif board[k-1][j][0] == Chess.PIECES[3] or board[k-1][j][0] == Chess.PIECES[4]:
                return True

        # Below the Piece
        for k in range(i, 7):
            if board[k+1][j] == Chess.EMPTY:
                continue
            elif board[k+1][j][1] == board[i][j][1] or board[k+1][j][0] != Chess.PIECES[3] and board[k+1][j][0] != Chess.PIECES[4]:
                break
            elif board[k+1][j][0] == Chess.PIECES[3] or board[k+1][j][0] == Chess.PIECES[4]:
                return True

    # Find if the piece is threatened diagonal 
    def is_threatened_diagonal(self, board):
        i = self.get_row_no()
        j = self.get_col_no()

        # Left up of the Piece
        for k in range(1, min(i,j)+1):
            if board[i-k][j-k] == Chess.EMPTY:
                continue
            elif board[i-k][j-k][1] == board[i][j][1] or board[i-k][j-k][0] != Chess.PIECES[2] and board[i-k][j-k][0] != Chess.PIECES[4]:
                break
            elif board[i-k][j-k][0] == Chess.PIECES[2] or board[i-k][j-k][0] == Chess.PIECES[4]:
                return True

        # Right up of the Piece
        for k in range(1, min(i, 7-j)+1):
            if board[i-k][j+k] == Chess.EMPTY:
                continue
            elif board[i-k][j+k][1] == board[i][j][1] or board[i-k][j+k][0] != Chess.PIECES[2] and board[i-k][j+k][0] != Chess.PIECES[4]:
                break
            elif board[i-k][j+k][0] == Chess.PIECES[2] or board[i-k][j+k][0] == Chess.PIECES[4]:
                return True

        # Left down of the Piece
        for k in range(1, min(7-i, j)+1):
            if board[i+k][j-k] == Chess.EMPTY:
                continue
            elif board[i+k][j-k][1] == board[i][j][1] or board[i+k][j-k][0] != Chess.PIECES[2] and board[i+k][j-k][0] != Chess.PIECES[4]:
                break
            elif board[i+k][j-k][0] == Chess.PIECES[2] or board[i+k][j-k][0] == Chess.PIECES[4]:
                return True

        # Right down of the Piece
        for k in range(1, min(7-i,7-j)+1):
            if board[i+k][j+k] == Chess.EMPTY:
                continue
            elif board[i+k][j+k][1] == board[i][j][1] or board[i+k][j+k][0] != Chess.PIECES[2] and board[i+k][j+k][0] != Chess.PIECES[4]:
                break
            elif board[i+k][j+k][0] == Chess.PIECES[2] or board[i+k][j+k][0] == Chess.PIECES[4]:
                return True
    
    # Find if the piece is threatened by pawn
    def is_threatened_by_pawn(self, board):
        i = self.get_row_no()
        j = self.get_col_no()

        color = self.get_name()[1]

        # If piece is black
        if color == Chess.BLACK and i < 7:
            if j == 0 and board[i+1][j+1] == Chess.WHITE_PAWN:
                return True
            elif j == 7 and board[i+1][j-1] == Chess.WHITE_PAWN:
                return True
            elif j > 0 and j < 7:
                if board[i+1][j+1] == Chess.WHITE_PAWN or board[i+1][j-1] == Chess.WHITE_PAWN:
                    return True

        # If piece is white
        if color == Chess.WHITE and i > 0:
            if j == 0 and board[i-1][j+1] == Chess.BLACK_PAWN:
                return True
            elif j == 7 and board[i-1][j-1] == Chess.BLACK_PAWN:
                return True
            elif j > 0 and j < 7:
                if board[i-1][j+1] == Chess.BLACK_PAWN or board[i-1][j-1] == Chess.BLACK_PAWN:
                    return True

    # Find if the piece is threatened by knigth
    def is_threatened_by_knigth(self, board):
        i = self.get_row_no()
        j = self.get_col_no()

        row_moves = Chess.KNIGTH_ROW_MOVES
        col_moves = Chess.KNIGTH_COL_MOVES
        
        for k in range(len(row_moves)):
            i_new = i+row_moves[k]
            j_new = j+col_moves[k]

            if i_new < 0 or i_new > 7 or j_new < 0 or j_new > 7:
                continue
            elif board[i_new][j_new][1] != board[i][j][1] and board[i_new][j_new][0] == Chess.PIECES[1]:
                return True

    # Find if the piece is threatened by king
    def is_threatened_by_king(self, board):
        i = self.get_row_no()
        j = self.get_col_no()

        row_moves = Chess.KING_ROW_MOVES
        col_moves = Chess.KING_COL_MOVES

        for k in range(len(row_moves)):
            i_new = i+row_moves[k]
            j_new = j+col_moves[k]

            if i_new < 0 or i_new > 7 or j_new < 0 or j_new > 7:
                continue
            elif board[i_new][j_new][1] != board[i][j][1] and board[i_new][j_new][0] == Chess.PIECES[5]:
                return True

    # Find if the piece is threatened
    def is_threatened(self, board):
        return self.is_threatened_hor_ver(board) or self.is_threatened_diagonal(board) or self.is_threatened_by_pawn(board) or self.is_threatened_by_king(board) or self.is_threatened_by_knigth(board)
