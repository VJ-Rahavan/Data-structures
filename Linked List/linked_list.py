class Node:
    def __init__(self, data):
        # Stores the value of the node
        self.data = data

        # Points to the next node
        self.next = None


class LinkedList:
    def __init__(self):
        # Initially the linked list is empty
        self.head = None

    # ----------------------------------------
    # Insert at Beginning
    # ----------------------------------------
    def insert_at_begin(self, data):
        # Create a new node
        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # Update head to the new node
        self.head = new_node

    # ----------------------------------------
    # Insert at End
    # ----------------------------------------
    def insert_at_last(self, data):
        new_node = Node(data)

        # If list is empty, new node becomes head
        if not self.head:
            self.head = new_node
            return

        # Traverse to the last node
        cur = self.head
        while cur.next:
            cur = cur.next

        # Last node points to new node
        cur.next = new_node

    # ----------------------------------------
    # Delete by Value
    # ----------------------------------------
    def delete(self, data):

        # Empty list
        if not self.head:
            return

        # If head itself should be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        cur = self.head
        prev = None

        # Traverse until value is found
        while cur:
            if cur.data == data:
                # Skip current node
                prev.next = cur.next
                return

            prev = cur
            cur = cur.next

    # ----------------------------------------
    # Search
    # ----------------------------------------
    def search(self, data):

        cur = self.head

        while cur:
            if cur.data == data:
                return True

            cur = cur.next

        return False

    # ----------------------------------------
    # Count Nodes
    # ----------------------------------------
    def count_nodes(self):

        cur = self.head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

    # ----------------------------------------
    # Display Linked List
    # ----------------------------------------
    def display(self):

        cur = self.head

        while cur:
            print("Data ->", cur.data)
            cur = cur.next

    # ----------------------------------------
    # First Node
    # ----------------------------------------
    def first_node(self):

        if not self.head:
            return None

        return self.head.data

    # ----------------------------------------
    # Last Node
    # ----------------------------------------
    def last_node(self):

        if not self.head:
            return None

        cur = self.head

        # Move until next becomes None
        while cur.next:
            cur = cur.next

        return cur.data

    # ----------------------------------------
    # Delete by Position (1-based indexing)
    # ----------------------------------------
    def delete_by_position(self, position):

        # Empty list
        if not self.head:
            return

        # Delete first node
        if position == 1:
            self.head = self.head.next
            return

        cur = self.head
        prev = None
        count = 1

        while cur:

            if count == position:
                # Remove current node
                prev.next = cur.next
                return

            prev = cur
            cur = cur.next
            count += 1