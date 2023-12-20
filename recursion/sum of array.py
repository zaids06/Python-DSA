def sumArray(arr):
    length = len(arr)
    if length == 1:
        return arr[0]
    return arr[length-1] + sumArray(arr[0:length-1])

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
