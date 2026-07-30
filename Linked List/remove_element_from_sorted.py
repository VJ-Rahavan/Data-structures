# Input: head = [1,1,2]
# Output: [1,2]

# Since the linked list is sorted, duplicate values will always be adjacent, 
# so I only need to compare the current node with its next node. 
# If both values are the same, I remove the next node by updating cur.next without moving cur, 
# as there may be more duplicates. If they're different, I move cur forward. 
# This traverses the list once, giving O(n) time complexity and O(1) extra space.

def remove_element_sorted_ll(head):
    
    if not head:
        return None
    
    cur = head
    
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    
    return head