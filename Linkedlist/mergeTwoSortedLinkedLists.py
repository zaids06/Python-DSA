from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists(head1, head2):
    fh = ft = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        fh = ft = head1
        head1 = head1.next
    else:
        fh = ft = head2
        head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next  # make changes in this
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next  # here too

        # instead of ft.next here do it case wise
    if head1 is not None:
        ft.next = head1
    elif head2 is not None:
        ft.next = head2
    return fh


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1