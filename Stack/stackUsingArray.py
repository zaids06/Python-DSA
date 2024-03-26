class Stack:
    def __init__(self):
        self.ls=[]
    def isEmpty(self):
        if len(self.ls)==0:
            return True
        else :
            return False
    def size(self): return len(self.ls)
    def push(self,x):
        self.ls.append(x)
    def top(self):
        if self.size()==0:
            print("Stack is empty")
        else:
            print(self.ls[self.size()-1])
    def pop (self):
        if self.size()==0:
            print("Stack is empty")
        else:
            print(self.ls.pop())
ob=Stack()
ob.push(3)
ob.push(4)
ob.push(5)
ob.pop()
ob.pop()
ob.pop()
ob.pop()