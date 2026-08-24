# I maintain a frequency map for nums2 because nums2 is frequently updated while nums1 remains unchanged.
# For each value in nums1, I calculate its required complement as tot - num and add its frequency from the map.
# In add(), I decrement the old value's frequency and increment the new value's frequency.
# This makes add() O(1) average and count() O(n).

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr = nums1
        self.arr2 = nums2
        self.freq = {}
        for num in nums2:
            self.freq[num] = self.freq.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        d = self.arr2[index]
        self.freq[d] -= 1
        self.freq[d + val] = self.freq.get(d + val, 0) + 1
        if self.freq[d] == 0:
            del self.freq[d]
        self.arr2[index] = d + val

    def count(self, tot: int) -> int:
        count = 0
        for i in self.arr:
            diff = tot - i
            if diff in self.freq:
                count += self.freq[diff]

        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
