# nodesBetweenCriticalPoints [ 2058]

#My Approach 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        cur = head
        prev = None
        idx = 0

        while cur:
            if prev and cur.next:
                if (
                    prev.val < cur.val > cur.next.val
                    or prev.val > cur.val < cur.next.val
                ):
                    arr.append(idx)
            prev = cur
            cur = cur.next
            idx += 1
        if not arr or len(arr) < 2:
            return [-1, -1]

        maxx = max(arr)
        minn = min(arr)
        res = float("inf")

        for i in range(1, len(arr) - 1):
            res = min(res, arr[i] - arr[i - 1], arr[i + 1] - arr[i])

        if res == float("inf"):
            res = maxx - minn
        return [res, maxx - minn]

#Optimized approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        prev = None
        idx = 0
        last = -1
        first = -1
        min_dist = float("inf")

        while cur and cur.next:
            if prev:
                if (
                    prev.val < cur.val > cur.next.val
                    or prev.val > cur.val < cur.next.val
                ):
                    if first == -1:
                        first = idx
                    else:
                        min_dist = min(min_dist, idx - last)
                    last = idx

            prev = cur
            cur = cur.next
            idx += 1
            
        if first == last:
            return [-1, -1]
       
        return [min_dist, last - first]
