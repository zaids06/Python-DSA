from sys import stdin


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Define data members and __init__()
    def __init__(self):
        self.head = None
        self.count = 0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.count

    # Implement the getSize() function

    def isEmpty(self):
        if (self.count == 0):
            return True
        else:
            return False

    # Implement the isEmpty() function

    def push(self, data):
        ob = Node(data)
        self.count += 1
        if (self.isEmpty()):
            self.head = ob
        else:
            ob.next = self.head
            self.head = ob

    # Implement the push(element) function

    def pop(self):
        if (self.isEmpty()):
            return -1
        else:
            ob = self.head
            self.head = self.head.next
            self.count -= 1
            return ob.data

    # Implement the pop() function

    def top(self):
        if (self.isEmpty()):
            return -1
        return self.head.data


def isBalanced(expression):
    length = len(expression)
    stack = Stack()
    for i in range(length):
        if (expression[i] == '('):
            stack.push(expression[i])
        elif expression[i] == ')':
            if (stack.top() != '('):
                return False
            else:
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False


# Your code goes here


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")
