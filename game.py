import random

# -- Display the board
#    Given a board (a 4x4 grid of integers) print out the board
#    state in a nice format. Values of zero are shown as blanks.
def show_board(board):
    print('_____________________________')
    for row in range(0,4):
        print('|      |      |      |      |')
        for col in range(0,4):
            val = board[row][col]
            if val > 0:
                print('| {:4d} '.format(val), end='')
            else:
                print('|      ', end='')
        print('|')
        print('|______|______|______|______|')

# -- Add a random tile
#    Pick an empty square at random and placing a tile with value of
#    either 2 (with 90% probability) or 4 (10% probability)
def add_tile(board):
    # -- Figure out whether we are adding 2 or 4
    r = random.random() * 100
    if r <= 10:
        new_tile = 4
    else:
        new_tile = 2
    # -- Try random spaces until we find an empty one
    added = False
    while not added:
        row = int(random.random() * 4)
        col = int(random.random() * 4)
        if board[row][col] == 0:
            board[row][col] = new_tile
            added = True
    return

# -- Swap two tiles
#    This is a simple function that swaps the values of two tiles.
#    We can use this function to move a tile from one position to
#    another by passing the coordinates of a tile for the "from"
#    position, and the coordinates of an empty square for the
#    "to" position.
def swap_tiles(board, from_row, from_col, to_row, to_col):
    return

# -- Merge two tiles
#    This function combines two tiles. It *assumes* that the two
#    given positions contain tiles with the same value, and that
#    they are adjacent (in some direction), so you don't need to
#    check these preconditions. The "from" position should end
#    up empty (zero), and the "to" position should hold a tile
#    with the new value (twice the original value).
def merge_tiles(board, from_row, from_col, to_row, to_col):
    return

# ----- Direction-specific functions -----------------------------
#
#  The three functions below need to be implemented separately for
#  each of the possible directions: left, right, up, and down. I am
#  showing only the versions for "left" here; you should create
#  a set of three functions with the same interface for the other
#  three directions.

# -- Compact one row to the left
#    This function is perhaps the trickiest to get right. Given a
#    board and a specific row (an integer index), this function
#    should move all of the non-zero tiles as far as they can go
#    to the left (towards lower indexes).
#    For example, given the following arguments:
#      board = [[0,0,0,0],[0,2,0,2],[4,4,2,0],[0,0,0,0]]
#      row = 1
#    it should compact only row 1 (the second row) resulting in
#      board = [[0,0,0,0],[2,2,0,0],[4,4,2,0],[0,0,0,0]]
#
#    Use the swap_tiles function to move tiles as necessary. Note
#    that it does not need to combine any tiles. It does not return
#    anything, since the board is modified "in place".
def compact_row_left(board, row):
    return

# -- Merge row left
#    This is the second tricky function in the program. It looks
#    at adjacent pairs of tiles in the given row and merges them
#    together if they have the same value. It returns any points
#    earned. Note that we will always run this function *after*
#    calling compact, so tiles that can be merged will always be
#    next to each other. Also note that you do not need to worry
#    about any empty spaces left behind -- we will just call
#    compact again to remove them. So, for example, given the
#    following arguments:
#      board = [[0,0,0,0],[0,2,0,2],[4,4,2,0],[0,0,0,0]]
#      row = 2
#    it should compact only row 2 (the third row) resulting in
#      board = [[0,0,0,0],[0,2,2,0],[8,0,2,0],[0,0,0,0]]
#    and return the value 4
#    Note that merging a row can cause up to two pairs of tiles
#    to merge, but not more.
def merge_row_left(board, row):
    points = 0
    return points

# -- Slide row left
#    This function combines the two functions above to perform a
#    complete "go left" operation for one row. It should first
#    compact the row, to get all the tiles to one side, then merge
#    adjacent tiles with the same value (if any), then compact the
#    row again, to remove any spaces left behind. It should return
#    the number of points
def slide_row_left(board, row):
    points = 0
    return points

# -- Slide left
#    This function simply calls slide_row_left for each row index
#    on the board. It should keep track of the total number
#    of points earned (if any) from the merging of the four rows
#    and return that value.
def slide_left(board):
    return 0

# ----- End of game functions ------------------------------------

# -- Is board full?
#    Return true if all of the tiles are non-zero
def is_board_full(board):
    return False

# -- Are there no moves?
#    Return true if there are no moves that would merge tiles.
def are_no_moves(board):
    return False

# ----- Main game function  --------------------------------------
# -- Play 2048
#    This function initializes the board, and then asks the user
#    repeatedly for directions, slides the tiles, and keeps track
#    of the score.
def play2048():
    b = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
    add_tile(b)
    add_tile(b)
    show_board(b)

    score = 0
    done = False
    while not done:
        m = input('Enter move (w=up, z=down, a=left, s=right): ')

        if m == 'a':
            x = slide_left(b)
        if m == 'q':
            break

        add_tile(b)
        score = score + x
        show_board(b)
        print('Score is {}'.format(score))

    print('Thanks for playing!')

# ----- Start of the program -------------------------------------
#  The whole program consists of calling the play2048 function
#  For unit testing, comment out this function call and add code
#  to create test boards, call functions, and print the results.
play2048()
