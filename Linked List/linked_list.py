class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    # Delete first occurrence of a value
    def delete(self, key):
        if not self.head:
            return

        # Delete head
        if self.head.data == key:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

    # Search for a value
    def search(self, key):
        curr = self.head

        while curr:
            if curr.data == key:
                return True
            curr = curr.next

        return False

    # Print the list
    def display(self):
        curr = self.head

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("None")