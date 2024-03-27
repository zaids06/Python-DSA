from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Define data members and __init__()
    def __init__(self):
        self.head = None
        self.count=0
    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.count
    # Implement the getSize() function

    def isEmpty(self):
        if(self.count==0):
            return True
        else:
            return False
    # Implement the isEmpty() function

    def push(self, data):
        ob= Node(data)
        self.count+=1
        if(self.isEmpty()):
            self.head =ob
        else:
            ob.next= self.head
            self.head=ob
    # Implement the push(element) function

    def pop(self):
        if(self.isEmpty()):
            return -1
        else:
            ob= self.head
            self.head=self.head.next
            self.count-=1
            return ob.data
    # Implement the pop() function

    def top(self):
        if(self.isEmpty()):
            return -1
        return self.head.data

# Implement the top() function


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1