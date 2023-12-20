arr=[33,22,11,4,22,1,0]
for i in range (len(arr)):
    flag=True
    for j in range (1,len(arr)-i):
        if ( arr[j-1]>arr[j]):
            flag=False
            arr[j-1],arr[j]=arr[j],arr[j-1]
    if flag:
        break
print(arr)