from sys import stdin


def wavePrint(mat, nRows, mCols):
    currow=0
    for col in range(mCols):
        if currow==nRows-1:
            for currow in range(currow,-1,-1):
                print(mat[currow][col],end=' ')
        else:
            for currow in range(nRows):
                print(mat[currow][col], end=' ')


# Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1