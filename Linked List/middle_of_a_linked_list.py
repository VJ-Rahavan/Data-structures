# 3. Find the middle node

# I use two pointers: a slow pointer and a fast pointer. 
# The slow pointer moves one node at a time, 
# while the fast pointer moves two nodes at a time. 
# When the fast pointer reaches the end of the list, 
# the slow pointer has traversed only half the distance and therefore points to the middle node. 
# This gives an O(n) time solution with O(1) extra space.

def middle_linked_list(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow