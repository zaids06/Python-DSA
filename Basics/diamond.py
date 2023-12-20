#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n=int(input())
u=n//2+1
l=n//2
i=1
while(i<=u):
    print(" "*(u-i),end="")
    print("*"*i,end='')
    print('*'*(i-1),end='')
    print()
    i+=1
i=1
while(i<=l):
    print(" "*(i),end="")
    print("*"*(u-i),end='')
    print('*'*(l-i),end='')
    print()
    i+=1

