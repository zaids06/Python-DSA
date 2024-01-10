from sys import stdin


def arrayEquilibriumIndex(arr, n):
    length=len(arr)
    for i in range(1,length):
        arr[i]+=arr[i-1]
    for i in range (1,length):
        if arr[i-1]==arr[length-1]-arr[i]:
            return i
    return -1

# Your code goes here


# Taking input using fast I/O method
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
    print(arrayEquilibriumIndex(arr, n))

    t -= 1