from math import *
from collections import *
from sys import *
from os import *
def lastIndex(arr,x,i):
    length = len(arr)
    if arr[i]==x:
        return i
    elif i==0:
        return -1
    return lastIndex(arr,x,i-1)
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x,n-1))