# 380. Insert Delete GetRandom O(1)

# I use an array and a hashmap to make all three operations O(1).
# The array stores the values, so getRandom() can randomly pick an index in O(1).
# The hashmap stores each value and its index in the array, so insert() and remove() can find elements in O(1).
# For removal, I don't shift elements because that would be O(n). 
# Instead, I move the last element into the position of the element I'm removing, 
# update its index in the hashmap, and then pop() the last element.
# Therefore, insert, remove, and getRandom are all O(1).


import random


class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        idx = self.indices[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.indices[last] = idx

        self.arr.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
