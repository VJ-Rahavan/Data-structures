# I first group the stones based on stone % 3, 
# because only the remainder affects whether the running sum becomes divisible by 3. 
# Remainder-0 stones don’t change the sum’s remainder but do consume a turn, 
# so their parity determines the game structure. 
# If the number of remainder-0 stones is even, Alice needs at least one remainder-1 and one remainder-2 stone. 
# If it’s odd, Alice wins only when the counts of remainder-1 and remainder-2 stones differ by more than 2. 
# This gives an O(n) solution with O(1) extra space.

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0
        else:
            return abs(count[1] - count[2]) > 2