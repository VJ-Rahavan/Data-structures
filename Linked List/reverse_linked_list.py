class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def reverse_copy(self):
        cur = self.head
        new_head = None

        while cur:
            temp = Node(cur.data)     # Create a new node
            temp.next = new_head      # Insert at the front
            new_head = temp           # Update new head
            cur = cur.next            # Move to next node

        return new_head

    def reverse(self):
        prev = None
        cur = self.head

        while cur:
            next_node = cur.next      # Save next node
            cur.next = prev           # Reverse the pointer
            prev = cur                # Move prev forward
            cur = next_node           # Move current forward

        self.head = prev              # Update the head

    def display(self, head=None):
        if head is None:
            head = self.head

        cur = head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


# ------------------------
# Driver Code
# ------------------------

ll = LinkedList()

ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)

print("Original Linked List:")
ll.display()

new_head = ll.reverse_copy()

print("New Reversed Linked List:")
ll.display(new_head)

print("Original Linked List (Still Unchanged):")
ll.display()