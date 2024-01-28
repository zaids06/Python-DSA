from sys import stdin


def pairSum(arr, length, num):
    arr.sort()
    ans=0
    for i in range(length-3):
        low=i+1
        high=length-1
        while low<high:
            curSum=arr[i]+arr[low]+arr[high]
            if curSum==num:
                ans+=1
                tempHigh=high-1
                while arr[tempHigh]==arr[high]and tempHigh>low:
                    ans+=1
                    tempHigh-=1
                low+=1
            elif curSum>num:
                high-=1
            else:
                low+=1
    return ans
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