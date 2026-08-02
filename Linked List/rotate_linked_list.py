class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

# First, find the length of the linked list and compute k % length to avoid unnecessary rotations. 
# Connect the tail to the head to form a circular linked list. 
# Then move to the (length - k - 1)th node, which becomes the new tail. 
# The next node becomes the new head, and finally break the circular link.  

def rotate_linked_list(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    tail = head
    length = 1

    while tail.next:
        tail = tail.next
        length += 1

    # Handle k greater than length
    k %= length

    if k == 0:
        return head

    # Make the list circular
    tail.next = head

    # Find the new tail
    steps = length - k - 1
    new_tail = head

    for _ in range(steps):
        new_tail = new_tail.next

    # New head
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None

    return new_head