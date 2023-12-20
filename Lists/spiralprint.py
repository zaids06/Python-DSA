from sys import stdin


def spiralPrint(mat, nRows, mCols):
    numOfElements = nRows * mCols
    rowLower = 0
    rowUpper = nRows - 1
    colLower = 0
    colUpper = mCols - 1
    while numOfElements > 0:
        # left->right
        if (rowLower>rowUpper):
            break
        for i in range(colLower, colUpper + 1):
            print(mat[rowLower][i],end=" ")
            numOfElements -= 1

        # top->bottom
        rowLower += 1
        if colLower>colUpper:
            break
        for row in range(rowLower, rowUpper + 1):
            print(mat[row][colUpper],end=" ")
            numOfElements -= 1
        # right->left
        colUpper -= 1
        if (rowLower>rowUpper):
            break
        for col in range(colUpper, colLower - 1,-1):
            print(mat[rowUpper][col],end=" ")
            numOfElements -= 1
        # bottom->top
        rowUpper -= 1
        if colLower>colUpper:
            break
        for row in range(rowUpper, rowLower - 1,-1):
            print(mat[row][colLower],end=" ")
            numOfElements-=1
        colLower += 1


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1