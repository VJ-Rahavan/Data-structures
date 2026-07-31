# I track the minimum price seen so far as I iterate through the array.
# For every price, I compute the profit if I sold today (current price - min so far)
# and update the maximum profit. Since I only need one pass and constant space,
# the time complexity is O(n) and space is O(1).

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
