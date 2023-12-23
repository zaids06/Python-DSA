def partion(arr,start,end):
    count=0
    for i in range(start+1,end+1):
        if arr[i]<=arr[start]:
            count+=1
    if count == 0:
        return start
    pivot=start+count
    arr[start],arr[pivot]=arr[pivot],arr[start]
    i=start
    j=end
    while i<pivot and end>pivot:
        if arr[i]>arr[pivot]and arr[j]>arr[pivot]:
            j-=1
        elif arr[i]<=arr[pivot]:
            i+=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            i+=1
    return pivot
def quickSort(arr,start,end):
    if end<=start:
        return
    pivot=partion(arr,start,end)
    quickSort(arr,start,pivot-1)
    quickSort(arr,pivot+1,end)


arr = [9, 27, 9, 3, 38, 82, 10]
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)