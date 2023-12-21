def merge(arr, low, mid, high):
    length1 = mid - low + 1
    length2 = high - mid
    i = 0
    j = 0
    k = low
    subarr1 = [None] * length1
    subarr2 = [None] * length2

    for l in range(low, mid + 1):
        subarr1[i] = arr[l]
        i += 1

    for l in range(mid + 1, high + 1):
        subarr2[j] = arr[l]
        j += 1

    i = j = 0
    while i < length1 and j < length2:
        if subarr1[i] < subarr2[j]:
            arr[k] = subarr1[i]
            i += 1
        else:
            arr[k] = subarr2[j]
            j += 1
        k += 1

    while i < length1:
        arr[k] = subarr1[i]
        i += 1
        k += 1

    while j < length2:
        arr[k] = subarr2[j]
        j += 1
        k += 1

def mergeSort(arr: [int], low: int, high: int):
    if high <= low:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)


def mergeSort(arr: [int], l: int, r: int):
    if r<=l:
        return
    mid=(l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)


arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)