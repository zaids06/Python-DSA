# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456
n=int(input())
i=1
while(i<=n):
    print(' '*(i-1),end='')
    j=i
    while(j<=n):
        print(j,end='')
        j+=1
    print()
    i+=1
i=1
while(i<n):
    print(' '*(n-i-1),end='')
    j=n-i
    while(j<=n):
        print(j,end='')
        j+=1
    print()
    i+=1