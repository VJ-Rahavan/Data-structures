import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        base = ""

        while head:
            base = str(head.val) + base
            head = head.next

        pow = len(base) - 1
        res = 0

        while pow >= 0:
            cur = int(base[pow]) * int(math.pow(2,pow))
            res += cur
            pow -= 1
        
        return res

#optimal approach
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0

        while head:
            res = res * 2 + head.val
            head = head.next

        return res