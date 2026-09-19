# I use a dummy node to simplify swapping pairs, especially when the first pair is involved.
# For each pair, I first store the next node after the pair so I don't lose the remaining list.
# Then I reverse the two nodes by updating their `next` pointers and connect the swapped pair using `prev`.
# Finally, I move `prev` and `cur` to the next pair and return `dummy.next`.
# The solution runs in O(n) time and O(1) space**.



class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = npn
            prev.next = second

            prev = cur
            cur = npn
        
        return dummy.next