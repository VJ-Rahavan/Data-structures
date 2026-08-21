class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sizes = sum(bobSizes)

        diff = (bob_sizes - alice_sum) // 2

        alice_set = set(bobSizes)

        for x in aliceSizes:
            y = x + diff
            if y in alice_set:
                return [x,y]

