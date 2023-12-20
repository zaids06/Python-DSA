li=[[1,2,3,5],
    [4,5,6,55],
    [7,555,9,12]]
n=len(li)
m=len(li[0])
for i in range(n):
    for ele in li:
        print(ele[i],end=" ")
    print()