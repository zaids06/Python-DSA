#                           111*
#                           111 * *
#                           111   * * *
#                           111     * * * *
#                           111   * * *
#                           111 * *
#                           111*
n=int(input())
u=n//2+1
l=n//2
i=1
while(i<=u):
    print(' '*(i-1),end="")
    print("*"*(i),end='')
    print() 
    i+=1
i=1
while(i<=l):
    print(' '*(l-i),end="")
    print("*"*(u-i),end="")
    print() 
    i+=1