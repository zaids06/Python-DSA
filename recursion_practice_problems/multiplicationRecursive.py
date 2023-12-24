from math import *
from collections import *
from sys import *
from os import *

def Multiplication(m,n):
    if n==0:
        return 0
    if n==1:
        return m
    return m+Multiplication(m,n-1)
setrecursionlimit(10**6)
m=int(input())
n=int(input())
print(Multiplication(m,n))