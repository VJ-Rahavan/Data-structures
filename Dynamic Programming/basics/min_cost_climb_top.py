
# I use bottom-up DP from right to left, where `cost[i]` represents the minimum cost to reach the top starting from stair `i`.
# From each stair, I can move either one or two steps, 
# so I choose the cheaper option: `cost[i] += min(cost[i+1], cost[i+2])`.
# I append `0` to represent the top, which has no cost.
# Since I can start from stair `0` or `1`, the final answer is `min(cost[0], cost[1])`.


# This is the key thing I want you to remember:
# cost[i] = minimum cost to reach TOP starting from stair i.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
