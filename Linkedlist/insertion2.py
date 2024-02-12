class Node:
    def __init__(self, n):
        self.value = n
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


def printLinkedList(head):
    cur = head
    while cur is not None:
        print(cur.value, end=' -> ')
        cur = cur.next
    print("None")


head = insert()
printLinkedList(head)
