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


def reverse(head):
    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev


def is_palindrome(head):

    if head is None or head.next is None:
        return True

    # Step 1: Find the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Skip the middle node for odd-length lists
    if fast:
        slow = slow.next

    print("Second Half:")
    print_ll(slow)

    # Step 2: Reverse the second half
    second_half = reverse(slow)

    print("\nReversed Second Half:")
    print_ll(second_half)

    # Step 3: Compare both halves
    first_half = head
    temp = second_half

    while temp:
        if first_half.val != temp.val:
            print("\nNot a Palindrome")
            return False

        first_half = first_half.next
        temp = temp.next

    print("\nPalindrome")
    return True


# -----------------------
# Example
# -----------------------

LList = Node(5)
LList.next = Node(2)
LList.next.next = Node(2)
LList.next.next.next = Node(5)

print("Original List:")
print_ll(LList)

print()
print(is_palindrome(LList))