# I first count the customers who are naturally satisfied when `grumpy[i] == 0`.
# Then I use a fixed-size sliding window of `minutes` to calculate the maximum additional customers that can be satisfied.
# As the window moves, I add the contribution of the new right element and remove the contribution of the outgoing left element.
# Finally, I return the naturally satisfied customers plus the maximum additional customers from any window.
# **Time:** `O(n)` | **Space:** `O(1)`


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        satisfied_customers = 0
        start = 0
        additional_customers = 0
        max_window = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]

            if grumpy[i] == 1:
                additional_customers += customers[i]

            while i - start + 1 > minutes:
                if grumpy[start] == 1:
                    additional_customers -= customers[start]
                start += 1

            max_window = max(additional_customers, max_window)

        return satisfied_customers + max_window
