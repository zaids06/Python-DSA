#   *
#  ***
# *****
#  ***
#   *



n=int(input())
u=n//2+1
l=n//2
i=1
while(i<=u):
    print(" "*(u-i),end="")
    print("*"*(i*2-1),end="")
    print()
    i+=1
i=l
while(i>0):
    print(" "*(u-i),end="")
    print("*"*(i*2-1),end="")
    print()
    i-=1
