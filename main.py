# Program for solving a Sudoku board recursively
_author_ = "Riley Miranda"
# zeroes represent blank squares

solvedBoard = [
    [6, 8, 9, 3, 5, 4, 7, 1, 2],
    [7, 4, 1, 2, 8, 9, 6, 5, 3],
    [3, 5, 2, 1, 7, 6, 8, 9, 4],
    [2, 9, 7, 6, 4, 5, 1, 3, 8],
    [5, 6, 4, 8, 1, 3, 2, 7, 9],
    [1, 3, 8, 7, 9, 2, 4, 6, 5],
    [8, 2, 3, 5, 6, 7, 9, 4, 1],
    [9, 7, 5, 4, 2, 1, 3, 8, 6],
    [4, 1, 6, 9, 3, 8, 5, 2, 7],
]

# the unsolved board
currBoard = [
    [6, 0, 0, 3, 5, 4, 0, 0, 2],
    [7, 4, 0, 0, 0, 0, 0, 5, 0],
    [0, 5, 2, 1, 0, 0, 8, 0, 0],
    [0, 9, 0, 6, 0, 0, 1, 0, 8],
    [5, 0, 4, 0, 0, 0, 2, 0, 9],
    [1, 0, 8, 0, 0, 2, 0, 6, 0],
    [0, 0, 3, 0, 0, 7, 9, 4, 0],
    [0, 7, 0, 0, 0, 0, 0, 8, 6],
    [4, 0, 0, 9, 3, 8, 0, 0, 7],
]
# returns true if the number we chose is already in the row and therefore can't be used and false otherwise
def numInRow(currBoard, row, num):
    for i in range(9):
        if currBoard[row][i] == num:
            return True
    return False



# returns true if the number we chose is already in the col and therefore can't be used and false otherwise
def numInCol(currBoard, col, num):
    for i in range(9):
        if currBoard[i][col] == num:
            return True
    return False

# returns true if the number we chose is already in the 3x3 square and therefore can't be used and false otherwise
# automatically starts at top right corner of 3x3 for easy iteration
def numInSquare(currBoard, row, col, num):
    for i in range(3):
        for j in range(3):
            # iterates through 3x3 square by incrementing the col 3 times for each of the 3 rows
            if currBoard[i + row][j + col] == num:
                return True
    return False
# returns true if number chosen is not already in row, col, or 3x3
def numWorksInBlank(currBoard, row, col, num):
    #
    if not numInRow(currBoard, row, num) and not numInCol(currBoard, col, num) and not numInSquare(currBoard,
    # % row/col - row/col % 3 automatically sets up the row and col to be in the top right corner of the blank's 3x3
    # box so numInSquare can easily iterate through
    row - row % 3, col - col % 3, num):
        return True
    else:
        return False


# Finds location of blank if it exists and sets the list rowCol to that location where in rowCol [row, col]
# returns false if no blanks
def thereIsBlank(currBoard, rowCol):
    for row in range(9):
        for col in range(9):
            if currBoard[row][col] == 0:
                rowCol[0] = row
                rowCol[1] = col
                return True
    return False

def sudokuSolver(currBoard):
    # sets up blank location reference list
    rowCol = [0, 0]
    # if there is not a blank
    if not thereIsBlank(currBoard, rowCol):
        return True

    # get row and col of blank from findBlank if blank is found from rowCol reference list
    row = rowCol[0]
    col = rowCol[1]

    # try nums 1 to 9
    for num in range(1, 10): # 1 inclusive 10 exclusive
        # if none of the nums 1 through 9 work we go back to last stack and reset the spot we filled in to 0 (blank)
        # and try the next number from 1 through 9
        if numWorksInBlank(currBoard, row, col, num):

            # try assigning num
            currBoard[row][col] = num

            # recursive call
            if sudokuSolver(currBoard):
                # if board gets solved
                return True

            # board isn't solved and need to backtrack
            currBoard[row][col] = 0

    return False

# print unsolved board
print("Unsolved board:")
for row in currBoard:
    print(row)

sudokuSolver(currBoard)
# print expected solved board and returned solved board
print("Expected solved board:\t\t   Returned Solved Board:")
for row in range(9):
    print(solvedBoard[row], "  ", currBoard[row])




            








