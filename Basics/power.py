#operator solution
# def power(x, n):
#     return x**n


#recursive solution
# def power(x, n):
#     if n==0:
#         return 1
#     return x*power(x, n-1)


#iterative solution
def power(x, n):
    ans=1
    for i in range(n):
        ans=ans*x
    return ans

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
