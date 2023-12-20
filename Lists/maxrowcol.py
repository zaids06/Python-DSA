'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    rowhigh=-2147483648
    rowind=-1
    for row in range(nRows):
        sumrow=0
        for col in range(mCols):
            sumrow+=arr[row][col]
        if sumrow>rowhigh:
            rowhigh=sumrow
            rowind=row
    colHigh=-2147483648
    colind=-1
    for col in range(mCols):
        sumcol=0
        for row in range(nRows):
            sumcol+=arr[row][col]
        if sumcol>colHigh:
            colHigh=sumcol
            colind=col
    if rowhigh>colHigh:
        print("row "+str(rowind) + " " + str(rowhigh))
    else:
        print("column "+str(colind) + " " + str(colHigh))
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
    findLargest(mat, nRows, mCols)

    t -= 1