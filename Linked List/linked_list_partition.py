class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def partition(head, x):
    less_dummy = Node(0)
    greater_dummy = Node(0)

    less = less_dummy
    greater = greater_dummy

    current = head

    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next

        current = current.next

    # Prevent cycle
    greater.next = None

    # Join both lists
    less.next = greater_dummy.next

    return less_dummy.next