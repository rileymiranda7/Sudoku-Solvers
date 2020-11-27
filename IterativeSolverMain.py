# Program for solving a Sudoku board iteratively
__author__ = "Riley Miranda"
from Blank import Blank

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

# the unsolved, current board
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
# returns the numbers in the whole row that aren't zero for the purpose of seeing what we can't put in blank square
# in that row
def getNumInRow(currRow):
    numInRow = []
    for j in range(len(currRow)):
        if currRow[j] != 0:
            numInRow.append(currRow[j])
    return numInRow


# returns the numbers in the whole column that aren't zero for the purpose of seeing what we can't put in blank square
# in that column
def getNumInCol(currBoard, j):
    numInCol = []
    # i is which row we are in; j is fixed position of each row to get column numbers
    for i in range(len(currBoard)):
        if currBoard[i][j] != 0:
            numInCol.append(currBoard[i][j])
    return numInCol

#returns numbers in square that aren't zero
def getNumInSquare(currBoard, i, j):
    numInSquare = []
    #each if elif block represents the square we could be in from 1 (top left corner) to 9 (bottom right corner)
    if 0 <= i <= 2 and 0 <= j <= 2: # square 1 (upper left corner)
        numInSquare += currBoard[0][0:3]
        numInSquare = numInSquare + currBoard[1][0:3]
        numInSquare += currBoard[2][0:3]
    elif 0 <= i <= 2 and 3 <= j <= 5: # square 2 (upper middle)
        numInSquare += currBoard[0][3:6]
        numInSquare = numInSquare + currBoard[1][3:6]
        numInSquare += currBoard[2][3:6]
    elif 0 <= i <= 2 and 6 <= j <= 8: # square 3 (upper right corner)
        numInSquare += currBoard[0][6:9]
        numInSquare = numInSquare + currBoard[1][6:9]
        numInSquare += currBoard[2][6:9]
    # row 2
    elif 3 <= i <= 5 and 0 <= j <= 2: # square 4 (left middle row)
        numInSquare += currBoard[3][0:3]
        numInSquare = numInSquare + currBoard[4][0:3]
        numInSquare += currBoard[5][0:3]
    elif 3 <= i <= 5 and 3 <= j <= 5: # square 5 (middle middle row)
        numInSquare += currBoard[3][3:6]
        numInSquare = numInSquare + currBoard[4][3:6]
        numInSquare += currBoard[5][3:6]
    elif 3 <= i <= 5 and 6 <= j <= 8: # square 6 (right middle row)
        numInSquare += currBoard[3][6:9]
        numInSquare = numInSquare + currBoard[4][6:9]
        numInSquare += currBoard[5][6:9]
    # row 3
    elif 6 <= i <= 8 and 0 <= j <= 2: # square 7 (bottom left corner)
        numInSquare += currBoard[6][0:3]
        numInSquare = numInSquare + currBoard[7][0:3]
        numInSquare += currBoard[8][0:3]
    elif 6 <= i <= 8 and 3 <= j <= 5: # square 8 (middle bottom row)
        numInSquare += currBoard[6][3:6]
        numInSquare = numInSquare + currBoard[7][3:6]
        numInSquare += currBoard[8][3:6]
    elif 6 <= i <= 8 and 6 <= j <= 8: # square 9 (bottom right corner)
        numInSquare += currBoard[6][6:9]
        numInSquare = numInSquare + currBoard[7][6:9]
        numInSquare += currBoard[8][6:9]


    # clears zeros
    atLastEle = False
    k = 0
    while (not(atLastEle)):
        if k > (len(numInSquare) - 1):
            break
            atLastEle = True
        if numInSquare[k] == 0:
            del numInSquare[k]
            k -= 1
        k += 1
    return numInSquare



