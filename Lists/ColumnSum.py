li=[[1,2,3,5],
    [4,5,6,55],
    [7,555,9,12]]
n=len(li)
m=len(li[0])
maxSum=0
maxind=-1
for i in range(m):
    locsum=0
    for j in range(n):
        locsum+=li[j][i]
    if locsum>maxSum:
        maxSum=locsum
        maxind=i
print(maxSum,maxind)