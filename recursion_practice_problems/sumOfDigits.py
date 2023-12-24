from math import *
from collections import *
import sys
from os import *

def sumOfDigits(string):
    length=len(string)
    if length==1:
        return int(string)
    return int(string[0])+sumOfDigits(string[1:length])


sys.setrecursionlimit(3000)
l=input()
print(sumOfDigits(l))