"""
The idea of a greedy algorithm is to use trackers (for min/max) to
find the "best" value while going through a data structure.
Once the element/node is visited, it is decided upon and we don't come back to it.

Typically, we store at least 2 values:
1) The "best" found value so far (whether it's a max or a min)
2) Any additional trackers needed to compare against the future elements visited
   further in the data structure.
"""


def get_max_profit(stock_price) -> float:
    """
    Returns the maximum value profit you could make from a list of stock prices.
    ex. 1
    input: [10, 7, 5, 8, 11, 9]
    output: 6

    ex. 2
    input: [10, 8, 1]
    output: -2 (purchase at 10, sell at 8)

    Questions:
    - Ex. 2 --> Maximum profit is negative because any purchase results in a re-sell at a lower value. Is that OK to return?
    - Can a stock price be <0?
    """
    if len(stock_price) < 2:
        raise ValueError("Must be at least 2 stock prices provided!")

    max_profit = stock_price[1] - stock_price[0]

    # Keep track of the best minimum found so far. This will be used to compute the maximal profit.
    # Profit = Sale price (max) - Purchase price (min)
    min_so_far = stock_price[0]

    for i in range(1, len(stock_price), 1):
        price = stock_price[i]

        profit = price - min_so_far
        if profit > max_profit:
            max_profit = profit
        
        # Replace the min price if we find it to be less than min so far
        if price < min_so_far:
            min_so_far = price

    return max_profit


print(
    "get_max_profit([10, 7, 5, 8, 11, 9]) = "
    + str(get_max_profit([10, 7, 5, 8, 11, 9]))
)
print(
    "get_max_profit([10, 8, 1]) = "
    + str(get_max_profit([10, 8, 1]))
)


def get_min_num_coins(coins, total: float) -> float:
    """
    Returns the minimum number of coins needed to produce a given total.
    Returns -1 if the total cannot be produced with the given coins.
    """
    if total < min(coins):
        print("Total is less than any coin value provided!")
        return -1

    # Try the largest coin first to minimize the number of coins we need to use.
    coins.sort(reverse=True)

    # Track the minimum to be returned.
    min_num_coins = 0
    # Track what is remaining of the total.
    remaining = total
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            min_num_coins += 1

    if remaining == 0:
        return min_num_coins
    # If anything is leftover, there is no possible combination of coins that can be used for change.
    else:
        return -1


print(
    "get_min_num_coins([1, 5, 10, 25], 30) = "
    + str(get_min_num_coins([1, 5, 10, 25], 30))
)
