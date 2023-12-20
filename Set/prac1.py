from os import *
from sys import *
from collections import *
from math import *


def print_pattern(arr, n, m):
    temp=n
    for i in range(temp,0,-1):
        for j in range (0,i):
            k=n-temp
            for k in arr :
                print (k)



n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

print_pattern(arr, n, m)