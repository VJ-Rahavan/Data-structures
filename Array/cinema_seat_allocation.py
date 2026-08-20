from collections import defaultdict
from typing import List

# I group the reserved seats by row and ignore seats 1 and 10 
# because they cannot be part of any valid four-seat family block. 
# I initially assume every row can fit two families, giving 2 * n. 
# For rows with reservations, I check whether the left, middle, and right blocks are free using isdisjoint(). 
# If both left and right are free, two families fit; if any one block is free, one fits; otherwise, none fit.
# Time: O(R), Space: O(R), where R is the number of reserved seats.

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT   = {2, 3, 4, 5}
        MIDDLE = {4, 5, 6, 7}
        RIGHT  = {6, 7, 8, 9}

        rows = defaultdict(set)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r].add(s)

        total = 2 * n
        for reserved in rows.values():
            left_free   = reserved.isdisjoint(LEFT)
            mid_free    = reserved.isdisjoint(MIDDLE)
            right_free  = reserved.isdisjoint(RIGHT)

            if left_free and right_free:
                continue                 
            elif left_free or mid_free or right_free:
                total -= 1               
            else:
                total -= 2               

        return total