def checkNumber(arr, x):
    length=len(arr)
    if length==0:
        return False
    if(arr[length-1]==x):
        return True
    return (arr[:length-1],x)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
