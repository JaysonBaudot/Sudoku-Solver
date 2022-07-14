board = [
    [0,1,6,0,2,0,7,8,0],
    [4,0,0,6,9,0,0,0,2],
    [2,0,0,7,0,1,0,0,3],
    [0,0,5,8,0,2,1,9,0],
    [8,6,0,0,0,0,0,2,4],
    [0,9,2,1,0,6,8,0,0],
    [1,0,0,4,0,5,0,0,7],
    [9,0,0,0,1,3,0,0,8],
    [0,5,3,0,8,0,2,4,0]
]

def solve(bo):
    print(board)
    find = find_empty(bo) # checks for empty space on the board
    if not find:          # base case for our recursion that states if there are no more empty spaces the board is solved
        return True
    else:
        row, col = find   # sets the row and column we're going to be looking at to the first available empty space
    
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i    # adds value onto board

            if solve(bo):       # recursive call to function over and over again until its solved or reaches a position that is unsolvable
                return True
            
            bo[row][col] = 0    # backtracks, empties the position, and tries againw22
    
    return False





def valid(bo, num, pos):
    # Check row 
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column 
    for i in range(len(board)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check Block
    block_x = pos[1] // 3
    block_y = pos[0] // 3

    for i in range(block_y*3, block_y*3 +3):
        for j in range (block_x*3, block_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True



def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | " , end ="")
            
            if j == 8:
                print(board[i][j])
            
            else:
                print(str(board[i][j]) + " ", end ="")
            
def find_empty(board):
    # returns first available empty space on the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None


print_board(board)
print("Solving Board...")
solve(board)
print_board(board)