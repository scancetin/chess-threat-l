class Chess:
    # b for white
    # s for black
    # p for pawn
    # a for knigth
    # f for bishop
    # k for rook
    # v for queen
    # s for king

    WHITE = 'b'
    BLACK = 's'

    PIECES = ["p", "a", "f", "k", "v", "s"]
    POINTS = [1, 3, 3, 5, 9, 100]

    WHITE_PAWN = "pb"
    BLACK_PAWN = "ps"
    EMPTY = "--"

    KING_ROW_MOVES = [+1, 0, -1, 0, +1, -1, +1, -1]
    KING_COL_MOVES = [+1, 0, -1, 0, +1, -1, +1, -1]
    KNIGTH_ROW_MOVES = [-2, -2, -1, -1, +1, +1, +2, +2]
    KNIGTH_COL_MOVES = [-1, +1, -2, +2, -2, +2, -1, +1]