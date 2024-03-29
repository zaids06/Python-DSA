from sys import stdin


def pairSum(arr, n, num):
    arr.sort()
    count = 0
    l=0
    r=n-1
    while l<r:
        if arr[l]+arr[r]==num:
            if arr[l] == arr[r]:
                total = (r - l) + 1
                total *= (total - 1)
                count = total // 2
                break
            elif arr[l] == arr[l + 1] or arr[r] == arr[r - 1]:
                countl, countr = 1, 1
                while l<r and arr[l]+arr[r]==num:
                        if arr[l+1]!=arr[l] and arr[r-1]!=arr[r]:
                            l+=1
                            break
                        if arr[l+1]==arr[l]:
                            countl+=1
                            l+=1
                        if arr[r-1]==arr[r]:
                            countr+=1
                            r-=1
                        count = countl * countr
        elif arr[l]+arr[r]>num:
            r-=1
        else:
            l+=1
    return count

# Your code goes here


# taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1