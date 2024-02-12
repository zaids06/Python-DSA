class Node:
    def __init__(self,n):
        self.value = n
        self.next = None
def insert ():
    nodelist = [int(ele) for ele in input().split()]
    head=None
    for curele in nodelist:
        if(curele ==-1):
            break
        if head is None:
            head=Node(curele)
        else:
            cur=head
            while cur.next is not None: cur=cur.next
            cur.next=Node(curele)
    return head
def printLinkedList(head):
    cur =head
    while cur is not None:
        print(cur.value)
        cur=cur.next

head=insert()
printLinkedList(head)
