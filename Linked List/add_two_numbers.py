# 2. Add Two Numbers


# I traverse both linked lists together, adding their corresponding digits along with the carry from the previous position.
# If one list is shorter, I treat its missing digit as `0`.
# For each sum, I store `sum % 10` as the current digit and `sum // 10` as the carry.
# Finally, if a carry remains after the loop, I add it as the last node.
# **Time:** O(max(n, m)) | **Space:** O(max(n, m)) for the result list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(-1)
        fin = res
        r = 0
        while l1 or l2:
            val = r
            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            r = val // 10
            res.next = ListNode(val%10)
            res = res.next
        
        if r > 0:
            res.next = ListNode(r)


        return fin.next