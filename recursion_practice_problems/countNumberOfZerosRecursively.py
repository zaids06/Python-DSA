from math import *
from collections import *
from sys import *
from os import *
def countNumberOfZeros(n):
    if n<=9 and n!=0:
        return 0
    elif n<=9 and n==0:
        return 1
    elif n%10==0 and n!=0:
        return 1+countNumberOfZeros(n//10)
    else:
        return 0+countNumberOfZeros(n//10)
l=int(input())
print(countNumberOfZeros(l))