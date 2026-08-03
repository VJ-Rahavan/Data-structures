

#optimal solution
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def merge_sorted_list(l1, l2):

    dummy = Node(-1)
    tail = dummy

    while l1 and l2:

        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1

    if l2:
        tail.next = l2

    return dummy.next
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def merge_sorted_list(l1, l2):

    head = None
    tail = None

    curr1 = l1
    curr2 = l2

    while curr1 and curr2:

        if curr1.val <= curr2.val:
            new_node = Node(curr1.val)
            curr1 = curr1.next
        else:
            new_node = Node(curr2.val)
            curr2 = curr2.next

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    while curr1:
        new_node = Node(curr1.val)

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

        curr1 = curr1.next

    while curr2:
        new_node = Node(curr2.val)

        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

        curr2 = curr2.next

    return head