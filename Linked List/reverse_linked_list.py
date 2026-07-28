# Reverse a linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# New linked list is created with the reversed order of the original linked list. 
# The function takes the head of the original linked list as input 
# and returns the head of the new reversed linked list.
def reverse_linked_list(data):
    if not data:
        return
    
    cur = data.next
    new_ll = Node(data.data)
    
    while cur:
        temp = Node(cur.data)
        temp.next = new_ll
        new_ll = temp
        cur = cur.next
    
    return new_ll


head = Node(4)
head.next = Node(2)

reverse_linked_list(head)