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

def countNodes(head):
    count=0
    cur=head
    while cur is not None:
        count+=1
        cur=cur.next
    return count
def insertIth(head,i,data):
    if(i<0 or i>countNodes(head)):
        return head
    newnode = Node(data)
    prev=None
    cur=head
    while i>0:
        prev=cur
        cur=cur.next
        i-=1
    if(prev is None):
        head=newnode
    else:
        prev.next=newnode
    newnode.next=cur
    return head
def printLinkedList(head):
    cur =head
    while cur is not None:
        print(cur.value)
        cur=cur.next

head=insert()
printLinkedList(head)
n=int(input("Enter the index"))
data=int(input("Enter the data"))
head=insertIth(head,n,data)
printLinkedList(head)
