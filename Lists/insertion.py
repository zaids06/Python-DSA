arr=[33,22,11,4,23,1,0]
min=0
for i in range(1,len(arr)):
    j=i-1
    ele=arr[i]
    while j>=0 and ele<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=ele
print(arr)
