# * We generate every possible **3-digit number** using three different indices.
# * The **hundreds digit cannot be 0**, and the **last digit must be even**.
# * We use a `set` to avoid counting duplicate numbers when the input contains duplicate digits.
# * Finally, return the size of the set as the number of unique valid 3-digit even numbers.
# * **Time:** O(n³), **Space:** O(n³) in the worst case.


class Solution:
    def totalNumbers(self, digits):
        nums = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(num)

        return len(nums)
