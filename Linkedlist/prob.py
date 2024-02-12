

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert():
    nodelist = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for curele in nodelist:
        if (curele == -1):
            break
        cur = Node(curele)
        if head is None:
            head = cur
            tail = cur
        else:
            tail.next=cur
            tail = tail.next
    return head

def length(head):
    cur = head
    count=0
    while cur is not None:
        count+=1
        cur = cur.next
    return count


head = insert()
length(head)
    #Your code goes here