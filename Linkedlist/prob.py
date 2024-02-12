'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def length(head):
    cur = head
    count=0
    while cur is not None:
        count+=1
        cur = cur.next


# Your code goes here