# returns set of numbers (1-9) that are available to be placed in that blank (don't conflict with row, col, or square)
def getNumsThatWork(numInRow, numInCol, numInSquare):
    totalNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numsThatWork = []
    numsThatDontWork =[]
    for i in range(len(numInRow)):
        if numInRow[i] != 0:
            numsThatDontWork.append(numInRow[i])
    for j in range(len(numInCol)):
        if numInCol[j] != 0 and not(numInCol[j] in numsThatDontWork): # will not add numbers already in list
            numsThatDontWork.append(numInCol[j])
    for k in range(len(numInSquare)):
        if numInSquare[k] != 0 and not(numInSquare[k] in numsThatDontWork):
            numsThatDontWork.append(numInSquare[k])
    # subtract numsThatDontWork from numsThatWork: need to use larger sized list for iterating
    if len(totalNums) >= len(numsThatDontWork):
        largerLen = len(totalNums)
    else:
        largerLen = len(numsThatDontWork)
    for h in range(largerLen):
        if not(totalNums[h] in numsThatDontWork):
            numsThatWork.append(totalNums[h])
    return numsThatWork


def sudokuSolver(currBoard):
    # create list of Blank objects and index
    blanksList = []
    BListI = -1

    # index for nested while loops
    row = 0
    col = 0

    # boolean for backtracking
    back = False

    while row < 9:
        while col < 9:
            print("row: ", row)
            print("col", col)
            # if program comes across a blank square
            if currBoard[row][col] == 0:
                if not back:
                    # get lists of current nonzero numbers in the whole row and whole column
                    numInRow = getNumInRow(currBoard[row])
                    numInCol = getNumInCol(currBoard, col)
                    numInSquare = getNumInSquare(currBoard, row, col)

                    # use prev lists to come up with list of numbers we can place in blank
                    numsThatWork = getNumsThatWork(numInRow, numInCol, numInSquare)
                    print("numsThatWork: ", numsThatWork)

                    # create new Blank object with numsThatWork and append to list
                    blanksList.append(Blank(numsThatWork))
                    BListI += 1
                    print("BListI: ", BListI)

                #  assign row and col to Blank object
                blanksList[BListI].row = row
                blanksList[BListI].col = col

                # if there are no numbers that work for the blank we picked the wrong number somewhere and need to
                # back track
                if len(blanksList[BListI].numsThatWork) == 0:
                    # keep backtracking until we find blank position with more than option in numsThatWork
                    numsThatWorkIsEmpty = True
                    while numsThatWorkIsEmpty:
                        # set row and col back to last blank location as long as we are not on first blank
                        if BListI != 0:
                            row = blanksList[BListI - 1].row
                            col = blanksList[BListI - 1].col
                            print("prev blank loc: ", row, " ", col)
                        # set previous Blank object's value to 0
                        currBoard[row][col] = 0

                        # delete the last blank's first number that works so next number in list is tried
                        if BListI == 0:
                            print("numsThatWork length: ", len(blanksList[BListI].numsThatWork))
                            del blanksList[BListI].numsThatWork[0]
                        else:
                            del blanksList[BListI - 1].numsThatWork[0]

                        # delete current Blank object
                        if BListI != 0:
                            del blanksList[BListI]
                        # go into backtracking mode for previous Blank object
                        back = True
                        BListI -= 1

                        # end loop if current blank has a new path to solve board (still has value in numsThatWork after
                        # deleting a value
                        if len(blanksList[BListI].numsThatWork) != 0:
                            numsThatWorkIsEmpty = False
                            print("not empty")
                else:
                    if back:
                        back = False

                    # set blank to first value in numsThatWork
                    currBoard[row][col] = blanksList[BListI].numsThatWork[0]
                    print("at ", row, ",", col, " value: ", currBoard[row][col], "\n")

                    # increment row and col
                    if col == 8:
                        row += 1
                        col = 0
                    else:
                        col += 1
            # else location is not blank
            else:
                if col == 8:
                    row += 1
                    col = 0
                else:
                    col += 1
            # break loop at last location on board (bottom right) because we need col 8 to shift to next row
            # so col never reaches 9 and while col < 9 never returns false
            if row == 9 and col == 0:
                break


# print unsolved board
print("Unsolved board:")
for row in currBoard:
    print(row)

sudokuSolver(currBoard)
# print expected solved board and returned solved board
print("Expected solved board:\t\t   Returned Solved Board:")
for row in range(9):
    print(solvedBoard[row], "  ", currBoard[row])
