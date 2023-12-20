def bsearch(arr,l,r,x):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return bsearch(arr,l,mid-1,x)
    else:
        return bsearch(arr,mid+1,r,x)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(bsearch(arr,0,n-1,x))