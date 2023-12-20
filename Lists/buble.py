arr=[33,22,11,4,22,1,0]
for i in range (len(arr)):
    for j in range (1,len(arr)-i):
        if ( arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
print(arr)