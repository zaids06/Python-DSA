from sys import stdin

def internal(arr,d):
    if d==0:
        return
    length = len(arr)
    arr2=[]
    for i in range(d,length):
        arr2.append(arr[i])
    for i in range(0,d):
        arr2.append(arr[i])
    return arr2

def rotate(arr, n, d):
    d%=n
    return internal(arr,d)


# Taking Input Using Fats I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    arr=rotate(arr, n, d)
    printList(arr, n)

    t -= 1