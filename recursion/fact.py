import sys
sys.setrecursionlimit(3000)
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

print(fact(1950))
ef=4
