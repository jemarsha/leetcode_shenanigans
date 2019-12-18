#solve sudoku later
import numpy as np


def sudoku_no_box(nums,valid_chars):

    rows= [False for i in nums for j in i if j not in valid_chars]

    flipped = np.array(nums).T

    columns = [False for i in flipped for j in i if j not in valid_chars]

    #for i in nums:
        #for j in i:
            #if j not in valid_chars:

    #print(m)            #return False

    if False in rows or False in columns:
        return False
    #for
    return True


def notInRow(arr, row):
    # Set to store characters seen so far.
    st = set()

    for i in range(0, len(arr)-1):

        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False

        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])

    return True


# Checks whether there is any
# duplicate in current column or not.
def notInCol(arr, col):
    st = set()

    for i in range(0, len(arr)-1):

        # If already encountered before,
        # return false
        if arr[i][col] in st:
            return False

        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            st.add(arr[i][col])

    return True


# Checks whether there is any duplicate
# in current 3x3 box or not.
def notInBox(arr, startRow, startCol):
    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]

            # If already encountered before,
            # return false
            if curr in st:
                return False

            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                st.add(curr)

    return True


# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(arr, row, col):
    #print(row - row % 3)
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))



def isValidConfig(arr, n):
    for i in range(0, n):
        for j in range(0, n):

            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(arr, i, j):
                return False

    return True



if __name__ == '__main__':
    t = [[1, 2, 8, 3, 4, 5],
         [4, 5, 2, 9, 8, 1],
         [3, '-', 5, 1, 2, 6]]

    valid_chars = set([1, 2, 3, 4, 5, 6, 7, 8, 9, '.'])

    print(sudoku_no_box(t,valid_chars))

    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    if isValidConfig(board, 9):
        print("YES")
    else:
        print("NO")

