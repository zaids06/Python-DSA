from math import *
from collections import *
from sys import *
from os import *
def geometric(k):
    if k==0:
        return 1
    return 1/(2**k)+geometric(k-1)

k=int(input())
# use the following inplace of setprecision method
print("{:.{}f}".format(geometric(k), 5))