def firstIndex(arr, x,i):
    length=len(arr)
    if length==i:
        return -1
    elif arr[i]==x:
        return i
    return firstIndex(arr,x,i+1)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))
