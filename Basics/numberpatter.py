# 1                         1
# 12                       21
# 123                     321
# 1234                   4321
# 12345                 54321


n=(int(input()))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j,end="")
        j+=1
    print(" "*((n-i)*2),end='')
    j=i
    while(j>0):
        print(j,end='')
        j-=1
    print()
    i+=1