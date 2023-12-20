def checkleft(arr : [int], n, key):
    i=key
    while arr[i] == arr[i - 1] and i > 0:
        i -= 1
    return i

nums=[1,2,2,3,3,3,4,8,9,19,19,19]
low =0
x=8
high=len(nums)-1
while low<=high:
    mid=(low+high)//2
    if(nums[mid]==x):
        print(checkleft(nums,len(nums),mid))
        break
    elif (nums[mid]>x):
        high=mid-1
    else :
        low=mid+1
