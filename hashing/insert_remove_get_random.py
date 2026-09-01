# 380. Insert Delete GetRandom O(1)

# I use an array and a hashmap to make all three operations O(1).
# The array stores the values, so getRandom() can randomly pick an index in O(1).
# The hashmap stores each value and its index in the array, so insert() and remove() can find elements in O(1).
# For removal, I don't shift elements because that would be O(n). 
# Instead, I move the last element into the position of the element I'm removing, 
# update its index in the hashmap, and then pop() the last element.
# Therefore, insert, remove, and getRandom are all O(1).