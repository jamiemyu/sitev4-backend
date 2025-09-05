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
    if (len(stock_price) < 2):
        raise ValueError('Must have at least two stock prices')

    max_profit = 0

    best_max_profit = stock_price[1] - stock_price[0]
    current_min_price = stock_price[0]

    for i in range(1, len(stock_price)):
        current_price = stock_price[i]
        
        max_profit = current_price - current_min_price
        if max_profit > best_max_profit:
            best_max_profit = max_profit

        if current_price < current_min_price:
            current_min_price = current_price

    return best_max_profit


print('get_max_profit([10, 7, 5, 8, 11, 9]) = ' + str(get_max_profit([10, 7, 5, 8, 11, 9])))


def get_min_num_coins(coins, total: float) -> float:
    """
    Returns the minimum number of coins needed to produce a given total.
    Returns -1 if the total cannot be produced with the given coins.
    """
    coins.sort(reverse=True)
    if total < min(coins):
        return -1
    
    min_num_coins = 0
    remaining = total
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            min_num_coins += 1
    
    if remaining == 0:
        return min_num_coins
    else:
        return -1


print('get_min_num_coins([1, 5, 10, 25], 30) = ' + str(get_min_num_coins([1,5,10,25], 30)))
