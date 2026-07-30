#optimal approach
# I initialize two pointers at the head. The slow pointer moves one node at a time, 
# while the fast pointer moves two nodes. 
# If the list has no cycle, the fast pointer eventually reaches None. 
# If a cycle exists, the fast pointer will eventually catch the slow pointer inside the cycle, and I return True.
def is_linked_list_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False



# I traverse the linked list while maintaining a hash set of visited nodes. 
# Before processing each node, I check whether it already exists in the set. 
# If it does, I've encountered the same node again, indicating a cycle, 
# so I return True. If I reach None, the list has no cycle, and I return False.

def is_linked_list_cycle(head):
    
    seen = set()
    cur = head
    
    while cur:
        if cur in seen:
            return True
        else:
            seen.add(cur)
            cur = cur.next
            
    return False