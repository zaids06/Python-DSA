from sys import stdin


def findUnique(arr, n):
    length = len(arr)
    if length==1:
        return arr[0]
    arr.sort()
    for i in range(1,length):
       if arr[i] != arr[i-1]:
           if length-1==i:
               return arr[i]
           elif arr[i]!=arr[i+1]:
               return arr[i]

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
    print(findUnique(arr, n))

    t -= 1