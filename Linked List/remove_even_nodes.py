def remove_even_node(head):
    cur = head

    while cur and cur.next:
        cur.next = cur.next.next
        cur = cur.next
    
    return head