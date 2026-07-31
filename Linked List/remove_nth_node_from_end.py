class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def print_ll(head):
    cur = head

    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

# I use a dummy node before the head so that every node, including the original head, has a previous node. 
# I move the fast pointer n + 1 steps ahead to maintain a fixed gap. 
# Then I move both slow and fast until fast reaches the end. 
# At that point, slow is just before the node to delete, so I bypass it by updating slow.next.
def remove_nth_node(head, pos):

    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Move fast ahead by pos + 1 nodes
    for _ in range(pos + 1):
        if fast is None:
            return -1
        fast = fast.next

    # Move both pointers
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete the node
    slow.next = slow.next.next

    return dummy.next


# -----------------------
# Example
# -----------------------

LList = Node(5)
LList.next = Node(2)
LList.next.next = Node(2)
LList.next.next.next = Node(5)
LList.next.next.next.next = Node(4)
LList.next.next.next.next.next = Node(6)

print("Before:")
print_ll(LList)

LList = remove_nth_node(LList, 2)

print("After:")
print_ll(LList)