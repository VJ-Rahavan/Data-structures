#Optimal Solution
# I maintain a gap of k nodes between the fast and slow pointers. 
# First, I move the fast pointer k steps ahead. 
# Then I move both pointers one step at a time. 
# When the fast pointer reaches the end of the list, the slow pointer is exactly k nodes from the end.
def kth_node_from_last(head, k):
    fast = head
    slow = head

    # Move fast k steps ahead
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    # Move both pointers together
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


def kth_node_from_last(head, k):
    # First pass: Find the length
    n = 0
    cur = head

    while cur:
        n += 1
        cur = cur.next

    # Handle invalid k
    if k > n or k <= 0:
        return -1

    # Second pass: Go to the (n-k)th index (0-based)
    target = n - k

    cur = head
    i = 0

    while cur:
        if i == target:
            return cur.data

        cur = cur.next
        i += 1

    return -1