# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            linkedList = lists[i]
            if linkedList is not None:
                heapq.heappush(heap, (linkedList.val, i, linkedList))
        
        res = ListNode(-1)
        cur  = res

        while heap:
            node, i, linkedList = heapq.heappop(heap)

            cur.next = ListNode(node)
            cur = cur.next
            
            if linkedList.next:
                heapq.heappush(heap, (linkedList.next.val, i, linkedList.next))
        
        return res.next


        
