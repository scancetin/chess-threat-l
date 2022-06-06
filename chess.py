from piece import Piece
from enums import Chess

# Get the scores for white and black side
def calc_points(board):
    w_p = 0
    b_p = 0

    # i for row, j for column
    for i in range(8):
        for j in range(8):
            # Find if it is piece
            if board[i][j] != Chess.EMPTY:
                point = piece_points(board[i][j])
                piece = Piece(board[i][j],i,j,point)

                # Find the side of this piece for total score
                if board[i][j][1] == Chess.WHITE:
                    w_p += piece.get_point(board)
                elif board[i][j][1] == Chess.BLACK:
                    b_p += piece.get_point(board)
    return w_p, b_p

# Get the point of the piece
def piece_points(name):
    if name[0] == Chess.PIECES[0]:
        return Chess.POINTS[0]    
    elif name[0] == Chess.PIECES[1]:
        return Chess.POINTS[1]
    elif name[0] == Chess.PIECES[2]:
        return Chess.POINTS[2]
    elif name[0] == Chess.PIECES[3]:
        return Chess.POINTS[3]
    elif name[0] == Chess.PIECES[4]:
        return Chess.POINTS[4]
    elif name[0] == Chess.PIECES[5]:
        return Chess.POINTS[5]
    else:
        return 0

if __name__=="__main__":
    # Read file and split pieces
    f = open("board3.txt", "r")
    pieces = f.read().split()
    
    # Get 2D array to represent the chess board
    board = [pieces[i:i+8] for i in range(0, len(pieces), 8)]

    # Get the scores for white and black side
    white_point, black_point = calc_points(board)
    print(f"Black: {black_point}")
    print(f"White: {white_point}")
